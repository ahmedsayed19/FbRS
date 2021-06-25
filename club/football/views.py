from django.shortcuts import render
from rest_framework import response
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework import status
from .models import ReservedHours, Playgrounds, ClubMember
from .serializers import MemeberSerializer, PGsSerializer, RHSerializer
from datetime import datetime
import json

# Registration
@api_view(['post'])
def register(request):
    '''
    INSERT INTO ClubMember(username, password, …)
    VALUES ('?', '?', …);
    '''
    try:
        exist = ClubMember.objects.get(username=request.data.get('username'))
    except:
        exist = None
    if exist:
        return Response(status.HTTP_409_CONFLICT)

    serializer = MemeberSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['post'])
def login(request):
    try:
        '''
        SELECT * FROM ClubMember WHERE username='?'
        '''
        member = ClubMember.objects.get(username=request.data.get('username'))
    except ClubMember.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    valid = member.check_password(request.data.get('password'))
    if valid:
        return Response(MemeberSerializer(member).data)
    return Response(status.HTTP_400_BAD_REQUEST)


# Playground
@api_view(['get', 'post'])
def get_post_playgrounds(request):
    if request.method == 'GET':
        pg_with_names = Playgrounds.objects.raw(
            '''
                SELECT football_playgrounds.id, name, photo, price, description, address, owner_id, football_clubmember.username FROM football_playgrounds JOIN football_clubmember on football_playgrounds.owner_id = football_clubmember.id
            '''
        )
        data = []
        for pg in pg_with_names:
            data.append({
                "id": pg.id,
                "name": pg.name,
                "photo": pg.photo or None,
                "price": pg.price,
                "description": pg.description,
                "address": pg.address,
                "owner": pg.owner_id,
                "owner_name": pg.username
            })
        return Response(data)
        # return Response({})
    if request.method == 'POST':
        try:
            is_owner = ClubMember.objects.get(pk=request.user.pk).is_owner
        except ClubMember.DoesNotExist:
            return Response(status.HTTP_403_FORBIDDEN)

        if not is_owner:
            # m = {"message": "You are Not an owner nigga !!"}
            return Response(status.HTTP_403_FORBIDDEN)
        data = {
            "name": request.data.get("name"),
            "photo": request.data.get("photo"),
            "price": int(request.data.get("price")),
            "description": request.data.get("description"),
            "address": request.data.get("address"),
            "owner": request.user.pk,
        }

        if data["owner"] == None:
            return Response(status.HTTP_403_FORBIDDEN)
            
        serializer = PGsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['put', 'get', 'delete'])
def put_get_delete_playground(request, pk):
    try:
        playground = Playgrounds.objects.get(pk=pk)
        
    except Playgrounds.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # owner_name = ClubMember.objects.get(pk=playground.owner).username
        res_hours_with_names = ReservedHours.objects.raw("SELECT football_reservedhours.id, playground_id_id, reserved_hour, player_id, football_clubmember.username FROM football_reservedhours JOIN football_clubmember ON football_reservedhours.player_id=football_clubmember.id WHERE  football_reservedhours.playground_id_id = %s", [pk])
        rh_data = []
        for res_hour in res_hours_with_names:
            rh_data.append({
                "reserved_hour": res_hour.reserved_hour,
                "playground_id": res_hour.playground_id_id,
                "player": res_hour.player_id,
                "player_name": res_hour.username
            })
        pg_serializer = PGsSerializer(playground)
        data = pg_serializer.data
        data['owner_name'] = playground.owner.username
        data['reserved_hour'] = rh_data
        return Response(data)

    # Updated to check that the request from the playground owner
    try:
        user = ClubMember.objects.get(username=request.user.username)
    except ClubMember.DoesNotExist:
        m = {"message": "You are not even a user !!"}
        return Response({json.dumps(m)}, status.HTTP_403_FORBIDDEN)
    if not user.is_owner:
        m = {"message": "You are Not an owner !!"}
        return Response({json.dumps(m)},status.HTTP_403_FORBIDDEN)
    if playground.owner != user:
        m = {"message": "You are Not The owner of this PG nigga !!"}
        return Response({json.dumps(m) },status.HTTP_403_FORBIDDEN)
    
    if request.method == 'PUT':
        '''
        UPDATE Playgrounds
        SET column1 = value1,
            column2 = value2,
            ...
        WHERE id = pk;
        '''
        data = {
            "name": request.data.get("name"),
            "photo": request.data.get("photo"),
            "price": int(request.data.get("price")),
            "description": request.data.get("description"),
            "address": request.data.get("address"),
            "owner": user.pk,
        }

        serializer = PGsSerializer(playground, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        '''
        DELETE FROM Playgrounds WHERE id = pk
        '''
        playground.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Reserved Hours

@api_view(['post'])
def reserve_an_hour(request, pk):
    # try:
    #     playground = Playgrounds.objects.get(pk=pk)
    # except Playgrounds.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    try:
        member = ClubMember.objects.get(username=request.user)
    except ClubMember.DoesNotExist:
        return Response(status.HTTP_403_FORBIDDEN)
    date = datetime.strptime(request.data.get('reserved_hour'), '%m %d %Y %H')
    data = {
        'playground_id': pk,
        'reserved_hour': date,
        'player': member.pk
    }
    is_reserved = ReservedHours.objects.filter(playground_id=pk, reserved_hour=date).count()
    if is_reserved:
        return Response(status.HTTP_409_CONFLICT)
    serializer = RHSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        res_data = serializer.data
        res_data['player_name'] = member.username
        return Response(res_data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
@api_view(['get'])
def reserved_hours(request, pk):
    try:
        res_hours = ReservedHours.objects.filter(playground_id=pk)
        print(res_hours)
    except ReservedHours.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    serializer = RHSerializer(res_hours, many=True)
    return Response(serializer.data)

@api_view(['post'])
def post_member(request):
    serializer = MemeberSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

# "SELECT football_reservedhours.id, playground_id_id reserved_hour, player_id, football_clubmember.username FROM football_reservedhours JOIN football_clubmember ON football_reservedhours.playground_id_id=football_clubmember.id WHERE football_reservedhours.playground_id_id = %s"
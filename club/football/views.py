from django.shortcuts import render
from rest_framework import response
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework import status
from .models import ReservedHours, Playgrounds, ClubMember
from .serializers import MemeberSerializer, PGsSerializer, RHSerializer
from datetime import datetime

# Create your views here.
@api_view(['get', 'post'])
def get_post_playgrounds(request):
    if request.method == 'GET':
        pgs = Playgrounds.objects.all()
        serializer = PGsSerializer(pgs, many=True)
        return Response(serializer.data)
        # return Response({})
    if request.method == 'POST':
        data = {
            "name": request.data.get("name"),
            "photo": request.data.get("photo"),
            "price": int(request.data.get("price")),
            "owner": request.user.pk or None,
        }
        if data["owner"] == None:
            return Response(status.HTTP_403_FORBIDDEN)
        serializer = PGsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['put', 'get'])
def edit_playground(request, pk):
    try:
        playground = Playgrounds.objects.get(pk=pk)
    except Playgrounds.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PGsSerializer(playground, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        serializer = PGsSerializer(playground)
        
        return Response(serializer.data)

@api_view(['post'])
def post_member(request):
    serializer = MemeberSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['post'])
def login(request):
    member = ClubMember.objects.get(username=request.data.get('username'))
    valid = member.check_password(request.data.get('password'))
    if valid:
        return Response(MemeberSerializer(member).data)
    return Response(status.HTTP_400_BAD_REQUEST)


@api_view(['get', 'put', 'delete'])
def get_put_delete_member(request, pk):
    try:
        cm = ClubMember.objects.get(pk=pk)
    except ClubMember.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MemeberSerializer(cm)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = MemeberSerializer(cm, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        cm.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['post'])
def reserve_an_hour(request, pk):
    # try:
    #     playground = Playgrounds.objects.get(pk=pk)
    # except Playgrounds.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        
        print("HEY:", request.user.username)
        member = ClubMember.objects.get(username=request.user)
        print("I'AM ", member)
        data = {
            'playground_id': pk,
            'reserved_hour': datetime.strptime(request.data.get('reserved_hour'), '%m %d %Y %I'),
            'player': member.pk
        }
        serializer = RHSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.contrib.auth.models import Group

from .models import ReservedHours, Playgrounds, ClubMember

# Register your models here.
class ClubMemberView(admin.ModelAdmin):
    exclude = ('last_login', 'is_superuser', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined', 'user_permissions', 'groups')
    list_display = ('username', 'is_owner', 'email', 'phone')
    
    list_filter = ('is_owner',)

class PlaygroundsView(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'price', 'address', 'description')

class ReservedHoursView(admin.ModelAdmin):
    list_display = ('playground_id', 'reserved_hour', 'player_id')
    
admin.site.register(ReservedHours, ReservedHoursView)
admin.site.register(Playgrounds,PlaygroundsView)
admin.site.register(ClubMember, ClubMemberView)
admin.site.unregister(Group)

admin.site.site_header = "Playground Reservation System"

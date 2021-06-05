from django.contrib import admin

from .models import ReservedHours, Playgrounds, ClubMember

# Register your models here.
admin.site.register(ReservedHours)
admin.site.register(Playgrounds)
admin.site.register(ClubMember)
# admin.site.register(Owners)
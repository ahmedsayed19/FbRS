from django.urls import path, include
from . import views


urlpatterns = [
    path('register', views.register),
    path('member/login', views.login),
    
    path('playgrounds', views.get_post_playgrounds),
    path('playgrounds/<int:pk>', views.put_get_delete_playground),

    path('reserve_h/<int:pk>', views.reserve_an_hour),
    path('reserved_hs/<int:pk>', views.reserved_hours),
]
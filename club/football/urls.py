from django.urls import path, include
from . import views


urlpatterns = [
    path('playgrounds', views.get_post_playgrounds, name='get_playgrounds'),
    path('playgrounds/<int:pk>', views.edit_playground, name='edit_pg'),
    
    path('reverse_h/<int:pk>', views.reserve_an_hour, name='reserve_an_hour'),

    path('member', views.post_member),
    path('member/login', views.login),
    path('member/<int:pk>', views.get_put_delete_member),

    
]
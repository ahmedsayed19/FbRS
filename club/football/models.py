from django.db import models
from django.db.models.base import ModelState
from django.db.models.deletion import CASCADE
from django.db.models.expressions import F
from django.test.testcases import TestCase
from django.contrib.auth.models import AbstractUser, User

class ClubMember(AbstractUser):
    __name__ = 'clubmember'
 
    profile_pic = models.ImageField(max_length=255, default='', null=True)
    phone = models.CharField(max_length=15, default='')
    is_owner = models.BooleanField(default=False)
    is_player = models.BooleanField(default=False)
    def __test__(self):
        return f"{self.username} {self.email} {self.profile_pic}"

    

class Playgrounds (models.Model):
    '''
    CREATE TABLE Playgrounds (
        name VARCHAR(255) UNIQUE,
        photo VARCHAR(255),
        price INT,
        description VARCHAR(300),
        address VARCHAR(200),
        FOREIGN KEY (owner)
        REFERENCES ClubMember (id)
    );
    '''
    name  = models.CharField(max_length=255, unique=True)
    photo = models.ImageField(max_length=255, null=True)
    price = models.IntegerField()
    description = models.CharField(max_length=300, default='', null=True)
    address = models.CharField(max_length=200, default='', null=True)
    owner = models.ForeignKey(ClubMember, on_delete=CASCADE, null=False, related_name='playground')

class ReservedHours (models.Model):
    __name__ = 'reservedhours'
    playground_id = models.ForeignKey(Playgrounds, on_delete=CASCADE, related_name='playground')
    reserved_hour = models.DateTimeField()
    player = models.ForeignKey(ClubMember, default='',on_delete=models.CASCADE)

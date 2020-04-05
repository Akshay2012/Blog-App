from django.db import models
from django.contrib.auth.models import User

from PIL import Image

# Create your models here.

class profile(models.Model):


    #CASCADE--If user deleted then profile deleted but not vice versa
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to="profile_pics")

    def __str__(self):
        return f'{self.user.username} PROFILE'
    
    #Already existing function being modified
    
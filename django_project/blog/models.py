from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content= models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)   #auto_now_add=True but this limits us from updating value ofthis date_posted
    author = models.ForeignKey(User,on_delete=models.CASCADE)  #If user is deleted then this post will be deleted as well
                                                                #User is not deleted when post is deleted.


                                                                #If you want to see sql code,then type this in cli : python manage.py  sqlmigrate blog 0001

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})
            
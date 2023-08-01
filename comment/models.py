from django.db import models
from user.models import user
from post.models import post
from manager.models import manager
# Create your models here.
class comment(models.Model):
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    text=models.TextField()
    post=models.ForeignKey(post, on_delete=models.CASCADE)
    accepted=models.BooleanField()
    
class commentService(models.Model):
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    text=models.TextField()
    manager=models.ForeignKey(manager, on_delete=models.CASCADE)
    accepted=models.BooleanField()
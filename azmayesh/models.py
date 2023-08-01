from django.db import models
from user.models import user
# Create your models here.
class azmayesh(models.Model):
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    image = models.ImageField('home/azmayesh/')
    created = models.DateTimeField(auto_now_add=True)
    descripton = models.TextField()
    response = models.TextField()
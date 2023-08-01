from django.db import models
from django import forms
from manager.models import manager
# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=20)
class post (models.Model):
    Choice =(
        ('image' , 'image'),
        ('podcast' ,'podcast'),
        ('video' ,'video'),
    )
    file=models.FileField(upload_to='home/post/')
    poster=models.ImageField('home/post/poster/' ,null=True)
    title =models.CharField(max_length=50)
    description=models.TextField()
    like=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    isDelete=models.BooleanField()
    types=models.CharField(max_length=10,choices=Choice)
    oprator=models.ForeignKey(manager, on_delete=models.CASCADE)
    category=models.ForeignKey(category,on_delete=models.CASCADE, blank=True, null=False)
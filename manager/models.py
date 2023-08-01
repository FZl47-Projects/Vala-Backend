from django.db import models
from django import forms
# Create your models here.
class manager(models.Model):
    Choice =(
        ('admin' , 'admin'),
        ('Feeding' ,'opratorF'),
        ('Wedding' ,'opratorW'),
        ('Beauty' ,'opratorB'),
        ('Photographic' ,'opratorP'),
        ('Medical' ,'opratorM'),
        ('Laboratory' ,'opratorL'),
        ('Sports' ,'opratorS'),
    )
    image = models.ImageField('admin/')
    name=models.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    created = models.DateTimeField(auto_now_add=True)
    types = models.CharField(max_length=20,choices=Choice)
    age=models.IntegerField()
    
    
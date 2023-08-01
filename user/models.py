from django.db import models
from django import forms
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=20)
    phone_number = PhoneNumberField(blank=True,region="IR",unique=True)
    age=models.IntegerField()
    weight = models.IntegerField()
    height=models.IntegerField()
    nationalcode = models.BigIntegerField()
    password = models.TextField()
    birthday= models.DateField()
    profileimage = models.ImageField('home/user/' ,null=True)
    created = models.DateTimeField(auto_now_add=True)
    wallet=models.BigIntegerField()
    pin = models.BooleanField(default=False)
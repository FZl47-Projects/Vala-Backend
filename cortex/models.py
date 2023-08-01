from django.db import models
from django import forms
from phonenumber_field.modelfields import PhoneNumberField
from user.models import user


class oprator_Laser(models.Model):
    name = models.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    phonenumber = PhoneNumberField(region="IR", unique=True)


class cortex(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    oprator_Las = models.ForeignKey(oprator_Laser, on_delete=models.CASCADE)
    descriptions = models.TextField()
    numbermeet = models.IntegerField()
    district = models.TextField()


class district(models.Model):
    name = models.CharField(max_length=50)

from django.db import models
from user.models import user
# Create your models here.
class routin (models.Model):
    Choice =(
        ('skin' , 'skin'),
        ('food' ,'food'),

    )
    name=models.CharField( max_length=50)
    types=models.CharField(max_length=10,choices=Choice)
    value=models.TextField()
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    created = models.DateTimeField( auto_now_add=True)
    isActive=models.BooleanField()
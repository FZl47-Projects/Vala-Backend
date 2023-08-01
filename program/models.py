from django.db import models
from user.models import user
from manager.models import manager
# Create your models here.
class food(models.Model):
    name=models.CharField(max_length=50)
    calories=models.IntegerField()
    value=models.IntegerField()
    oprator = models.ForeignKey(manager,on_delete=models.CASCADE)
class program(models.Model):
    Choice =(
        ('Food' , 'Food'),
        ('Sport' ,'Sport'),
    )
    user=models.ForeignKey(user,  on_delete=models.CASCADE)
    created = models.DateTimeField( auto_now_add=True)
    oprator = models.ForeignKey(manager,on_delete=models.CASCADE)
    types = models.CharField(max_length=20,choices=Choice)
    diet=models.TextField(null=True)
    
    
   

  
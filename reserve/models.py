from django.db import models
from manager.models import manager
from user.models import user
# Create your models here.
class service(models.Model):
    oprator = models.ForeignKey(manager, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.BigIntegerField()
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    
class reserve(models.Model):
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
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    date= models.DateField(auto_now=False, auto_now_add=True)
    oprator= models.ForeignKey(manager(), on_delete=models.CASCADE)
    accept= models.BooleanField()
    types = models.CharField(max_length=20,choices=Choice)
    description = models.TextField()

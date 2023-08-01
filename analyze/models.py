from django.db import models
from user.models import user
# Create your models here.
class analyze(models.Model):
    image1=models.ImageField('home/analyze/' ,null=True)
    image2=models.ImageField('home/analyze/' ,null=True)
    image3=models.ImageField('home/analyze/' ,null=True)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
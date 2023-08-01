from django.db import models
from user.models import user
class product(models.Model):
    name=models.CharField(max_length=50)
    description = models.TextField()
    price=models.FloatField()
    poster=models.ImageField('home/post/products/' ,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class order(models.Model):
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    user = models.ForeignKey(user,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
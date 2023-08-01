from django.db import models

# Create your models here.
class category (models.Model):
    name=models.CharField(max_length=25)
class story(models.Model):
    title = models.CharField(max_length=50)
    file=models.FileField(upload_to='home/story/')
    created=models.DateTimeField( auto_now_add=True)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
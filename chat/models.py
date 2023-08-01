from django.db import models
from user.models import user 
from manager.models import manager
# Create your models here.
class chat(models.Model):
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    ChoiceStatus=(
        ('admin','admin'),
        ('user','user'),
    )
    status=models.CharField(max_length=6,choices=ChoiceStatus)
    

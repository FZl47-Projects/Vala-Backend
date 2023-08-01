from django.db import models
from user.models import user
from manager.models import manager
# Create your models here.
class ticket(models.Model):
    message = models.TextField()
    user = models.ForeignKey(user, on_delete=models.CASCADE)

    ChoiceStatus=(
        ('ans','answerd'),
        ('wa','waiting'),
    )
    status = models.CharField( max_length=50 ,choices=ChoiceStatus)
    created = models.DateTimeField(auto_now_add=True)
    answerdTime = models.DateTimeField(auto_now=True)
    
    
    
class ticketReply(models.Model):
    ticket = models.ForeignKey(ticket, on_delete=models.CASCADE)
    message = models.TextField()    
    created = models.DateTimeField(auto_now_add=True)
    oprator= models.ForeignKey(manager, on_delete=models.CASCADE)
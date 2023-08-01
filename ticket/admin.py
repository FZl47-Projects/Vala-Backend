from django.contrib import admin
from .models import ticket,ticketReply
# Register your models here.
admin.site.register(ticket),
admin.site.register(ticketReply)

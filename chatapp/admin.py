from email import message
from django.contrib import admin
from .models import Room, Message #Import functions from models.py

# Register your models here.
admin.site.register(Room)
admin.site.register(Message)
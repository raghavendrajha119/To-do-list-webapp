from django.db import models
from django.contrib.auth.models import User
# defines database
# Create your models here.
# register apps in settings.py of project
# register model in admin.py
# make migrations update changes and store in a file
# migrate updates the database admin page
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default =1)
    Task=models.CharField(max_length=100)
    Reminder=models.TimeField(blank=True)
    Date=models.DateField(blank=True)
    def __str__(self):
        return self.Task
class Contact(models.Model):
    name= models.CharField(max_length=120)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=12)
    desc=models.TextField(blank=True,null = True)
    date=models.DateField()
    def __str__(self):
        return self.name


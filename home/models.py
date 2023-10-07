from django.db import models
# defines database
# Create your models here.
# register apps in settings.py of project
# register model in admin.py
# make migrations update changes and store in a file
# migrate updates the database admin page
class Contact(models.Model):
    name= models.CharField(max_length=120)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.name


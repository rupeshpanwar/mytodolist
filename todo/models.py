from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True,blank=True)
    important = models.BooleanField(default=False)
    #store the identity of user and setup a foreign key relationship with User model(table)
    #its 1-to-Many
    user = models.ForeignKey(User, on_delete = models.CASCADE)

#to make the field readable in Admin site
    def __str__(self):
       return self.title

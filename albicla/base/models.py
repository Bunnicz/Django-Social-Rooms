from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # One to many relationship
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) # One to many relationship
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants =
    updated = models.DateTimeField(auto_now=True)  # updates timestamp everytime
    created = models.DateTimeField(auto_now_add=True)  # Initial timestamp

    class Meta:
        # "-" inverts order
        ordering = ['-updated', '-created']
    
    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # One to many relationship: User can have many messages but message have one user
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  # One to many relationship
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)  # updates timestamp everytime
    created = models.DateTimeField(auto_now_add=True)  # Initial timestamp

    def __str__(self):
        return self.body[0:50]

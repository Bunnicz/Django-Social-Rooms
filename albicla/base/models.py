from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    # One to many relationship
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # One to many relationship
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # Many to many relationship
    participants = models.ManyToManyField(User, related_name="participants", blank=True)
    updated = models.DateTimeField(auto_now=True)  # updates timestamp everytime
    created = models.DateTimeField(auto_now_add=True)  # Initial timestamp

    class Meta:
        # Order of getting data from object "-" inverts order
        ordering = ["-updated", "-created"]

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

    class Meta:
        # Order of getting data from object "-" inverts order
        ordering = ["-updated", "-created"]

    def __str__(self):
        return self.body[0:50]

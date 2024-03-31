from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Dentist(models.Model):
    user = models.ForeignKey(
        User, related_name="created_dentist", on_delete=models.CASCADE
    )
    # name = models.CharField(max_length=50, unique=True)
    age = models.PositiveIntegerField()
    # user_name = models.CharField(max_length=100, unique=True)
    # pass_word = models.CharField(max_length=250)

    # Specify unique related_name attributes for groups and user_permissions
    # groups = models.ManyToManyField(
    #     "auth.Group",
    #     related_name="dentist_groups",
    #     blank=True,
    #     verbose_name="groups",
    #     help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
    # )
    # user_permissions = models.ManyToManyField(
    #     "auth.Permission",
    #     related_name="dentist_user_permissions",
    #     blank=True,
    #     verbose_name="user permissions",
    #     help_text="Specific permissions for this user.",
    # )

    def __str__(self) -> str:
        return self.user.username  # Assuming username is a field of the User model


class Message(models.Model):
    message = models.TextField(max_length=4000)
    send_to = models.ForeignKey(
        Dentist, related_name="received_message", on_delete=models.CASCADE
    )
    created_by = models.ForeignKey(
        User, related_name="sent_messages", on_delete=models.CASCADE
    )
    created_dt = models.DateTimeField(auto_now_add=True)


# class Account(models.Model):
#     username = models.CharField()
#     password = models.CharField()

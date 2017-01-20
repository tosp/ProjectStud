from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    home_directory = models.OneToOneField('spaced_repetition.Folder')

import datetime
from django.db import models

from user_profiles.models import Student


class Folder(models.Model):
    owner = models.ForeignKey(Student)
    parent_directory = models.ForeignKey('self')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Deck(models.Model):
    owner = models.ForeignKey(Student)
    parent_directory = models.ForeignKey(Folder)
    name = models.DateTimeField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Card(models.Model):
    owner = models.ForeignKey(Student)
    deck = models.ForeignKey(Deck)
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=750)
    box = models.IntegerField(default=1)
    last_studied = models.DateTimeField(default=datetime.datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

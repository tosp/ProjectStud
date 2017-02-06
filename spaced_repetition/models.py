import datetime
from django.db import models


class Folder(models.Model):
    owner = models.ForeignKey('user_profiles.Student', null=True, default=None)
    parent_directory = models.ForeignKey('self', null=True, default=None)
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)


class Deck(models.Model):
    owner = models.ForeignKey('user_profiles.Student')
    parent_directory = models.ForeignKey(Folder)
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)


class Card(models.Model):
    owner = models.ForeignKey('user_profiles.Student')
    deck = models.ForeignKey(Deck)
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=750)
    box = models.IntegerField(default=1)
    last_studied = models.DateTimeField(default=datetime.datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.question)

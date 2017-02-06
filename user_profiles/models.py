from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from spaced_repetition.models import Folder


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    home_directory = models.OneToOneField(Folder)

    def __str__(self):
        return '{}'.format(self.user)


@receiver(post_save, sender=User)
def create_student_profile_for_new_user(sender, created, instance, **kwargs):
    if created:
        # Create his future home directory
        new_home_directory = Folder()
        new_home_directory.save()

        # Create the new student object
        student = Student(
                          user=instance,
                          home_directory=new_home_directory
                         )
        student.save()

        # Assign the new student as the owner of the new directory
        new_home_directory.owner = student
        new_home_directory.save()

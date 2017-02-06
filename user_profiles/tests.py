from django.contrib.auth.models import User
from django.test import TestCase

from .models import Student
from spaced_repetition.models import Folder


class TestStudentModel(TestCase):

    def setUp(self):
        test_user = User(username="tiesto", password="tiesto666")
        test_user.save()

    def test_student_profile_creation(self):
        test_user = User.objects.get(username="tiesto")
        self.assertIsInstance(test_user.student, Student)

    def test_student_home_directory_creation(self):
        test_user = User.objects.get(username="tiesto")
        test_student = test_user.student
        self.assertIsInstance(test_student.home_directory, Folder)

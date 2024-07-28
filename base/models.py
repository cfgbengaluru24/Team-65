from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    preferred_subjects = models.ManyToManyField(Subject)
    email = models.EmailField(default='charlie.davis@example.com')
    def __str__(self):
        return self.user.username


class Student(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    email = models.EmailField(default=None)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    std = models.IntegerField()
    subjects = models.ManyToManyField(Subject)


class Preference(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    week_start_date = models.DateField()
    day_of_week = models.IntegerField()
    rsvp = models.BooleanField(default=False)  # 0 for Monday, 1 for Tuesday, etc

    def __str__(self):
        return f"{self.student.user.username} - {self.volunteer.user.username} - {self.subject.name}"


class Feedback(models.Model):
    preference = models.OneToOneField(Preference, on_delete=models.SET_NULL, null=True)
    question1 = models.TextField()
    question2 = models.TextField()
    question3 = models.TextField()
    question4 = models.TextField()
    question5 = models.TextField()
    volunteer_attended = models.BooleanField()
    by = models.CharField(max_length=100)

    def __str__(self):
        return f"Feedback for {self.preference}"
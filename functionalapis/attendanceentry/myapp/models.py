from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    attendance_percentage = models.FloatField(default=100)
    is_present = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class DailyReport(models.Model):
    date = models.DateField(auto_now_add=True)
    topic_taught = models.TextField()

    def __str__(self):
        return str(self.date)

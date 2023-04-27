from django.db import models


class Doctor(models.Model):
    fullname = models.CharField(max_length=30)
    experience = models.IntegerField()

    def __str__(self):
        return self.fullname


class Patient(models.Model):
    fullname = models.CharField(max_length=30)
    purpose = models.CharField(max_length=30)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='patients')

    def __str__(self):
        return self.fullname

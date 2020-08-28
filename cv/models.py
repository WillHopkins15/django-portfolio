from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import ArrayField

class Cv(models.Model):
    name = models.CharField(max_length=30)
    curr_employment = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    links = ArrayField(models.CharField(max_length=30))
    skills = ArrayField(models.CharField(max_length=30))
    hobbies = ArrayField(models.CharField(max_length=30))
    profile = models.CharField(max_length=2000)
    employment_hist = ArrayField(models.CharField(max_length=100))
    education = ArrayField(models.CharField(max_length=100))
    references = ArrayField(models.CharField(max_length=100))

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
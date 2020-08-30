from django.conf import settings
from django.db import models
from django_mysql.models import JSONField

class Cv(models.Model):
    name = models.CharField(max_length=30)
    curr_employment = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    links = JSONField()
    skills = JSONField()
    hobbies = JSONField()
    profile = models.CharField(max_length=2000)
    employment_hist = JSONField()
    education = JSONField()
    references = JSONField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
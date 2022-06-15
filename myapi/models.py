# models.py
from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    department = models.CharField(max_length=60)

    def __str__(self):
        return self.name

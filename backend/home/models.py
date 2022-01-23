from django.conf import settings
from django.db import models


class Teacher(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
    email = models.EmailField(
        max_length=254,
    )


class Student(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
    email = models.EmailField(
        max_length=254,
    )
    phone = models.DecimalField(
        max_digits=30,
        decimal_places=10,
    )


class Login(models.Model):
    "Generated Model"
    email = models.EmailField(
        max_length=254,
    )
    password = models.CharField(
        max_length=256,
    )


class Signup(models.Model):
    "Generated Model"
    email = models.EmailField(
        max_length=254,
    )
    password = models.CharField(
        max_length=256,
    )

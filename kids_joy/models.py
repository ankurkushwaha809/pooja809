# from tkinter import CASCADE
from unicodedata import name
from urllib import request
from django.db import models
# Create your models here.

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


# class Subctaegory(models.Model):
    
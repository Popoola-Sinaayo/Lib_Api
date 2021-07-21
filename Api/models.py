from django.db import models
import datetime
# Create your models here.


class Book(models.Model):
    Title = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    Date_Added = models.DateField(default=datetime.datetime.now)
    Category = models.CharField(max_length=100)

    def __str__ (self):
        return f"{self.Title}"
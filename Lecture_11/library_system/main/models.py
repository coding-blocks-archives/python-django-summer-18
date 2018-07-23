from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey('Publisher', on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Author(models.Model):
    STATUS = (
        ('M', 'Married'),
        ('U', 'Unmarried'),
        ('C', 'Complicated'),
    )

    name = models.CharField(max_length = 100)
    marital_status = models.CharField(max_length = 5, choices = STATUS)

    def __str__(self):
        return self.name
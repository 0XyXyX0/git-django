from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255, unique=True)
    surname = models.CharField(max_length=255)
    biography = models.TextField()
    age = models.PositiveIntegerField()
    birthdate = models.DateField()

    def __str__(self):
        return f"{self.name}"



class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=10)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

    

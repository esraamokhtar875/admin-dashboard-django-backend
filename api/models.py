from django.db import models


# Food Model
class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# User Model
class UserProfile(models.Model):
    PROFILE_TYPES = (
        ('customer', 'Customer'),
        ('admin', 'Admin'),
    )
    type = models.CharField(max_length=10, choices=PROFILE_TYPES)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

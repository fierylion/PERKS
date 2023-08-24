from django.db import models

class Vendor(models.Model):
    businessName = models.CharField(max_length=200, verbose_name="Business name", unique=True)
    locationAddress = models.CharField(max_length=200, verbose_name="Location address")
    emailAddress = models.CharField(max_length=100, verbose_name="Email")
    phoneNumber = models.CharField(max_length=30, unique=True, verbose_name="Phone number")
    password = models.CharField(max_length=50, verbose_name="Password")

    def __str__(self) -> str:
        return self.businessName + " - " + self.locationAddress

class User(models.Model):
    userName = models.CharField(max_length=200, verbose_name="Name")
    phoneNumber = models.CharField(max_length=30, unique=True, verbose_name="Phone number")

    def __str__(self) -> str:
        return self.userName + " - " + self.phoneNumber

class Transaction(models.Model):
    phoneNumber = User.phoneNumber
    amount = models.CharField(max_length=500, verbose_name="Amount")

    def __str__(self) -> str:
        return self.phoneNumber + " - " + self.amount
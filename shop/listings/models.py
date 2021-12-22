from datetime import datetime
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from checkout.models import CustomerInformation


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Listing(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to="static/listings/%y/%m/%d/", blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(null=True)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now())
    active = models.BooleanField(default=False)
    deviceId = models.CharField(max_length=250, null=True, blank=True)
    finished = models.BooleanField(default=False)
    delivery_address = models.ForeignKey(CustomerInformation, blank=True, null=True, on_delete=models.SET_NULL)

    def get_total(self):
        return sum(x.get_sum() for x in self.orderlisting_set.all())

    def __str__(self):
        if self.user:
            return self.user.username
        return self.deviceId


class OrderListing(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)

    def get_sum(self):
        return self.listing.price * self.quantity

    def __str__(self):
        return self.listing.name

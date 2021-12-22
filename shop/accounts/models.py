from django.db import models
from django.contrib.auth.models import User
from listings.models import Listing


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listings = models.ManyToManyField(Listing)


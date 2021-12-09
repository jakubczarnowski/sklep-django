from django.db import models
from django.db.models.fields.related import ForeignKey
import listings
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)


class CartItem(models.Model):
    object_id = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(verbose_name=('quantity'))
    cart = models.ForeignKey(Cart, verbose_name=("Cart"), on_delete=models.CASCADE)

    def get_product(self):
        return listings.models.Listing.objects.get(pk=self.object_id)

from django.db import models


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

    def __str__(self) -> str:
        return self.name

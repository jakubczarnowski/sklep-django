from django.db import models
# Create your models here.
class Listing(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to="static/listings/%y/%m/%d/", blank=True)\
    
    def __str__(self) -> str:
        return self.name
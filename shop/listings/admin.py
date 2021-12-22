from django.contrib import admin
from . import models
from django.template.defaultfilters import slugify


class ListingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(models.Listing, ListingAdmin)
admin.site.register(models.Category)
admin.site.register(models.OrderListing)
admin.site.register(models.Order)

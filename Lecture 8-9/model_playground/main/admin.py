from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Person)
admin.site.register(models.Student)
admin.site.register(models.Subject)
admin.site.register(models.Pizza)
admin.site.register(models.Topping)
admin.site.register(models.Book)
admin.site.register(models.Publisher)
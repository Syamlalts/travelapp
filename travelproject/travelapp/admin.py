from django.contrib import admin
from . models import place

from . models import peoples

# Register your models here.
admin .site.register(place)
admin .site.register(peoples)
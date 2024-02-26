from django.contrib import admin

from .models import Location
from .models import Sensor


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')


class SensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')  # Display id, name, and location
    list_filter = ('location',)  # Filter sensors by location
    ordering = ('name', 'location')  # Sort sensors by name or location


admin.site.register(Sensor, SensorAdmin)

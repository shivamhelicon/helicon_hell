from django.db import models
from django.contrib import admin
import uuid
from django.utils.text import slugify


class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
   

class Sensor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ['name', 'location']

    def __str__(self):
        return f'{self.name} ({self.location.name})'

from django.db import models


# Create your models here - "Collection of things" -> name of the thing, description and slug
class Thing(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)

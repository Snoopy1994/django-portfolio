# projects/models.py

from django.db import models
from taggit.managers import TaggableManager


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(max_length=200, blank=True)
    tags = TaggableManager()
    image = models.FileField(upload_to="project_images/", blank=True)

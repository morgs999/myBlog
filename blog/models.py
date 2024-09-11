# blog/models.py

from django.db import models

class Post(models.Model):
    "blog post"
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)

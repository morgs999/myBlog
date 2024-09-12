# blog/models.py

from django.db import models
from django.conf import settings

class Topic(models.Model):
    """blog post topic"""
    name = models.CharField(
        max_length=50,
        unique=True
    )
    slug=models.SlugField(unique=True)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ['name']


class Post(models.Model):
    """blog post"""
    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    ]

    # fields
    title = models.CharField(max_length=255)

    slug = models.SlugField(
        null=False,
        help_text='The date & time this article was published',
        unique_for_date='published',
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='blog_posts',
        null=False
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=DRAFT,
        help_text='Set to "published" to make this post publicly visible',
    )

    content = models.TextField()

    published = models.DateTimeField(
        null=True,
        blank=True,
        help_text='The date & time this article was published',
    )

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now = True)

    topics = models.ManyToManyField(
        Topic,
        related_name='blog_posts'
    )


    class Meta:
        ordering = ['-created',]

    def __str__(self):
        return str(self.title)


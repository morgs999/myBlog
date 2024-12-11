# blog/models.py
"""blog models"""

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model


class PostQuerySet(models.QuerySet):
    """custom queryset for Post model"""
    def published(self):
        """return only published posts"""
        return self.filter(status=self.model.PUBLISHED)
    def draft(self):
        """return only draft posts"""
        return self.filter(status=self.model.DRAFT)
    def get_authors(self):
        """return all authors who have authored a post"""
        user = get_user_model()
        return user.objects.filter(blog_posts__in=self).distinct()    


class Topic(models.Model):
    """blog post topic"""
    name = models.CharField(
        max_length=50,
        unique=True,
        null=False
    )
    slug=models.SlugField(
        unique=True,
        null=False
    )

    objects = models.Manager()

    def get_absolute_url(self):
        """provide url"""
        kwargs={'slug':self.slug}
        return reverse('topic-detail', kwargs=kwargs)

    def __str__(self):
        return str(self.name)

    class Meta:
        """meta information for Topic model"""
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
    title = models.CharField(
        max_length=255,
        null=False
    )

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
        null=False,
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

    # methods
    objects = PostQuerySet.as_manager()

    def publish(self):
        """publish this post"""
        self.status = self.PUBLISHED
        self.published = timezone.now()

    def get_absolute_url(self):
        """provide url"""
        if self.published:
            kwargs={
                'year':self.published.year,
                'month':self.published.month,
                'day':self.published.day,
                'slug':self.slug
            }
        else:
            kwargs = {'pk':self.pk}

        return reverse('post-detail', kwargs=kwargs)

    # meta
    class Meta:
        """meta information for Post model"""
        ordering = ['created',]

    def __str__(self):
        return str(self.title)[:50]


class Comment(models.Model):
    """blog post comment"""
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        null=False
    )

    name = models.CharField(
        max_length=50,
        null=False
    )

    email = models.EmailField(
        max_length=100,
        null=False
    )

    text = models.TextField(
        max_length=2000,
        null=False
    )

    approved = models.BooleanField(
        default=True
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    objects = models.Manager()

    class Meta:
        """meta information for Comment model"""
        ordering = ['-created']

    def __str__(self):
        return str(self.text)[:50]

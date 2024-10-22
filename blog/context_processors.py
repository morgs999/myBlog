# blog/context_processors.py

from django.db.models import Count
from . import models

def base_context(request):
    """sidebar refresh data"""
    authors = models.Post.objects.published() \
            .get_authors() \
            .order_by('first_name')

    topics = models.Topic.objects.annotate(
            post_count=Count('blog_posts')) \
            .order_by('-post_count')

    return {'authors':authors,'topics':topics}

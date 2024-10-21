# blog/views.py
"""views for blog app"""

from django.shortcuts import render
from django.db.models import Count
from . import models

def home(request):
    """
    The Blog homepage
    """

    latest_posts = models.Post.objects.filter(status='published').order_by('-created')

    authors = models.Post.objects.published().get_authors().order_by('first_name')

    topics = models.Topic.objects.annotate(post_count=Count('blog_posts')).order_by('-post_count')

    context = {
        'authors': authors,
        'latest_posts': latest_posts,
        'topics': topics,
    }

    return render(request, 'blog/home.html', context)

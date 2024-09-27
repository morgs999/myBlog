# blog/views.py
"""views for blog app"""

from django.shortcuts import render
from . import models

# Create your views here.

def home(request):
    """
    The Blog homepage
    """

    latest_posts = models.Post.objects.filter(status='published').order_by('-created')
    authors = models.Post.objects.published().get_authors().order_by('first_name')
    context = {
        'authors': authors,
        'latest_posts': latest_posts
    }
    return render(request, 'blog/home.html', context)

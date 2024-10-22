# blog/views.py
"""views for blog app"""

from django.shortcuts import render
# from django.db.models import Count
from django.views.generic.base import TemplateView
from . import models

class HomeView(TemplateView):
    """
    The Blog homepage
    """

    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_posts = models.Post.objects.filter(status='published').order_by('-created')

        context.update({'latest_posts':latest_posts})

        return context

class AboutView(TemplateView):
    """
    About Page
    """
    template_name = 'blog/about.html'

def terms_and_conditions(request):
    """termsandconditions"""
    return render(request, 'blog/terms_and_conditions.html')

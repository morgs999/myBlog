# blog/views.py
"""views for blog app"""

from django.shortcuts import render
# from django.db.models import Count
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
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

class PostListView(ListView):
    """
    All the (published) Posts page
    """
    model = models.Post
    context_object_name = 'posts'
    queryset = models.Post.objects \
        .published() \
        .order_by('-published')
    
class PostDetailView(DetailView):
    """
    Single Post Page
    """
    model = models.Post

    def get_queryset(self):
        # Get the base queryset
        queryset = super().get_queryset().published()

        # If a PK lookup, use default queryset
        if 'pk' in self.kwargs:
            return queryset
        
        # else filter on published date
        return queryset.filter(
            published__year=self.kwargs['year'],
            published__month=self.kwargs['month'],
            published__day=self.kwargs['day'],
        )


def terms_and_conditions(request):
    """termsandconditions"""
    return render(request, 'blog/terms_and_conditions.html')

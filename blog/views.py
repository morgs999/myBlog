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

class TopicListView(ListView):
    """
    All the Topics page
    """
    model = models.Topic
    context_object_name = 'topics'

class TopicDetailView(DetailView):
    """
    Single Topic Page
    """
    model = models.Topic
    context_object_name = 'topic'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['postsCount'] = self.object.blog_posts.published().count()
        context['posts'] = models.Post.objects \
            .published() \
            .filter(topics=self.object) \
            .order_by('-published')
        return context

    def get_object(self, queryset=None):
        return models.Topic.objects.get(slug=self.kwargs['slug'])

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        return context

def terms_and_conditions(request):
    """termsandconditions"""
    return render(request, 'blog/terms_and_conditions.html')

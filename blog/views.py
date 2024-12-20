# blog/views.py
"""views for blog app"""

from django.shortcuts import render
# from django.db.models import Count
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from . import models, forms

class HomeView(TemplateView):
    """
    The Blog homepage
    """

    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_posts = models.Post.objects.filter(status='published').order_by('-published')

        context.update({'latest_posts':latest_posts})

        return context

class AboutView(TemplateView):
    """
    About Page
    """
    template_name = 'blog/about.html'

class ContactView(TemplateView):
    """
    Contact Page
    """
    template_name = 'blog/contact.html'

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
        context['topics'] = self.object.topics.all
        context['comments'] = self.object.comments.all().order_by('created')
        return context

class FormViewExample(FormView):
    """example form """
    template_name = 'blog/form_example.html'
    form_class = forms.ExampleSignupForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Create a "success" message
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Thank you for signing up!'
        )
        # Continue with default behaviour
        return super().form_valid(form)

class ContactFormView(CreateView):
    """contact form"""
    model = models.Contact
    success_url = reverse_lazy('home')
    fields = [
        'first_name',
        'last_name',
        'email',
        'message',
    ]

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Thanks! Your message has been sEnT...'
        )

        return super().form_valid(form)

class PhotoContestView(CreateView):
    """photo contest form"""
    model = models.PhotoContest
    success_url = reverse_lazy('photo-contest')
    fields = [
        'name',
        'email',
        'photo',
    ]

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Thanks for entering the photo cOnTeSt!'
        )

        return super().form_valid(form)


def terms_and_conditions(request):
    """termsandconditions"""
    return render(request, 'blog/terms_and_conditions.html')

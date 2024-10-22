"""
URL configuration for myBlog project.
"""

from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('/terms', views.terms_and_conditions, name='terms-and-conditions'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:year>/<int:month>/<int:day>/<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>', views.PostDetailView.as_view(), name='post-detail')
]

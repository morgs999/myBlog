"""
URL configuration for myBlog project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.HomeView.as_view(), name='home'),

    path('about/', views.AboutView.as_view(), name='about'),

    # path('contact/', views.ContactView.as_view(), name='contact'),
    path('contact', views.ContactFormView.as_view(), name='contact'),

    path('terms/', views.terms_and_conditions, name='terms-and-conditions'),

    path('posts/', views.PostListView.as_view(), name='post-list'),

    path('posts/<int:year>/<int:month>/<int:day>/<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),

    path('posts/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),

    path('topics/', views.TopicListView.as_view(), name='topic-list'),

    path('topics/<slug:slug>/', views.TopicDetailView.as_view(), name='topic-detail'),

    path('formview-example/', views.FormViewExample.as_view(), name='formview-example'),

    path('photo-contest/', views.PhotoContestView.as_view(), name='photo-contest'),

    path('ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

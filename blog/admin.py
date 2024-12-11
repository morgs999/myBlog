# blog/admin.py

from django.contrib import admin
from . import models

class CommentInline(admin.TabularInline):
    model = models.Comment
    readonly_fields = ('name', 'email', 'text')
    extra = 0

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'updated',)
    search_fields = ('title', 'author__username','author__first_name', 'author__last_name')
    list_filter = ('author', 'status', 'topics',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CommentInline]

@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'created', 'updated', 'approved')
    search_fields = ('post__title', 'name')
    list_filter = ('approved',)

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'last_name',
        'first_name',
        'submitted'
    )
    readonly_fields = (
        'email',
        'last_name',
        'first_name',
        'message',
        'submitted'
    )

@admin.register(models.PhotoContest)
class PhotoContestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'photo', 'submitted')
    readonly_fields = ('name', 'email', 'photo', 'submitted')
    search_fields = ('name', 'email')
    list_filter = ('submitted', 'name', 'email')

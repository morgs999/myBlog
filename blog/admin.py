# blog/admin.py

from django.contrib import admin
from . import models

class CommentInline(admin.TabularInline):
    model = models.Comment
    readonly_fields = ('name', 'email', 'text')
    extra = 0

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated',)
    search_fields = ('title', 'author__username','author__first_name', 'author__last_name')
    list_filter = ('status', 'topics',)
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

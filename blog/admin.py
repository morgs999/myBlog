# blog/admin.py

from django.contrib import admin
from . import models

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'updated',)
    search_fields = ('title', 'author__username',)
    list_filter = ('status', 'created', 'updated', 'author', 'topics',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(models.Post, PostAdmin)

@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

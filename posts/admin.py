from django.contrib import admin
from .models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated', 'timestamp']
    list_display_links = ['title']
    list_filter = ['updated', 'timestamp']
    search_fields = ['title', 'content']
    # list_editable = ['title']
    ordering = ['title']
    # actions = ['make_published']

    # def make_published(self, request, queryset):
    #     queryset.update(blog='p')
    #
    # make_published.short_description = "Mark selected stories as published"


admin.site.register(Post, PostModelAdmin)
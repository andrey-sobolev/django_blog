from django.contrib import admin

from blog.models import Post, Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'date', 'user', 'post',
    ]
    list_display_links = ['id', 'date']
    list_filter = ['date']
    
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'date', 'author', 'title',
    ]
    list_display_links = ['id', 'date']
    list_filter = ['date']

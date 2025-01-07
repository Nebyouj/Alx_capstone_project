from django.contrib import admin
from .models import User, Post, Follow, Comment, Like

# User model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'bio', 'profile_picture', 'date_joined')
    search_fields = ('username', 'email')
    list_filter = ('date_joined',)

# Post model
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('created_at', 'author')
    ordering = ('-created_at',)

# Follow model
@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('follower', 'following')
    search_fields = ('follower__username', 'following__username')

# Comment model
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at')
    search_fields = ('author__username', 'content', 'post__title')
    list_filter = ('created_at', 'post')
    ordering = ('-created_at',)

# Like model
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'like_type')
    search_fields = ('user__username', 'post__title')
    list_filter = ('like_type',)


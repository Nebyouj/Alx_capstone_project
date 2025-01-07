from django.urls import path
from .views import (
    UserListCreateView, UserDetailView, PostListCreateView, PostDetailView,
    FollowView, UnfollowView, CommentListCreateView, CommentDetailView,
    LikeView, UnlikeView, FeedView
)

urlpatterns = [
    # User Endpoints
    path('users/', UserListCreateView.as_view(), name='user-list-create'),  # Create a new user
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),  # Retrieve, Update or Delete user details

    # Post Endpoints
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),  # Create a new post
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # Retrieve, Update or Delete post

    # Follow System Endpoints
    path('users/<int:user_id>/follow/', FollowView.as_view(), name='follow'),  # Follow a user
    path('users/<int:user_id>/unfollow/', UnfollowView.as_view(), name='unfollow'),  # Unfollow a user

    # Feed Endpoint
    path('feed/', FeedView.as_view(), name='feed'),  # Retrieve the feed of posts from followed users

    # Comment Endpoints
    path('posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),  # Create a new comment on a post
    path('posts/<int:post_id>/comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),  # Retrieve, update, or delete a comment

    # Like/Dislike Endpoints
    path('posts/<int:post_id>/like/', LikeView.as_view(), name='like'),  # Like a post
    path('posts/<int:post_id>/dislike/', LikeView.as_view(), name='dislike'),  # Dislike a post
    path('posts/<int:post_id>/like/remove/', UnlikeView.as_view(), name='remove-like'),  # Remove like from a post
    path('posts/<int:post_id>/dislike/remove/', UnlikeView.as_view(), name='remove-dislike'),  # Remove dislike from a post
]



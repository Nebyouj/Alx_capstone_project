from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from .models import Post, Follow, Comment, Like
from .serializers import PostSerializer, FollowSerializer, CommentSerializer, LikeSerializer, UserSerializer

User = get_user_model()

# User Management Views
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny] 
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['is_active', 'date_joined']  # Example filters for User model
    ordering_fields = ['date_joined', 'username']
    search_fields = ['username', 'email']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['include_tokens'] = True  # Add tokens to context for this view
        return context


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny] 
    def get_object(self):
        user = self.request.user
        return user

# Post Management Views
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.select_related('author').prefetch_related('comments')
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['author', 'category', 'tags']  # Add any fields relevant to the Post model
    ordering_fields = ['created_at', 'likes_count']
    search_fields = ['title', 'content']
    # permission_classes = [IsAuthenticated]  # Ensure the user is authenticated
    permission_classes = [AllowAny] 
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny] 

# Follow System Views
class FollowView(generics.CreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny] 

class UnfollowView(generics.DestroyAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    # permission_classes = [IsAuthenticated]

    def get_object(self):
        follower = self.request.user
        following_user = User.objects.get(pk=self.kwargs['user_id'])
        return Follow.objects.get(follower=follower, following=following_user)

# Comment Management Views
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['post', 'author']
    ordering_fields = ['created_at']
    search_fields = ['content']
    permission_classes = [AllowAny] 

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny] 
# Like/Dislike Management Views
class LikeView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [AllowAny] 

class UnlikeView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [AllowAny] 
    def get_object(self):
        post = Post.objects.get(pk=self.kwargs['post_id'])
        user = self.request.user
        return Like.objects.get(post=post, user=user)

# Personalized Feed View
class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticated]  # Ensure only authenticated users access the feed
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['author', 'category', 'tags']  # Same filters as PostListCreateView
    ordering_fields = ['created_at', 'likes_count']
    search_fields = ['title', 'content']
    permission_classes = [AllowAny] 
    def get_queryset(self):
        user = self.request.user
        following = user.following.values_list('following', flat=True)
        return Post.objects.filter(author__in=following).order_by('-created_at')

from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Post, Follow, Comment, Like

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    tokens = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'tokens']

    def get_tokens(self, user):
        # Ensure tokens are only added in relevant views
        if self.context.get('include_tokens', False):  # Check context for token inclusion
            refresh = RefreshToken.for_user(user)
            return {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        return {}

class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'created_at', 'updated_at']

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['id', 'follower', 'following']

    def validate(self, data):
        if data['follower'] == data['following']:
            raise serializers.ValidationError("You cannot follow yourself.")
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'post', 'user', 'like_type']

    def validate(self, data):
        if Like.objects.filter(post=data['post'], user=data['user']).exists():
            raise serializers.ValidationError("You have already liked this post.")
        return data


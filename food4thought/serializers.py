from rest_framework import serializers
from .models import Post, Comment, BecomeMember


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'slug', 'title', 'subtitle', 'post_content', 'likes', 'audio_content', 'date_posted']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'name', 'comment', 'date_commented']


class BecomeMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BecomeMember
        fields = ['id', 'name', 'email', 'phone', 'photo', 'date_joined']

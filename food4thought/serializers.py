from rest_framework import serializers
from .models import Post, Comment, BecomeMember, Testimony



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'post_content', 'audio_content', 'date_posted']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'comment',
                  'date_of_comment']


class BecomeMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BecomeMember
        fields = ['id', 'name', 'email','date_joined']


class TestimonySerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimony
        fields = ['id', 'name', 'testimony',
                  'date_of_testimony']



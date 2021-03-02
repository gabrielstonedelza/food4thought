from rest_framework import serializers
from .models import Post, Comment, BecomeMember



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'post_content', 'likes', 'audio_content', 'date_posted']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'comment',
                  'date_of_comment', 'time_of_comment']


class BecomeMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BecomeMember
        fields = ['id', 'name', 'email','date_joined']




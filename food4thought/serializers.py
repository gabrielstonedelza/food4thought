from rest_framework import serializers
from .models import Thought, Comment, BecomeMember, Testimony


class ThoughtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thought
        fields = ['id', 'title', 'author', 'bible_quotations',
                  'audio_content', 'date_posted']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'comment',
                  'date_of_comment']


class BecomeMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BecomeMember
        fields = ['id', 'name', 'email', 'date_joined']


class TestimonySerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimony
        fields = ['id', 'name', 'testimony',
                  'date_of_testimony']

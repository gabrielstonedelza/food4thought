from rest_framework import serializers
from .models import Thought, FeedBack, BecomeMember, Testimony, Question, Answers, Message


class ThoughtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thought
        fields = ['id', 'title', 'author', 'bible_quotations',
                  'audio_content', 'date_posted']


class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = ['id', 'name', 'message',
                  'date_of_feedback']


class BecomeMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BecomeMember
        fields = ['id', 'name', 'date_joined']


class TestimonySerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimony
        fields = ['id', 'name', 'testimony',
                  'date_of_testimony']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'name', 'question', 'answered', 'date_posted']


class AnswersSerializer(serializers.ModelSerializer):
    question_question = serializers.ReadOnlyField(source='question.question')
    question_owner = serializers.ReadOnlyField(source='question.name')

    class Meta:
        model = Answers
        fields = "__all__"

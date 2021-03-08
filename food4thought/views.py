from .models import Thought, FeedBack, BecomeMember, Testimony
from .serializers import ThoughtSerializer, FeedBackSerializer, BecomeMemberSerializer, TestimonySerializer

from rest_framework import viewsets


class ThoughtLists(viewsets.ModelViewSet):
    queryset = Thought.objects.all().order_by('-date_posted')
    serializer_class = ThoughtSerializer


class MembersLists(viewsets.ModelViewSet):
    queryset = BecomeMember.objects.all().order_by('-date_joined')
    serializer_class = BecomeMemberSerializer


class Just2Day(viewsets.ModelViewSet):
    queryset = Thought.objects.all()[:1]
    serializer_class = ThoughtSerializer


class FeedPost(viewsets.ModelViewSet):
    queryset = FeedBack.objects.all().order_by('-date_of_feedback')
    serializer_class = FeedBackSerializer


class TestimonyView(viewsets.ModelViewSet):
    queryset = Testimony.objects.all().order_by('-date_of_testimony')
    serializer_class = TestimonySerializer

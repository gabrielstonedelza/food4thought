from .models import Post, Comment, BecomeMember
from .serializers import PostSerializer, CommentSerializer, BecomeMemberSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status,viewsets


class ThoughtListView(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-date_posted')
    serializer_class = PostSerializer

class ThoughtTodayView(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-date_posted')[:1]
    serializer_class = PostSerializer


class MembersView(viewsets.ModelViewSet):
    queryset = BecomeMember.objects.all().order_by('-date_joined')
    serializer_class = BecomeMemberSerializer

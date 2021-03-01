from .models import Post, Comment, BecomeMember
from .serializers import PostSerializer, CommentSerializer, BecomeMemberSerializer

from rest_framework import viewsets

class ThoughtLists(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-date_posted')
    serializer_class = PostSerializer

class MembersLists(viewsets.ModelViewSet):
    queryset = BecomeMember.objects.all().order_by('-date_joined')
    serializer_class = BecomeMemberSerializer

class Just2Day(viewsets.ModelViewSet):
    queryset = Post.objects.all()[:1]
    serializer_class = PostSerializer

class CommentOnPost(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-date_of_comment')
    serializer_class = CommentSerializer
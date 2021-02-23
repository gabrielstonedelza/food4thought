from .models import Post, Comment, BecomeMember
from .serializers import PostSerializer, CommentSerializer, BecomeMemberSerializer
from django.shortcuts import get_object_or_404

from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET'])
def post_today(request):
    post2day = Post.objects.all().order_by('-date_posted')[:1]
    serializer = PostSerializer(post2day, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all().order_by('-date_posted')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@csrf_exempt
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def post_delete(request, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
    except Post.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def all_members(request):
    members = BecomeMember.objects.all().order_by('-date_joined')
    serializer = BecomeMemberSerializer(members, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def become_member(request):
    serializer = BecomeMemberSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def like_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.likes += 1
    post.save()
    
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

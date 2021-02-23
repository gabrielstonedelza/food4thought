from django.db import models
from django.shortcuts import reverse
from PIL import Image
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=200, blank=True)
    post_content = models.TextField(blank=True, help_text="You can leave this field blank if you don't need to add text")
    likes = models.IntegerField(default=0, blank=True)
    views = models.IntegerField(default=0, blank=True)
    audio_content = models.FileField(upload_to="post_audio_files", blank=True,help_text="select audio content")
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=({self.pk}))

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=True, default="Anonymous")
    comment = models.TextField()
    date_of_comment = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} commented on the post '{self.post.title}'"


class BecomeMember(models.Model):
    name = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=250, unique=True)
    phone = models.CharField(max_length=100, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} just became a member of food4thought"


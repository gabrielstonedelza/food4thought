from django.db import models
from django.shortcuts import reverse
from PIL import Image
from django.utils.text import slugify
from django.utils import timezone


class Thought(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    bible_quotations = models.CharField(max_length=500, blank=True)
    audio_content = models.FileField(
        upload_to="post_audio_files", blank=True, help_text="select audio content")
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=({self.pk}))


class FeedBack(models.Model):
    name = models.CharField(max_length=150, blank=True, default="Anonymous")
    message = models.TextField()
    date_of_feedback = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BecomeMember(models.Model):
    name = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=250, unique=True)
    profession = models.CharField(max_length=100, blank=True,
                                  help_text="If can leave this field blank if you don't to your profession")
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} just became a member of food4thought"


class Testimony(models.Model):
    name = models.CharField(max_length=200, unique=True)
    testimony = models.TextField()
    date_of_testimony = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} just gave a testimony"


class Question(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, help_text="We will notify you when your question is answered")
    question = models.TextField()
    answered = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} asked a question"


class Answers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.question.name}'s question was answered"


class Message(models.Model):
    message = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
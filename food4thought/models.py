from django.db import models
from django.shortcuts import reverse
from PIL import Image
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=200,blank=True)
    post_content = models.TextField()
    likes = models.IntegerField(default=0,blank=True)
    views = models.IntegerField(default=0,blank=True)
    audio_content = models.FileField(upload_to="post_audio_files",blank=True)
    slug = models.SlugField(max_length=100, default='')
    date_posted = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            # 'pk': self.id,
            'slug': self.slug
        }
        return reverse('post_detail', kwargs=kwargs)
    
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=150,blank=True,default="Anonymous")
    comment = models.TextField()
    date_of_comment = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} commented on the post '{self.post.title}'"


class BecomeMember(models.Model):
    name = models.CharField(max_length=200,unique=True)
    email = models.EmailField(max_length=250,unique=True)
    phone = models.CharField(max_length=100,blank=True)
    photo = models.ImageField(upload_to='members_photo',blank=True,default='default_member.jpg')
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} just became a member of food4thought"

    # def save(self, *args, **kwargs):

    #     if self.photo:
    #         img = Image.open(self.photo.path)
    #         if img.height > 300 or img.width > 300:
    #             output_size = (40, 40)
    #             img.thumbnail(output_size)
    #             img.save(self.photo.path)
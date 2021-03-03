from django.contrib import admin
from .models import Post, Comment,BecomeMember,Testimony

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(BecomeMember)
admin.site.register(Testimony)
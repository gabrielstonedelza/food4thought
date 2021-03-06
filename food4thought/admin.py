from django.contrib import admin
from .models import Thought, Comment,BecomeMember,Testimony

admin.site.register(Thought)
admin.site.register(Comment)
admin.site.register(BecomeMember)
admin.site.register(Testimony)
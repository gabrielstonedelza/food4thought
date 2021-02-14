from django.urls import path
from . import views

urlpatterns = [
    path('api/post2day/', views.post_today, name='post_today'),
    path('api/post/', views.post_list, name='post_list'),
    path('api/post/<int:id>/', views.post_detail, name='detail'),
    path('api/post/new/', views.create_post, name='post_new'),
    path('api/post/<int:id>/delete/', views.post_delete, name='post_delete'),
    path('api/members/', views.all_members, name='f4t_members'),
    path('api/members/new/', views.become_member, name='become_member'),
    path('api/post/<int:id>/like/', views.like_post, name='like_post')
]

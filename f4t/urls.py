from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_home, name='post_home'),
    path('posts/', views.all_posts, name='allposts'),
    path("post/new/", views.create_post, name="create_post"),
    path('posts/<str:slug>/', views.post_detail, name='post_detail'),
    path('like_post/<str:slug>/', views.like_post, name='like_post'),
    path('members/', views.members, name='members'),
    path('member/new/', views.become_amember, name='new_member'),
    path('about/', views.about, name='about'),
    path('search/', views.search_queries, name='search'),
]

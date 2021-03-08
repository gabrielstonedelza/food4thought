from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_home, name='post_home'),
    path('posts/', views.all_posts, name='allposts'),
    path("post/new/", views.create_post, name="create_post"),
    path('members/', views.members, name='members'),
    path('member/new/', views.become_member, name='new_member'),
    path('testimonies/', views.testimonies, name='testimonies'),
    path('testimony/new/', views.create_testimony, name='new_testimony'),
    path('feedbacks/', views.feedbacks, name='feedbacks'),
    path('feedback/new/', views.create_feedback, name='new_feedback'),
    path('about/', views.about, name='about'),
    path('search/', views.search_queries, name='search'),
]

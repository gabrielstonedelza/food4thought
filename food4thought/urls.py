from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('thoughtlist', views.ThoughtLists)
router.register('members', views.MembersLists)
router.register('feedbacks', views.FeedPost)
router.register('testimonies', views.TestimonyView)
router.register('questions', views.QuestionsView)
router.register('answers', views.AnswersView)

urlpatterns = [
    path('api/', include(router.urls))
]

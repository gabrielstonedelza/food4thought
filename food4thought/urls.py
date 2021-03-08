from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('thoughtlist', views.ThoughtLists)
router.register('members', views.MembersLists)
router.register('comments', views.FeedPost)
router.register('testimonies', views.TestimonyView)

urlpatterns = [
    path('api/', include(router.urls))
]

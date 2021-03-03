from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('thoughtlist', views.ThoughtLists)
router.register('members', views.MembersLists)
router.register('comments', views.CommentOnPost)
router.register('testimonies', views.TestimonyView)
# router.register('just2day',views.Just2Day)

urlpatterns = [
    path('api/', include(router.urls))
]

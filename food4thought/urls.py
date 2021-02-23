from django.urls import path,include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('thoughts',views.ThoughtListView)
router.register('thought_today',views.ThoughtTodayView)
router.register('members',views.MembersView)

urlpatterns = [

    path('api/',include(router.urls))
]

from django.urls import path, include
from rest_framework import routers
from events import views


router = routers.DefaultRouter()


router.register(r'events', views.EventViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'attendance', views.AttendanceViewSet)


urlpatterns = router.urls

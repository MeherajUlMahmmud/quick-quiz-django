from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import FeedbackModelViewSet, FileModelViewSet

router = DefaultRouter()
router.register(r'feedback', FeedbackModelViewSet, basename='feedbacks')
router.register(r'file', FileModelViewSet, basename='files')

urlpatterns = [
    path('', include(router.urls)),
]

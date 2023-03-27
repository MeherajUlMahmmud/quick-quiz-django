from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import FeedbackModelViewSet

router = DefaultRouter()
router.register(r'feedback', FeedbackModelViewSet, basename='feedbacks')

urlpatterns = [
    path('', include(router.urls)),
]

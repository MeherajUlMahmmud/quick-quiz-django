from django.urls import path, include
from rest_framework.routers import DefaultRouter

from utility_control.views.feedback import FeedbackModelViewSet
from utility_control.views.issue import IssueModelViewSet

router = DefaultRouter()
router.register(r'feedback', FeedbackModelViewSet, basename='feedback')
router.register(r'issue', IssueModelViewSet, basename='issue')

urlpatterns = [
    path('', include(router.urls)),
]

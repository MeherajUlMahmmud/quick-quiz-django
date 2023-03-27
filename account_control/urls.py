from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .views.auth import RegisterAPIView, LoginAPIView, LogoutAPIView, ResetPasswordAPIView, ChangePasswordAPIView
from .views.student import StudentModelViewSet
from .views.teacher import TeacherModelViewSet
from .views.user import UserModelViewSet

router = DefaultRouter()
router.register(r'users', UserModelViewSet, basename='users')
router.register(r'students', StudentModelViewSet, basename='students')
router.register(r'teachers', TeacherModelViewSet, basename='teachers')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', RegisterAPIView.as_view(), name="register"),
    path('auth/login/', LoginAPIView.as_view(), name="login"),
    path('auth/logout/', LogoutAPIView.as_view(), name="logout"),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/change-password/', ChangePasswordAPIView.as_view(), name='change_password'),
    path('auth/reset-password/', ResetPasswordAPIView.as_view(), name='reset_password'),
]

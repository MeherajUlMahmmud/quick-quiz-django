from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from account_control.urls import router as account_router
from exam_control.urls import router as exam_router
from group_control.urls import router as group_router
from subscription_control.urls import router as subscription_router
from utility_control.urls import router as utility_router

router = routers.DefaultRouter()
router.registry.extend(account_router.registry)
router.registry.extend(exam_router.registry)
router.registry.extend(group_router.registry)
router.registry.extend(subscription_router.registry)
router.registry.extend(utility_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
    path('', include('account_control.urls'), name='account'),
    path('', include('group_control.urls'), name='group'),
    path('', include('subscription_control.urls'), name='subscription'),
    path('', include('utility_control.urls'), name='sell'),
]

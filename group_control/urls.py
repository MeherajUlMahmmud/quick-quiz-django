from django.urls import path, include
from rest_framework.routers import DefaultRouter

from group_control.views.group import GroupModelViewSet
from group_control.views.group_member import GroupMemberRequestModelViewSet, GroupMemberModelViewSet
from group_control.views.group_post import (GroupPostModelViewSet, GroupPostClapModelViewSet,
                                            GroupPostCommentModelViewSet)

router = DefaultRouter()
router.register(r'group', GroupModelViewSet, basename='group')
router.register(r'group-member-request', GroupMemberRequestModelViewSet, basename='group-member-request')
router.register(r'group-member', GroupMemberModelViewSet, basename='group-member')
router.register(r'group-post', GroupPostModelViewSet, basename='group-post')
router.register(r'group-post-clap', GroupPostClapModelViewSet, basename='group-post-clap')
router.register(r'group-post-comment', GroupPostCommentModelViewSet, basename='group-post-comment')

urlpatterns = [
    path('', include(router.urls)),
]

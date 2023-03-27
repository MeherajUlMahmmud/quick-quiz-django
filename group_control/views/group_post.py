from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from common.custom_pagination import CustomPageNumberPagination
from common.custom_view import CustomModelViewSet
from group_control.custom_filters import GroupPostClapModelFilter, GroupPostModelFilter, GroupPostCommentModelFilter
from group_control.models import GroupPostModel, GroupPostClapModel, GroupPostCommentModel
from group_control.serializers.group_post import (GroupPostModelSerializer, GroupPostClapModelSerializer,
                                                  GroupPostCommentModelSerializer)


class GroupPostModelViewSet(CustomModelViewSet):
    http_method_names = ['get', 'head', 'options', 'post', 'put', 'patch', 'delete']
    queryset = GroupPostModel.objects.all().order_by('-created_at')
    permission_classes = [IsAuthenticated]
    filterset_class = GroupPostModelFilter
    filter_backends = [DjangoFilterBackend]
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GroupPostModelSerializer.List
        elif self.request.method == 'POST':
            return GroupPostModelSerializer.Write
        elif self.request.method == 'PATCH':
            return GroupPostModelSerializer.Update
        return GroupPostModelSerializer.List

    def get_queryset(self):
        return GroupPostModel.objects.filter(group__created_by=self.request.user).order_by('-created_at')


class GroupPostClapModelViewSet(CustomModelViewSet):
    http_method_names = ['get', 'head', 'options', 'post', 'put', 'patch', 'delete']
    queryset = GroupPostClapModel.objects.all().order_by('-created_at')
    permission_classes = [IsAuthenticated]
    filterset_class = GroupPostClapModelFilter
    filter_backends = [DjangoFilterBackend]
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GroupPostClapModelSerializer.List
        elif self.request.method == 'POST':
            return GroupPostClapModelSerializer.Write
        elif self.request.method == 'PATCH':
            return GroupPostClapModelSerializer.Update
        return GroupPostClapModelSerializer.List

    def get_queryset(self):
        return GroupPostClapModel.objects.filter(group_post__group__created_by=self.request.user) \
            .order_by('-created_at')


class GroupPostCommentModelViewSet(CustomModelViewSet):
    http_method_names = ['get', 'head', 'options', 'post', 'put', 'patch', 'delete']
    queryset = GroupPostCommentModel.objects.all().order_by('-created_at')
    permission_classes = [IsAuthenticated]
    filterset_class = GroupPostCommentModelFilter
    filter_backends = [DjangoFilterBackend]
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GroupPostCommentModelSerializer.List
        elif self.request.method == 'POST':
            return GroupPostCommentModelSerializer.Write
        elif self.request.method == 'PATCH':
            return GroupPostCommentModelSerializer.Update
        return GroupPostCommentModelSerializer.List

    def get_queryset(self):
        return GroupPostCommentModel.objects.filter(group_post__group__created_by=self.request.user).order_by(
            '-created_at')

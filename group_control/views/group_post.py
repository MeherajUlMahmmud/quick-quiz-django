from rest_framework.permissions import IsAuthenticated

from common.custom_view import CustomModelViewSet
from group_control.custom_filters.clap_comment import GroupPostClapModelFilter, GroupPostCommentModelFilter
from group_control.custom_filters.group_post import GroupPostModelFilter
from group_control.models import GroupPostModel, GroupPostClapModel, GroupPostCommentModel
from group_control.serializers.group_post import (GroupPostModelSerializer, GroupPostClapModelSerializer,
                                                  GroupPostCommentModelSerializer)


class GroupPostModelViewSet(CustomModelViewSet):
    http_method_names = ['get', 'head', 'options', 'post', 'put', 'patch', 'delete']
    queryset = GroupPostModel.objects.all()
    permission_classes = [IsAuthenticated]
    filterset_class = GroupPostModelFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GroupPostModelSerializer.List
        elif self.request.method == 'POST':
            return GroupPostModelSerializer.Write
        elif self.request.method == 'PATCH':
            return GroupPostModelSerializer.Update
        return GroupPostModelSerializer.List

    def get_queryset(self):
        return GroupPostModel.objects.filter(group__created_by=self.request.user)


class GroupPostClapModelViewSet(CustomModelViewSet):
    http_method_names = ['get', 'head', 'options', 'post', 'put', 'patch', 'delete']
    queryset = GroupPostClapModel.objects.all()
    permission_classes = [IsAuthenticated]
    filterset_class = GroupPostClapModelFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GroupPostClapModelSerializer.List
        elif self.request.method == 'POST':
            return GroupPostClapModelSerializer.Write
        elif self.request.method == 'PATCH':
            return GroupPostClapModelSerializer.Update
        return GroupPostClapModelSerializer.List

    def get_queryset(self):
        return GroupPostClapModel.objects.filter(group_post__group__created_by=self.request.user)


class GroupPostCommentModelViewSet(CustomModelViewSet):
    http_method_names = ['get', 'head', 'options', 'post', 'put', 'patch', 'delete']
    queryset = GroupPostCommentModel.objects.all()
    permission_classes = [IsAuthenticated]
    filterset_class = GroupPostCommentModelFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GroupPostCommentModelSerializer.List
        elif self.request.method == 'POST':
            return GroupPostCommentModelSerializer.Write
        elif self.request.method == 'PATCH':
            return GroupPostCommentModelSerializer.Update
        return GroupPostCommentModelSerializer.List

    def get_queryset(self):
        return GroupPostCommentModel.objects.filter(group_post__group__created_by=self.request.user)

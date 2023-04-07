from rest_framework.permissions import IsAuthenticated

from common.custom_view import CustomModelViewSet
from group_control.custom_filters.group_member import GroupMemberModelFilter
from group_control.custom_filters.group_member_request import GroupMemberRequestModelFilter
from group_control.models import GroupMemberRequestModel, GroupMemberModel
from group_control.serializers.group_member import GroupMemberRequestModelSerializer, GroupMemberModelSerializer


class GroupMemberRequestModelViewSet(CustomModelViewSet):
    http_method_names = ['get', 'head', 'options', 'post', 'put', 'patch', 'delete']
    queryset = GroupMemberRequestModel.objects.all()
    permission_classes = [IsAuthenticated]
    filterset_class = GroupMemberRequestModelFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GroupMemberRequestModelSerializer.List
        elif self.request.method == 'POST':
            return GroupMemberRequestModelSerializer.Write
        elif self.request.method == 'PATCH':
            return GroupMemberRequestModelSerializer.Update
        return GroupMemberRequestModelSerializer.List

    def get_queryset(self):
        return GroupMemberRequestModel.objects.filter(group__created_by=self.request.user)


class GroupMemberModelViewSet(CustomModelViewSet):
    http_method_names = ['get', 'head', 'options', 'post', 'put', 'patch', 'delete']
    queryset = GroupMemberModel.objects.all()
    permission_classes = [IsAuthenticated]
    filterset_class = GroupMemberModelFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GroupMemberModelSerializer.List
        elif self.request.method == 'POST':
            return GroupMemberModelSerializer.Write
        elif self.request.method == 'PATCH':
            return GroupMemberModelSerializer.Update
        return GroupMemberModelSerializer.List

    def get_queryset(self):
        if self.request.user.is_superuser:
            return GroupMemberModel.objects.all()
        return GroupMemberModel.objects.filter(group__created_by=self.request.user)

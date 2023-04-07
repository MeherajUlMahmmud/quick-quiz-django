import random
import string

from django.db import transaction
from django.db.models import F
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_403_FORBIDDEN

from common.custom_view import CustomModelViewSet
from group_control.custom_filters.group import GroupModelFilter
from group_control.models import GroupModel, GroupMemberModel, GroupPostModel
from group_control.serializers.group import GroupModelSerializer


class GroupModelViewSet(CustomModelViewSet):
    http_method_names = ['get', 'head', 'options', 'post', 'put', 'patch', 'delete']
    queryset = GroupModel.objects.all()
    permission_classes = [IsAuthenticated]
    filterset_class = GroupModelFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GroupModelSerializer.List
        elif self.request.method == 'POST':
            return GroupModelSerializer.Write
        elif self.request.method == 'PATCH':
            return GroupModelSerializer.Update
        return GroupModelSerializer.List

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        if not request.user.is_teacher:
            return Response({'error': 'Only teachers are allowed to create group'}, status=HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        unique_code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        serializer.save(unique_code=unique_code, created_by=request.user)
        return Response({'group': serializer.data}, status=HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        group = GroupModel.objects.filter(id=instance.id)

        group_serializer_data = GroupModelSerializer.List(group.first()).data
        members = GroupMemberModel.objects.filter(group=instance.id).values(
            'member',
        ).annotate(
            id=F('member__id'),
            name=F('member__name'),
            email=F('member__email'),
        ).values('id', 'name', 'email')
        group_serializer_data['members'] = members

        posts = GroupPostModel.objects.filter(group=instance.id).values(
            'id',
            'post',
            'claps',
            'comments',
            'created_at',
        ).annotate(
            author_id=F('created_by__id'),
            author_name=F('created_by__name'),
            author_email=F('created_by__email'),
        ).values('id', 'post', 'claps', 'comments', 'created_at', 'author_id', 'author_name', 'author_email')
        group_serializer_data['posts'] = posts

        return Response(group_serializer_data)

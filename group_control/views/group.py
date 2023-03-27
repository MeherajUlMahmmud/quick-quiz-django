import string
import random

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from common.custom_pagination import CustomPageNumberPagination
from common.custom_view import CustomModelViewSet
from group_control.custom_filters import GroupModelFilter
from group_control.models import GroupModel
from group_control.serializers.group import GroupModelSerializer


class GroupModelViewSet(CustomModelViewSet):
    http_method_names = ['get', 'head', 'options', 'post', 'put', 'patch', 'delete']
    queryset = GroupModel.objects.all().order_by('-created_at')
    permission_classes = [IsAuthenticated]
    search_fields = ['name']
    filterset_class = GroupModelFilter
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GroupModelSerializer.List
        elif self.request.method == 'POST':
            return GroupModelSerializer.Write
        elif self.request.method == 'PATCH':
            return GroupModelSerializer.Update
        return GroupModelSerializer.List

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        unique_code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        serializer.save(unique_code=unique_code, created_by=request.user)
        return Response({'group': serializer.data}, status=HTTP_201_CREATED)

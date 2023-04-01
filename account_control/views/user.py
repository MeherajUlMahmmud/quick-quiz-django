from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework import filters

from account_control.custom_filters import UserModelFilter
from account_control.models import UserModel
from account_control.serializers.user import UserModelSerializer
from common.custom_pagination import CustomPageNumberPagination
from common.custom_view import CustomModelViewSet


class UserModelViewSet(CustomModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = UserModel.objects.all().order_by('-created_at')
    permission_classes = [IsAuthenticated]
    search_fields = ['username']
    filterset_class = UserModelFilter
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserModelSerializer.Write
        elif self.request.method == 'PUT' or self.request.method == 'PATCH':
            return UserModelSerializer.Update
        return UserModelSerializer.List

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.is_staff or self.request.user.is_admin:
            return UserModel.objects.all().order_by('-created_at')
        return UserModel.objects.filter(id=self.request.user.id).order_by('-created_at')

    def retrieve(self, request, *args, **kwargs):
        user = UserModel.objects.get(id=kwargs['pk'])
        if request.user.is_admin:
            user_data = UserModelSerializer.List(user).data
            return Response({'user': user_data}, status=HTTP_200_OK)
        elif request.user.id == int(kwargs['pk']):
            user_data = UserModelSerializer.List(user).data
            return Response({'user': user_data}, status=HTTP_200_OK)
        return Response({'message': 'You are not authorized to perform this action'}, status=HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        user = UserModel.objects.get(id=kwargs['pk'])
        if request.user.is_admin:
            serializer = self.get_serializer(user, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            user_data = UserModelSerializer.List(user).data
            return Response({'user': user_data}, status=HTTP_200_OK)
        elif request.user.id == int(kwargs['pk']):
            serializer = self.get_serializer(user, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            user_data = UserModelSerializer.List(user).data
            return Response({'user': user_data}, status=HTTP_200_OK)
        return Response({'message': 'You are not authorized to perform this action'}, status=HTTP_400_BAD_REQUEST)

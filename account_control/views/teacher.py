from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from account_control.models import TeacherModel
from account_control.serializers.teacher import TeacherModelSerializer
from common.custom_pagination import CustomPageNumberPagination


class TeacherModelViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options']
    queryset = TeacherModel.objects.all().order_by('-created_at')
    serializer_class = TeacherModelSerializer.List
    search_fields = ['user']
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination

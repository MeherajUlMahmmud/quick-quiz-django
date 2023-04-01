from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from account_control.models import StudentModel
from account_control.serializers.student import StudentModelSerializer
from common.custom_pagination import CustomPageNumberPagination


class StudentModelViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options']
    queryset = StudentModel.objects.all().order_by('-created_at')
    serializer_class = StudentModelSerializer.List
    search_fields = ['user']
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination

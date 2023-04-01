from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN
from rest_framework.viewsets import ModelViewSet

from common.custom_pagination import CustomPageNumberPagination
from exam_control.models import OptionModel, OptionAttachmentModel
from exam_control.serializers.option import OptionModelSerializer, OptionAttachmentModelSerializer


class OptionModelViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'put', 'delete']
    queryset = OptionModel.objects.all().order_by('-created_at')
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OptionModelSerializer.List
        else:
            return OptionModelSerializer.Write

    def create(self, request, *args, **kwargs):
        if not request.user.is_teacher:
            return Response({'detail': 'Only teachers are allowed to create option.'}, status=HTTP_403_FORBIDDEN)


class OptionAttachmentModelViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete']
    queryset = OptionAttachmentModel.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OptionAttachmentModelSerializer.List
        else:
            return OptionAttachmentModelSerializer.Write

    def create(self, request, *args, **kwargs):
        if not request.user.is_teacher:
            return Response({'detail': 'Only teachers are allowed to create option attachment.'}, status=HTTP_403_FORBIDDEN)

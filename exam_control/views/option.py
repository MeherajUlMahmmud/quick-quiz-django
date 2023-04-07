from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN

from common.custom_view import CustomModelViewSet
from exam_control.models import OptionModel, OptionAttachmentModel
from exam_control.serializers.option import OptionModelSerializer, OptionAttachmentModelSerializer


class OptionModelViewSet(CustomModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'put', 'delete']
    queryset = OptionModel.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OptionModelSerializer.List
        else:
            return OptionModelSerializer.Write

    def create(self, request, *args, **kwargs):
        if not request.user.is_teacher:
            return Response({'detail': 'Only teachers are allowed to create option.'}, status=HTTP_403_FORBIDDEN)


class OptionAttachmentModelViewSet(CustomModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete']
    queryset = OptionAttachmentModel.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OptionAttachmentModelSerializer.List
        else:
            return OptionAttachmentModelSerializer.Write

    def create(self, request, *args, **kwargs):
        if not request.user.is_teacher:
            return Response({'detail': 'Only teachers are allowed to create option attachment.'},
                            status=HTTP_403_FORBIDDEN)

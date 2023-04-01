import os
import uuid

from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.viewsets import ModelViewSet

from common.custom_pagination import CustomPageNumberPagination
from utility_control.custom_filters import FeedbackModelFilter
from utility_control.models import FeedbackModel, FileModel
from utility_control.serializers import FeedbackSerializer, FileModelSerializer


class FeedbackModelViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete']
    queryset = FeedbackModel.objects.all().order_by('-created_at')
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = FeedbackModelFilter
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return FeedbackSerializer.List
        return FeedbackSerializer.Write


class FileModelViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'delete']
    queryset = FileModel.objects.all().order_by('-created_at')
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return FileModelSerializer.List
        return FileModelSerializer.Write

    def create(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        if file:
            file_type = file.content_type
            if file_type not in ['image/jpeg', 'image/png', 'application/pdf']:
                return Response({'detail': 'File type not supported.'}, status=HTTP_400_BAD_REQUEST)
            file_size = file.size
            if file_size > 10485760:  # 10MB
                return Response({'detail': 'File size too large.'}, status=HTTP_400_BAD_REQUEST)
            file_name = file.name
            file_extension = file_name.split('.')[-1]
            file_url = f'{uuid.uuid4()}_{file_name}.{file_extension}'
            file_path = os.path.join(settings.MEDIA_ROOT, file_url)
            with open(file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            file_model = FileModel.objects.create(
                file=file,
                file_type=file_type,
                file_size=file_size,
                file_name=file_name,
                file_extension=file_extension,
                file_url=file_path,
                created_by=request.user
            )
            return Response(FileModelSerializer.Write(file_model).data, status=HTTP_201_CREATED)
        return Response({'detail': 'File not found.'}, status=HTTP_400_BAD_REQUEST)

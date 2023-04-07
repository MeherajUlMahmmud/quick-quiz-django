from django.utils import timezone
from rest_framework.viewsets import ModelViewSet

from common.custom_pagination import CustomPageNumberPagination


class CustomModelViewSet(ModelViewSet):
    pagination_class = CustomPageNumberPagination

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user, updated_at=timezone.now())

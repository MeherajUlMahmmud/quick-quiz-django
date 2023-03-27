from django.utils import timezone

from rest_framework.viewsets import ModelViewSet


class CustomModelViewSet(ModelViewSet):

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user, updated_at=timezone.now())

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from common.custom_pagination import CustomPageNumberPagination
from utility_control.custom_filters import FeedbackModelFilter
from utility_control.models import FeedbackModel
from utility_control.serializers import FeedbackSerializer


class FeedbackModelViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete']
    queryset = FeedbackModel.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = FeedbackModelFilter
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return FeedbackSerializer.List
        return FeedbackSerializer.Write

from rest_framework.permissions import IsAuthenticated

from common.custom_view import CustomModelViewSet
from utility_control.custom_filters.feedback import FeedbackModelFilter
from utility_control.models import FeedbackModel
from utility_control.serializers.feedback import FeedbackModelSerializer


class FeedbackModelViewSet(CustomModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete']
    queryset = FeedbackModel.objects.all()
    permission_classes = [IsAuthenticated]
    filterset_class = FeedbackModelFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return FeedbackModelSerializer.List
        return FeedbackModelSerializer.Write

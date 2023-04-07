from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from utility_control.custom_filters.issue import IssueModelFilter
from utility_control.models import IssueModel
from utility_control.serializers.issue import IssueModelSerializer


class IssueModelViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete']
    queryset = IssueModel.objects.all()
    permission_classes = [IsAuthenticated]
    filterset_class = IssueModelFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return IssueModelSerializer.List
        return IssueModelSerializer.Write

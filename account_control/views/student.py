from rest_framework.permissions import IsAuthenticated

from account_control.custom_filters.student import StudentModelFilter
from account_control.models import StudentModel
from account_control.serializers.student import StudentModelSerializer
from common.custom_view import CustomModelViewSet


class StudentModelViewSet(CustomModelViewSet):
    http_method_names = ['get', 'head', 'options']
    queryset = StudentModel.objects.all()
    serializer_class = StudentModelSerializer.List
    permission_classes = [IsAuthenticated]
    filterset_class = StudentModelFilter

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.is_staff or self.request.user.is_admin:
            return StudentModel.objects.all()
        return StudentModel.objects.filter(id=self.request.user.id)

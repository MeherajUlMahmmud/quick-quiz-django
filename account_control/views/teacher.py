from rest_framework.permissions import IsAuthenticated

from account_control.custom_filters.teacher import TeacherModelFilter
from account_control.models import TeacherModel
from account_control.serializers.teacher import TeacherModelSerializer
from common.custom_view import CustomModelViewSet


class TeacherModelViewSet(CustomModelViewSet):
    http_method_names = ['get', 'head', 'options']
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherModelSerializer.List
    permission_classes = [IsAuthenticated]
    filterset_class = TeacherModelFilter

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.is_staff or self.request.user.is_admin:
            return TeacherModel.objects.all()
        return TeacherModel.objects.filter(id=self.request.user.id)

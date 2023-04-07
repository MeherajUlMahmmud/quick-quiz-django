from rest_framework.permissions import IsAuthenticated

from common.custom_pagination import CustomPageNumberPagination
from common.custom_view import CustomModelViewSet
from exam_control.models import StudentSubmissionModel, StudentSubmissionAnswerModel
from exam_control.serializers.submission import StudentSubmissionModelSerializer, StudentSubmissionAnswerModelSerializer


class StudentSubmissionViewSet(CustomModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = StudentSubmissionModel.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return StudentSubmissionModelSerializer.List
        elif self.request.method == 'POST':
            return StudentSubmissionModelSerializer.Write
        else:
            return StudentSubmissionModelSerializer.Update


class StudentSubmissionAnswerModelViewSet(CustomModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = StudentSubmissionAnswerModel.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return StudentSubmissionAnswerModelSerializer.List
        else:
            return StudentSubmissionAnswerModelSerializer.Write

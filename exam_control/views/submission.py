from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from common.custom_pagination import CustomPageNumberPagination
from exam_control.models import StudentSubmissionModel, StudentSubmissionAnswerModel
from exam_control.serializers.submission import StudentSubmissionModelSerializer, StudentSubmissionAnswerModelSerializer


class StudentSubmissionViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = StudentSubmissionModel.objects.all().order_by('-created_at')
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return StudentSubmissionModelSerializer.List
        elif self.request.method == 'POST':
            return StudentSubmissionModelSerializer.Write
        else:
            return StudentSubmissionModelSerializer.Update


class StudentSubmissionAnswerModelViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = StudentSubmissionAnswerModel.objects.all().order_by('-created_at')
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return StudentSubmissionAnswerModelSerializer.List
        else:
            return StudentSubmissionAnswerModelSerializer.Write

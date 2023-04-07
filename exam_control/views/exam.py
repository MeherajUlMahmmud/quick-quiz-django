from django.db import models
from django.db.models import Count, Avg
from django.db.models.functions import Coalesce
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN

from common.custom_view import CustomModelViewSet
from exam_control.models import ExamModel, StudentSubmissionModel
from exam_control.serializers.exam import ExamModelSerializer
from exam_control.serializers.question import QuestionModelSerializer


class ExamModelViewSet(CustomModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = ExamModel.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ExamModelSerializer.List
        return ExamModelSerializer.Write

    def create(self, request, *args, **kwargs):
        if not request.user.is_teacher:
            return Response({'detail': 'Only teachers are allowed to create exam.'}, status=HTTP_403_FORBIDDEN)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        exam = ExamModel.objects.filter(id=instance.id).annotate(
            total_questions=Coalesce(Count('questions__id', output_field=models.IntegerField()), 0),
        )
        exam_serializer_data = ExamModelSerializer.Details(exam.first()).data
        questions = instance.questions.all()
        question_serializer_data = QuestionModelSerializer.ForExam(questions, many=True).data
        exam_serializer_data['questions'] = question_serializer_data
        return Response(exam_serializer_data)

    @action(detail=True, methods=['get'])
    def leaderboard(self, request, pk=None):
        exam = self.get_object()
        submissions = StudentSubmissionModel.objects.filter(exam=exam).select_related('student')
        leaderboard = submissions.values('student').annotate(score=Avg('score')).order_by('-score')
        return Response(leaderboard)

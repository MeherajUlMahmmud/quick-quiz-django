from django.db import models
from django.db.models import Count
from django.db.models.functions import Coalesce
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN

from common.custom_view import CustomModelViewSet
from exam_control.models import QuestionModel, QuestionAttachmentModel
from exam_control.serializers.option import OptionModelSerializer
from exam_control.serializers.question import QuestionModelSerializer, QuestionAttachmentModelSerializer


class QuestionModelViewSet(CustomModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = QuestionModel.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return QuestionModelSerializer.List
        else:
            return QuestionModelSerializer.Write

    def create(self, request, *args, **kwargs):
        if not request.user.is_teacher:
            return Response({'detail': 'Only teachers are allowed to create question.'}, status=HTTP_403_FORBIDDEN)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        question = QuestionModel.objects.filter(id=instance.id).annotate(
            total_attachments=Coalesce(Count('attachments__id', output_field=models.IntegerField()), 0),
            total_options=Coalesce(Count('options__id', output_field=models.IntegerField()), 0),
        )
        question_serializer_data = QuestionModelSerializer.Details(question.first()).data
        options = instance.options.all()
        option_serializer_data = OptionModelSerializer.Lite(options, many=True).data
        attachments = instance.attachments.all()
        attachment_serializer_data = QuestionAttachmentModelSerializer.Lite(attachments, many=True).data
        question_serializer_data['options'] = option_serializer_data
        question_serializer_data['attachments'] = attachment_serializer_data
        return Response(question_serializer_data)


class QuestionAttachmentModelViewSet(CustomModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = QuestionAttachmentModel.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return QuestionAttachmentModelSerializer.List
        else:
            return QuestionAttachmentModelSerializer.Write

    def create(self, request, *args, **kwargs):
        if not request.user.is_teacher:
            return Response({'detail': 'Only teachers are allowed to create question attachment.'},
                            status=HTTP_403_FORBIDDEN)

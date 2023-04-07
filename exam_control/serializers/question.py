from rest_framework.serializers import ModelSerializer, IntegerField

from exam_control.models import QuestionAttachmentModel, QuestionModel
from exam_control.serializers.exam import ExamModelSerializer
from exam_control.serializers.option import OptionModelSerializer


class QuestionAttachmentModelSerializerMeta(ModelSerializer):
    class Meta:
        model = QuestionAttachmentModel
        fields = [
            'question',
            'attachment',
        ]


class QuestionAttachmentModelSerializer:
    class List(QuestionAttachmentModelSerializerMeta):
        class Meta(QuestionAttachmentModelSerializerMeta.Meta):
            fields = QuestionAttachmentModelSerializerMeta.Meta.fields + [
                'id',
                'created_at',
                'updated_at',
            ]

    class Lite(QuestionAttachmentModelSerializerMeta):
        class Meta(QuestionAttachmentModelSerializerMeta.Meta):
            fields = QuestionAttachmentModelSerializerMeta.Meta.fields + [
                'id',
            ]

    class Write(QuestionAttachmentModelSerializerMeta):
        class Meta(QuestionAttachmentModelSerializerMeta.Meta):
            fields = QuestionAttachmentModelSerializerMeta.Meta.fields


class QuestionModelSerializerMeta(ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = [
            'exam',
            'type',
            'prompt',
        ]


class QuestionModelSerializer:
    class List(QuestionModelSerializerMeta):
        exam = ExamModelSerializer.Lite()

        class Meta(QuestionModelSerializerMeta.Meta):
            fields = QuestionModelSerializerMeta.Meta.fields + [
                'id',
                'created_at',
                'updated_at',
            ]

    class Lite(QuestionModelSerializerMeta):
        class Meta(QuestionModelSerializerMeta.Meta):
            fields = [
                'id',
                'exam',
                'type',
                'prompt',
            ]

    class Details(QuestionModelSerializerMeta):
        total_attachments = IntegerField()
        total_options = IntegerField()

        class Meta(QuestionModelSerializerMeta.Meta):
            fields = QuestionModelSerializerMeta.Meta.fields + [
                'id',
                'total_attachments',
                'total_options',
            ]

    class ForExam(QuestionModelSerializerMeta):
        attachments = QuestionAttachmentModelSerializer.Lite(many=True, allow_null=True)
        options = OptionModelSerializer.Lite(many=True, allow_null=True)

        class Meta(QuestionModelSerializerMeta.Meta):
            fields = [
                'id',
                'exam',
                'type',
                'prompt',
                'attachments',
                'options',
            ]

    class Write(QuestionModelSerializerMeta):
        class Meta(QuestionModelSerializerMeta.Meta):
            fields = QuestionModelSerializerMeta.Meta.fields

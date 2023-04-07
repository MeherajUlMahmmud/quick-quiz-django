from rest_framework.serializers import ModelSerializer, IntegerField

from account_control.serializers.user import UserModelSerializer
from exam_control.models import ExamModel


class ExamModelSerializerMeta(ModelSerializer):
    class Meta:
        model = ExamModel
        fields = [
            'title',
            'description',
            'total_duration',
            'student_duration',
            'created_by',
        ]


class ExamModelSerializer:
    class List(ExamModelSerializerMeta):
        created_by = UserModelSerializer.Lite()

        class Meta(ExamModelSerializerMeta.Meta):
            fields = ExamModelSerializerMeta.Meta.fields + [
                'id',
                'total_score',
                'is_published',
                'is_completed',
                'created_at',
                'updated_at',
            ]

    class Lite(ExamModelSerializerMeta):
        class Meta(ExamModelSerializerMeta.Meta):
            fields = [
                'id',
                'title',
                'description',
                'total_duration',
                'student_duration',
                'created_by',
            ]

    class Details(ExamModelSerializerMeta):
        total_questions = IntegerField()
        created_by = UserModelSerializer.Lite()

        class Meta(ExamModelSerializerMeta.Meta):
            fields = ExamModelSerializerMeta.Meta.fields + [
                'id',
                'total_score',
                'total_questions',
                'is_published',
                'is_completed',
                'created_at',
                'updated_at',
            ]

    class Write(ExamModelSerializerMeta):
        class Meta(ExamModelSerializerMeta.Meta):
            fields = ExamModelSerializerMeta.Meta.fields

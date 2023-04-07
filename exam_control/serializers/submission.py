from rest_framework.serializers import ModelSerializer

from exam_control.models import StudentSubmissionModel, StudentSubmissionAnswerModel


class StudentSubmissionModelSerializerMeta(ModelSerializer):
    class Meta:
        model = StudentSubmissionModel
        fields = [
            'exam',
            'student',
            'started_at',
        ]


class StudentSubmissionModelSerializer:
    class List(StudentSubmissionModelSerializerMeta):
        class Meta(StudentSubmissionModelSerializerMeta.Meta):
            fields = StudentSubmissionModelSerializerMeta.Meta.fields + [
                'id',
                'submitted_at',
                'duration',
                'score',
                'is_graded',
                'feedback',
                'created_at',
                'updated_at',
            ]

    class Write(StudentSubmissionModelSerializerMeta):
        class Meta(StudentSubmissionModelSerializerMeta.Meta):
            fields = StudentSubmissionModelSerializerMeta.Meta.fields

    class Update(StudentSubmissionModelSerializerMeta):
        class Meta(StudentSubmissionModelSerializerMeta.Meta):
            fields = StudentSubmissionModelSerializerMeta.Meta.fields + [
                'submitted_at',
                'feedback',
            ]


class StudentSubmissionAnswerModelSerializerMeta(ModelSerializer):
    class Meta:
        model = StudentSubmissionAnswerModel
        fields = [
            'id',
            'submission',
            'question',
            'option',
        ]


class StudentSubmissionAnswerModelSerializer:
    class List(StudentSubmissionAnswerModelSerializerMeta):
        class Meta(StudentSubmissionAnswerModelSerializerMeta.Meta):
            fields = StudentSubmissionAnswerModelSerializerMeta.Meta.fields

    class Write(StudentSubmissionAnswerModelSerializerMeta):
        class Meta(StudentSubmissionAnswerModelSerializerMeta.Meta):
            fields = StudentSubmissionAnswerModelSerializerMeta.Meta.fields

    class Update(StudentSubmissionAnswerModelSerializerMeta):
        class Meta(StudentSubmissionAnswerModelSerializerMeta.Meta):
            fields = StudentSubmissionAnswerModelSerializerMeta.Meta.fields

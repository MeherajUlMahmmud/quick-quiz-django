from rest_framework.serializers import ModelSerializer, SerializerMethodField

from account_control.models import StudentModel


class StudentModelSerializerMeta(ModelSerializer):
    class Meta:
        model = StudentModel
        fields = [
            'id',
        ]


class StudentModelSerializer:
    class List(StudentModelSerializerMeta):
        user = SerializerMethodField()

        def get_user(self, obj):
            return obj.user.username

        class Meta(StudentModelSerializerMeta.Meta):
            fields = StudentModelSerializerMeta.Meta.fields + [
                'user',
            ]

    class Lite(StudentModelSerializerMeta):
        class Meta(StudentModelSerializerMeta.Meta):
            fields = StudentModelSerializerMeta.Meta.fields

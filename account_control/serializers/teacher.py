from rest_framework.serializers import ModelSerializer, SerializerMethodField

from account_control.models import TeacherModel


class TeacherModelSerializerMeta(ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = [
            'id',
        ]


class TeacherModelSerializer:
    class List(TeacherModelSerializerMeta):
        user = SerializerMethodField()

        def get_user(self, obj):
            return obj.user.username

        class Meta(TeacherModelSerializerMeta.Meta):
            fields = TeacherModelSerializerMeta.Meta.fields + [
                'user',
            ]

    class Lite(TeacherModelSerializerMeta):
        class Meta(TeacherModelSerializerMeta.Meta):
            fields = TeacherModelSerializerMeta.Meta.fields

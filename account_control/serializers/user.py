from rest_framework.serializers import ModelSerializer, CharField, ValidationError

from account_control.models import UserModel


class UserModelSerializerMeta(ModelSerializer):
    class Meta:
        model = UserModel
        fields = [
            'id',
            'username',
            'name',
            'email',
        ]


class UserModelSerializer:
    class Write(UserModelSerializerMeta):
        password = CharField(write_only=True)

        class Meta(UserModelSerializerMeta.Meta):
            fields = UserModelSerializerMeta.Meta.fields + [
                'password',
                'is_student',
                'is_teacher',
            ]
            read_only_fields = ['id', 'password']

        def validate(self, attrs):
            password = attrs.get('password', '')
            is_student = attrs.get('is_student', False)
            is_teacher = attrs.get('is_teacher', False)
            if not is_student and not is_teacher:
                raise ValidationError(
                    "User must be either student or teacher"
                )
            if is_student and is_teacher:
                raise ValidationError(
                    "User cannot be both player and agent"
                )
            if len(password) < 6:
                raise ValidationError(
                    "Password must be at least 6 characters"
                )
            return attrs

        def save(self, **kwargs):
            password = self.validated_data.pop('password')
            user = UserModel.objects.create(**self.validated_data)
            user.set_password(password)
            user.password_plain = password
            user.save()
            return user

    class Update(UserModelSerializerMeta):
        class Meta(UserModelSerializerMeta.Meta):
            fields = UserModelSerializerMeta.Meta.fields + [
                'phone',
                'email',
            ]
            read_only_fields = ['id']

    class List(UserModelSerializerMeta):

        class Meta(UserModelSerializerMeta.Meta):
            fields = UserModelSerializerMeta.Meta.fields + [
                'phone',
                'email',
                'is_student',
                'is_teacher',
                'is_active',
                'is_admin',
                'student',
                'teacher',
            ]

    class Lite(UserModelSerializerMeta):
        class Meta(UserModelSerializerMeta.Meta):
            fields = UserModelSerializerMeta.Meta.fields + [
                'email',
            ]

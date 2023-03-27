from rest_framework.serializers import ModelSerializer

from account_control.serializers.user import UserModelSerializer
from group_control.models import GroupModel


class GroupModelSerializerMeta(ModelSerializer):
    class Meta:
        model = GroupModel
        fields = [
            'id',
            'name',
            'description',
            'unique_code',
        ]


class GroupModelSerializer:
    class List(GroupModelSerializerMeta):
        created_by = UserModelSerializer.Lite(many=False, allow_null=True, read_only=True)

        class Meta(GroupModelSerializerMeta.Meta):
            fields = GroupModelSerializerMeta.Meta.fields + [
                'created_by',
                'cover_picture',
                'profile_picture',
            ]

    class Write(GroupModelSerializerMeta):
        class Meta(GroupModelSerializerMeta.Meta):
            fields = GroupModelSerializerMeta.Meta.fields

    class Update(GroupModelSerializerMeta):
        class Meta(GroupModelSerializerMeta.Meta):
            fields = GroupModelSerializerMeta.Meta.fields + [
                'cover_picture',
                'profile_picture',
            ]

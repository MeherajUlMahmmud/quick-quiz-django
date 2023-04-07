from rest_framework.serializers import ModelSerializer

from account_control.serializers.user import UserModelSerializer
from group_control.models import GroupMemberRequestModel, GroupMemberModel
from group_control.serializers.group import GroupModelSerializer


class GroupMemberRequestModelSerializerMeta(ModelSerializer):
    class Meta:
        model = GroupMemberRequestModel
        fields = [
            'id',
            'group',
            'user',
            'status',
            'accepted_by',
            'rejected_by',
        ]


class GroupMemberRequestModelSerializer:
    class List(GroupMemberRequestModelSerializerMeta):
        class Meta(GroupMemberRequestModelSerializerMeta.Meta):
            fields = GroupMemberRequestModelSerializerMeta.Meta.fields

    class Write(GroupMemberRequestModelSerializerMeta):
        class Meta(GroupMemberRequestModelSerializerMeta.Meta):
            fields = GroupMemberRequestModelSerializerMeta.Meta.fields

    class Update(GroupMemberRequestModelSerializerMeta):
        class Meta(GroupMemberRequestModelSerializerMeta.Meta):
            fields = GroupMemberRequestModelSerializerMeta.Meta.fields


class GroupMemberModelSerializerMeta(ModelSerializer):
    group = GroupModelSerializer.List(many=False, allow_null=True, read_only=True)
    member = UserModelSerializer.Lite(many=False, allow_null=True, read_only=True)

    class Meta:
        model = GroupMemberModel
        fields = [
            'id',
            'group',
            'member',
        ]


class GroupMemberModelSerializer:
    class List(GroupMemberModelSerializerMeta):
        class Meta(GroupMemberModelSerializerMeta.Meta):
            fields = GroupMemberModelSerializerMeta.Meta.fields

    class Write(GroupMemberModelSerializerMeta):
        class Meta(GroupMemberModelSerializerMeta.Meta):
            fields = GroupMemberModelSerializerMeta.Meta.fields

    class Update(GroupMemberModelSerializerMeta):
        class Meta(GroupMemberModelSerializerMeta.Meta):
            fields = [
                'is_admin',
                'is_moderator',
            ]

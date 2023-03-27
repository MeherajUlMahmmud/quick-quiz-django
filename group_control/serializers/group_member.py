from rest_framework.serializers import ModelSerializer

from group_control.models import GroupMemberRequestModel, GroupMemberModel


class GroupMemberRequestModelSerializerMeta(ModelSerializer):
    class Meta:
        model = GroupMemberRequestModel
        fields = ('id', 'group', 'user', 'status', 'accepted_by', 'rejected_by')


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
    class Meta:
        model = GroupMemberModel
        fields = ('id', 'group', 'user', 'is_admin', 'is_moderator')


class GroupMemberModelSerializer:
    class List(GroupMemberModelSerializerMeta):
        class Meta(GroupMemberModelSerializerMeta.Meta):
            fields = GroupMemberModelSerializerMeta.Meta.fields

    class Write(GroupMemberModelSerializerMeta):
        class Meta(GroupMemberModelSerializerMeta.Meta):
            fields = GroupMemberModelSerializerMeta.Meta.fields

    class Update(GroupMemberModelSerializerMeta):
        class Meta(GroupMemberModelSerializerMeta.Meta):
            fields = GroupMemberModelSerializerMeta.Meta.fields

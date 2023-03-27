from rest_framework.serializers import ModelSerializer

from group_control.models import GroupPostModel, GroupPostClapModel, GroupPostCommentModel


class GroupPostModelSerializerMeta(ModelSerializer):
    class Meta:
        model = GroupPostModel
        fields = [
            'id',
            'group',
            'created_by',
            'post',
            'files',
        ]


class GroupPostModelSerializer:
    class List(GroupPostModelSerializerMeta):
        class Meta(GroupPostModelSerializerMeta.Meta):
            fields = GroupPostModelSerializerMeta.Meta.fields + [
                'claps',
                'comments',
                'created_at',
            ]

    class Write(GroupPostModelSerializerMeta):
        class Meta(GroupPostModelSerializerMeta.Meta):
            fields = GroupPostModelSerializerMeta.Meta.fields

    class Update(GroupPostModelSerializerMeta):
        class Meta(GroupPostModelSerializerMeta.Meta):
            fields = GroupPostModelSerializerMeta.Meta.fields

    class Delete(GroupPostModelSerializerMeta):
        class Meta(GroupPostModelSerializerMeta.Meta):
            fields = GroupPostModelSerializerMeta.Meta.fields

    class Detail(GroupPostModelSerializerMeta):
        class Meta(GroupPostModelSerializerMeta.Meta):
            fields = GroupPostModelSerializerMeta.Meta.fields


class GroupPostClapModelSerializerMeta(ModelSerializer):
    class Meta:
        model = GroupPostClapModel
        fields = [
            'id',
            'group_post',
            'created_by',
        ]


class GroupPostClapModelSerializer:
    class List(GroupPostClapModelSerializerMeta):
        class Meta(GroupPostClapModelSerializerMeta.Meta):
            fields = GroupPostClapModelSerializerMeta.Meta.fields

    class Write(GroupPostClapModelSerializerMeta):
        class Meta(GroupPostClapModelSerializerMeta.Meta):
            fields = GroupPostClapModelSerializerMeta.Meta.fields

    class Update(GroupPostClapModelSerializerMeta):
        class Meta(GroupPostClapModelSerializerMeta.Meta):
            fields = GroupPostClapModelSerializerMeta.Meta.fields


class GroupPostCommentModelSerializerMeta(ModelSerializer):
    class Meta:
        model = GroupPostCommentModel
        fields = [
            'id',
            'group_post',
            'comment',
            'file',
            'created_by',
        ]


class GroupPostCommentModelSerializer:
    class List(GroupPostCommentModelSerializerMeta):
        class Meta(GroupPostCommentModelSerializerMeta.Meta):
            fields = GroupPostCommentModelSerializerMeta.Meta.fields

    class Write(GroupPostCommentModelSerializerMeta):
        class Meta(GroupPostCommentModelSerializerMeta.Meta):
            fields = GroupPostCommentModelSerializerMeta.Meta.fields

    class Update(GroupPostCommentModelSerializerMeta):
        class Meta(GroupPostCommentModelSerializerMeta.Meta):
            fields = GroupPostCommentModelSerializerMeta.Meta.fields

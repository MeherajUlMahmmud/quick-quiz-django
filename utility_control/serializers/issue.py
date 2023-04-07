from rest_framework.serializers import ModelSerializer

from utility_control.models import IssueModel


class IssueModelSerializerMeta(ModelSerializer):
    class Meta:
        model = IssueModel
        fields = [
            'title',
            'description',
            'status',
        ]


class IssueModelSerializer:
    class List(IssueModelSerializerMeta):
        class Meta(IssueModelSerializerMeta.Meta):
            fields = IssueModelSerializerMeta.Meta.fields + [
                'id',
                'created_at',
                'updated_at',
            ]

    class Write(IssueModelSerializerMeta):
        class Meta(IssueModelSerializerMeta.Meta):
            fields = IssueModelSerializerMeta.Meta.fields

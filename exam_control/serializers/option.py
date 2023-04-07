from rest_framework.serializers import ModelSerializer

from exam_control.models import OptionModel, OptionAttachmentModel


class OptionAttachmentModelSerializerMeta(ModelSerializer):
    class Meta:
        model = OptionAttachmentModel
        fields = [
            'option',
            'attachment',
        ]


class OptionAttachmentModelSerializer:
    class List(OptionAttachmentModelSerializerMeta):
        class Meta(OptionAttachmentModelSerializerMeta.Meta):
            fields = OptionAttachmentModelSerializerMeta.Meta.fields + [
                'id',
                'created_at',
                'updated_at',
            ]

    class Lite(OptionAttachmentModelSerializerMeta):
        class Meta(OptionAttachmentModelSerializerMeta.Meta):
            fields = OptionAttachmentModelSerializerMeta.Meta.fields + [
                'id',
            ]

    class Write(OptionAttachmentModelSerializerMeta):
        class Meta(OptionAttachmentModelSerializerMeta.Meta):
            fields = OptionAttachmentModelSerializerMeta.Meta.fields


class OptionModelSerializerMeta(ModelSerializer):
    class Meta:
        model = OptionModel
        fields = [
            'id',
            'question',
            'text',
            'is_correct',
        ]


class OptionModelSerializer:
    class List(OptionModelSerializerMeta):
        class Meta(OptionModelSerializerMeta.Meta):
            fields = OptionModelSerializerMeta.Meta.fields

    class Lite(OptionModelSerializerMeta):
        attachments = OptionAttachmentModelSerializer.Lite(many=True, allow_null=True)

        class Meta(OptionModelSerializerMeta.Meta):
            fields = OptionModelSerializerMeta.Meta.fields + [
                'attachments',
            ]

    class Write(OptionModelSerializerMeta):
        class Meta(OptionModelSerializerMeta.Meta):
            fields = OptionModelSerializerMeta.Meta.fields

    class Update(OptionModelSerializerMeta):
        class Meta(OptionModelSerializerMeta.Meta):
            fields = OptionModelSerializerMeta.Meta.fields

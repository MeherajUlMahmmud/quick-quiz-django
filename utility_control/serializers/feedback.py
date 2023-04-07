from rest_framework.serializers import ModelSerializer

from utility_control.models import FeedbackModel


class FeedbackSerializerMeta(ModelSerializer):
    class Meta:
        model = FeedbackModel
        fields = [
            'name',
            'email',
            'message',
            'source',
        ]


class FeedbackModelSerializer(FeedbackSerializerMeta):
    class Write(FeedbackSerializerMeta):
        class Meta(FeedbackSerializerMeta.Meta):
            fields = FeedbackSerializerMeta.Meta.fields

    class List(FeedbackSerializerMeta):
        class Meta(FeedbackSerializerMeta.Meta):
            fields = FeedbackSerializerMeta.Meta.fields + [
                'id',
                'created_at',
                'updated_at',
            ]

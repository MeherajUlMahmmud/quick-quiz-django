from rest_framework.serializers import ModelSerializer

from utility_control.models import FeedbackModel, FileModel


class FeedbackSerializerMeta(ModelSerializer):
    class Meta:
        model = FeedbackModel
        fields = ['name', 'email', 'message', 'source']


class FeedbackSerializer(FeedbackSerializerMeta):
    class Write(FeedbackSerializerMeta):
        class Meta(FeedbackSerializerMeta.Meta):
            fields = FeedbackSerializerMeta.Meta.fields

    class List(FeedbackSerializerMeta):
        class Meta(FeedbackSerializerMeta.Meta):
            fields = FeedbackSerializerMeta.Meta.fields + ['id', 'created_at', 'updated_at']


class FileModelSerializerMeta(ModelSerializer):
    class Meta:
        model = FileModel
        fields = ['file']


class FileModelSerializer:
    class Write(FileModelSerializerMeta):
        class Meta(FileModelSerializerMeta.Meta):
            fields = FileModelSerializerMeta.Meta.fields

    class List(FileModelSerializerMeta):
        class Meta(FileModelSerializerMeta.Meta):
            fields = FileModelSerializerMeta.Meta.fields + ['id', 'file_name', 'file_type', 'file_size',
                                                            'created_at', 'updated_at']

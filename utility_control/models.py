from django.db import models
from common.choices import FeedbackSource

from common.models import BaseModel


class FileModel(BaseModel):
    file = models.FileField(upload_to='files')
    file_type = models.CharField(max_length=255)
    file_size = models.IntegerField()
    file_name = models.CharField(max_length=255)
    file_extension = models.CharField(max_length=255)
    file_url = models.CharField(max_length=255)

    class Meta:
        db_table = 'file'
        verbose_name = 'File'
        verbose_name_plural = 'Files'

    def __str__(self):
        return self.file_name


class FeedbackModel(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField()
    source = models.CharField(max_length=255, choices=FeedbackSource.choices, default=FeedbackSource.WEBSITE)
    file = models.ForeignKey(FileModel, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'feedback'
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'

    def __str__(self):
        return self.name

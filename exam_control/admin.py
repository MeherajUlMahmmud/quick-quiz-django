from django.contrib import admin

from exam_control.models import ExamModel, QuestionModel, QuestionAttachmentModel, OptionModel, OptionAttachmentModel

admin.site.register(ExamModel)
admin.site.register(QuestionModel)
admin.site.register(QuestionAttachmentModel)
admin.site.register(OptionModel)
admin.site.register(OptionAttachmentModel)

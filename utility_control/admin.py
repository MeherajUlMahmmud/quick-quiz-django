from django.contrib import admin
from utility_control.models import FileModel, FeedbackModel


class FeedbackModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'source', 'created_at', 'updated_at')
    list_filter = ('source', 'created_at', 'updated_at')
    search_fields = ('name', 'message')


admin.site.register(FileModel)
admin.site.register(FeedbackModel, FeedbackModelAdmin)

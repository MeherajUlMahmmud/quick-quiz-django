from django.contrib import admin

from group_control.models import GroupModel, GroupMemberModel, GroupMemberRequestModel, GroupPostModel, \
    GroupPostClapModel, GroupPostCommentModel


class GroupModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'unique_code', 'created_by', 'cover_picture', 'profile_picture')
    search_fields = ('name', 'description', 'unique_code', 'created_by', 'cover_picture', 'profile_picture')
    list_filter = ('name', 'description', 'unique_code', 'created_by', 'cover_picture', 'profile_picture')


admin.site.register(GroupModel, GroupModelAdmin)
admin.site.register(GroupMemberModel)
admin.site.register(GroupMemberRequestModel)
admin.site.register(GroupPostModel)
admin.site.register(GroupPostClapModel)
admin.site.register(GroupPostCommentModel)

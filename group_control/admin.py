from django.contrib import admin

from group_control.models import (GroupModel, GroupMemberModel, GroupMemberRequestModel, GroupPostModel,
                                  GroupPostClapModel, GroupPostCommentModel)


class GroupModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'unique_code', 'created_by', 'created_at')
    search_fields = ('name', 'unique_code')
    list_filter = ('name', 'unique_code', 'created_by')


class GroupMemberModelAdmin(admin.ModelAdmin):
    list_display = ('group', 'member', 'is_admin', 'is_moderator')
    search_fields = ('group', 'member', 'is_admin', 'is_moderator')
    list_filter = ('group', 'member', 'is_admin', 'is_moderator')


admin.site.register(GroupModel, GroupModelAdmin)
admin.site.register(GroupMemberModel, GroupMemberModelAdmin)
admin.site.register(GroupMemberRequestModel)
admin.site.register(GroupPostModel)
admin.site.register(GroupPostClapModel)
admin.site.register(GroupPostCommentModel)

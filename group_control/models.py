from django.db import models

from account_control.models import UserModel
from common.choices import GroupMemberRequestStatus
from common.models import BaseModel
from utility_control.models import FileModel


class GroupModel(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    cover_picture = models.ForeignKey(FileModel, on_delete=models.SET_NULL, related_name='cover_picture', null=True,
                                      blank=True)
    profile_picture = models.ForeignKey(FileModel, on_delete=models.SET_NULL, related_name='profile_picture', null=True,
                                        blank=True)
    unique_code = models.CharField(max_length=255)
    total_members = models.IntegerField(default=0)
    is_auto_accept = models.BooleanField(default=False)

    class Meta:
        db_table = 'group'

        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

    def __str__(self):
        return self.name


class GroupMemberRequestModel(BaseModel):
    group = models.ForeignKey(GroupModel, on_delete=models.CASCADE, related_name='req_group')
    member = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='req_members')
    status = models.CharField(max_length=255, choices=GroupMemberRequestStatus.choices,
                              default=GroupMemberRequestStatus.PENDING)
    accepted_by = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='accepted_by', null=True,
                                    blank=True)
    rejected_by = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='rejected_by', null=True,
                                    blank=True)

    class Meta:
        db_table = 'group_member_request'

        verbose_name = 'Group Member Request'
        verbose_name_plural = 'Group Member Requests'


class GroupMemberModel(BaseModel):
    group = models.ForeignKey(GroupModel, on_delete=models.CASCADE, related_name='group')
    member = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='members')
    is_admin = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)

    class Meta:
        db_table = 'group_member'

        verbose_name = 'Group Member'
        verbose_name_plural = 'Group Members'


class GroupPostModel(BaseModel):
    group = models.ForeignKey(GroupModel, on_delete=models.CASCADE, related_name='group_post')
    post = models.TextField()
    files = models.ManyToManyField(FileModel, related_name='files')
    claps = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)

    class Meta:
        db_table = 'group_post'

        verbose_name = 'Group Post'
        verbose_name_plural = 'Group Posts'


class GroupPostClapModel(BaseModel):
    group_post = models.ForeignKey(GroupPostModel, on_delete=models.CASCADE, related_name='group_post_clap')

    class Meta:
        db_table = 'group_post_clap'

        verbose_name = 'Group Post Clap'
        verbose_name_plural = 'Group Post Claps'


class GroupPostCommentModel(BaseModel):
    group_post = models.ForeignKey(GroupPostModel, on_delete=models.CASCADE, related_name='group_post_comment')
    comment = models.TextField()
    file = models.ForeignKey(FileModel, on_delete=models.CASCADE, null=True, blank=True, related_name='comment_file')

    class Meta:
        db_table = 'group_post_comment'

        verbose_name = 'Group Post Comment'
        verbose_name_plural = 'Group Post Comments'

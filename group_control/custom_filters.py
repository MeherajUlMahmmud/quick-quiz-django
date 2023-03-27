from django_filters import CharFilter, DateFromToRangeFilter
from django_filters.rest_framework import FilterSet, ChoiceFilter

from common.choices import GroupMemberRequestStatus
from common.custom_widgets import CustomDateRangeFilterWidget
from group_control.models import GroupModel, GroupMemberRequestModel, GroupMemberModel, GroupPostModel, \
    GroupPostClapModel, GroupPostCommentModel


class GroupModelFilter(FilterSet):
    name = CharFilter(field_name="name", label="Name", lookup_expr='icontains')
    created_by = CharFilter(field_name="created_by", label="Created By")

    class Meta:
        model = GroupModel
        fields = [
            'name',
            'created_by',
        ]


class GroupMemberRequestModelFilter(FilterSet):
    group = CharFilter(field_name="group", label="Group")
    created_by = CharFilter(field_name="created_by", label="Created By")
    status = ChoiceFilter(field_name="status", label="Status", choices=GroupMemberRequestStatus.choices)
    accepted_by = CharFilter(field_name="accepted_by", label="Accepted By")
    rejected_by = CharFilter(field_name="rejected_by", label="Rejected By")
    created_at = DateFromToRangeFilter(
        field_name="created_at", label="Created At",
        widget=CustomDateRangeFilterWidget()
    )

    class Meta:
        model = GroupMemberRequestModel
        fields = [
            'group',
            'created_by',
            'status',
            'accepted_by',
            'rejected_by',
            'created_at',
        ]


class GroupMemberModelFilter(FilterSet):
    group = CharFilter(field_name="group", label="Group")
    user = CharFilter(field_name="user", label="User")
    is_admin = ChoiceFilter(field_name="is_admin", label="Is Admin",
                            choices=((True, 'Yes'), (False, 'No')))
    is_moderator = ChoiceFilter(field_name="is_moderator", label="Is Moderator",
                                choices=((True, 'Yes'), (False, 'No')))

    class Meta:
        model = GroupMemberModel
        fields = [
            'group',
            'user',
            'is_admin',
            'is_moderator',
        ]


class GroupPostModelFilter(FilterSet):
    group = CharFilter(field_name="group", label="Group")
    created_by = CharFilter(field_name="created_by", label="Created By")
    created_at = DateFromToRangeFilter(
        field_name="created_at", label="Created At",
        widget=CustomDateRangeFilterWidget()
    )

    class Meta:
        model = GroupPostModel
        fields = [
            'group',
            'created_by',
            'created_at',
        ]


class GroupPostClapModelFilter(FilterSet):
    group_post = CharFilter(field_name="group_post", label="Group Post")
    created_by = CharFilter(field_name="created_by", label="Created By")
    created_at = DateFromToRangeFilter(
        field_name="created_at", label="Created At",
        widget=CustomDateRangeFilterWidget()
    )

    class Meta:
        model = GroupPostClapModel
        fields = [
            'group_post',
            'created_by',
            'created_at',
        ]


class GroupPostCommentModelFilter(FilterSet):
    group_post = CharFilter(field_name="group_post", label="Group Post")
    created_by = CharFilter(field_name="created_by", label="Created By")
    created_at = DateFromToRangeFilter(
        field_name="created_at", label="Created At",
        widget=CustomDateRangeFilterWidget()
    )

    class Meta:
        model = GroupPostCommentModel
        fields = [
            'group_post',
            'created_by',
            'created_at',
        ]

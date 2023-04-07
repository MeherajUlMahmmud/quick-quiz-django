from django.forms import TextInput
from django_filters import CharFilter, DateFromToRangeFilter
from django_filters.rest_framework import FilterSet

from common.custom_widgets import CustomDateRangeFilterWidget
from group_control.models import GroupPostClapModel, GroupPostCommentModel


class GroupPostClapModelFilter(FilterSet):
    group_post = CharFilter(
        field_name="group_post", label="Group Post ID",
        widget=TextInput(attrs={'placeholder': 'Group Post ID', 'class': 'form-control'}),
    )
    created_by = CharFilter(
        field_name="created_by", label="Created By (ID)",
        widget=TextInput(attrs={'placeholder': 'Created By', 'class': 'form-control'}),
    )
    created_at = DateFromToRangeFilter(
        field_name="created_at", label="Created At",
        widget=CustomDateRangeFilterWidget(attrs={'placeholder': 'YYYY-MM-DD', 'class': 'form-control'}),
    )

    class Meta:
        model = GroupPostClapModel
        fields = [
            'group_post',
            'created_by',
            'created_at',
        ]


class GroupPostCommentModelFilter(FilterSet):
    group_post = CharFilter(
        field_name="group_post", label="Group Post ID",
        widget=TextInput(attrs={'placeholder': 'Group Post ID', 'class': 'form-control'}),
    )
    created_by = CharFilter(
        field_name="created_by", label="Created By (ID)",
        widget=TextInput(attrs={'placeholder': 'Created By', 'class': 'form-control'}),
    )
    created_at = DateFromToRangeFilter(
        field_name="created_at", label="Created At",
        widget=CustomDateRangeFilterWidget(attrs={'placeholder': 'YYYY-MM-DD', 'class': 'form-control'}),
    )

    class Meta:
        model = GroupPostCommentModel
        fields = [
            'group_post',
            'created_by',
            'created_at',
        ]

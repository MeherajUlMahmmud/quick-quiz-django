from django.forms import TextInput
from django_filters import CharFilter, DateFromToRangeFilter
from django_filters.rest_framework import FilterSet

from common.custom_widgets import CustomDateRangeFilterWidget
from group_control.models import GroupPostModel


class GroupPostModelFilter(FilterSet):
    group = CharFilter(
        field_name="group", label="Group ID",
        widget=TextInput(attrs={'placeholder': 'Group ID', 'class': 'form-control'}),
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
        model = GroupPostModel
        fields = [
            'group',
            'created_by',
            'created_at',
        ]

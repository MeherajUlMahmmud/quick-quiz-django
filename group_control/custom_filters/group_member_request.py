from django.forms import TextInput
from django_filters import CharFilter, DateFromToRangeFilter
from django_filters.rest_framework import FilterSet, ChoiceFilter

from common.choices import GroupMemberRequestStatus
from common.custom_widgets import CustomDateRangeFilterWidget
from group_control.models import GroupMemberRequestModel


class GroupMemberRequestModelFilter(FilterSet):
    group = CharFilter(
        field_name="group", label="Group ID",
        widget=TextInput(attrs={'placeholder': 'Group ID', 'class': 'form-control'}),
    )
    created_by = CharFilter(
        field_name="created_by", label="Created By (ID)",
        widget=TextInput(attrs={'placeholder': 'Created By (ID)', 'class': 'form-control'}),
    )
    status = ChoiceFilter(field_name="status", label="Status", choices=GroupMemberRequestStatus.choices)
    accepted_by = CharFilter(
        field_name="accepted_by", label="Accepted By",
        widget=TextInput(attrs={'placeholder': 'Accepted By', 'class': 'form-control'}),
    )
    rejected_by = CharFilter(
        field_name="rejected_by", label="Rejected By",
        widget=TextInput(attrs={'placeholder': 'Rejected By', 'class': 'form-control'}),
    )
    created_at = DateFromToRangeFilter(
        field_name="created_at", label="Created At",
        widget=CustomDateRangeFilterWidget(attrs={'placeholder': 'YYYY-MM-DD', 'class': 'form-control'}),
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

from django.forms import TextInput
from django_filters.rest_framework import FilterSet, CharFilter, ChoiceFilter, DateFromToRangeFilter

from common.choices import IssueStatus
from common.custom_widgets import CustomDateRangeFilterWidget
from utility_control.models import IssueModel


class IssueModelFilter(FilterSet):
    title = CharFilter(
        field_name="title", label="Title", lookup_expr='icontains',
        widget=TextInput(attrs={'placeholder': 'Title', 'class': 'form-control'}),
    )
    description = CharFilter(
        field_name="description", label="Description", lookup_expr='icontains',
        widget=TextInput(attrs={'placeholder': 'Description', 'class': 'form-control'}),
    )
    status = ChoiceFilter(
        field_name="status", label="Status", choices=IssueStatus.choices
    )
    created_at = DateFromToRangeFilter(
        field_name="created_at", label="Created At",
        widget=CustomDateRangeFilterWidget(attrs={'placeholder': 'YYYY-MM-DD'}),
    )

    class Meta:
        model = IssueModel
        fields = [
            'title',
            'description',
            'status',
            'created_at',
        ]

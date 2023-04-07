from django.forms import TextInput
from django_filters import CharFilter, DateFromToRangeFilter
from django_filters.rest_framework import FilterSet, ChoiceFilter

from common.choices import FeedbackSource
from common.custom_widgets import CustomDateRangeFilterWidget
from utility_control.models import FeedbackModel


class FeedbackModelFilter(FilterSet):
    name = CharFilter(
        field_name="name", label="User's Name", lookup_expr='icontains',
        widget=TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}),
    )
    message = CharFilter(
        field_name="message", label="Message", lookup_expr='icontains',
        widget=TextInput(attrs={'placeholder': 'Message', 'class': 'form-control'}),
    )
    source = ChoiceFilter(
        field_name="source", label="Source", choices=FeedbackSource.choices
    )
    created_at = DateFromToRangeFilter(
        field_name="created_at", label="Created At",
        widget=CustomDateRangeFilterWidget(attrs={'placeholder': 'YYYY-MM-DD'}),
    )

    class Meta:
        model = FeedbackModel
        fields = [
            'name',
            'message',
            'source',
            'created_at',
        ]

from django_filters import CharFilter, DateFromToRangeFilter
from django_filters.rest_framework import FilterSet, ChoiceFilter

from common.custom_widgets import CustomDateRangeFilterWidget
from common.choices import FeedbackSource
from utility_control.models import FeedbackModel


class FeedbackModelFilter(FilterSet):
    name = CharFilter(field_name="name", label="Name", lookup_expr='icontains')
    message = CharFilter(field_name="message", label="Message", lookup_expr='icontains')
    source = ChoiceFilter(
        field_name="source", label="Source", choices=FeedbackSource.choices
    )
    created_at = DateFromToRangeFilter(
        field_name="created_at", label="Created At", widget=CustomDateRangeFilterWidget()
    )

    class Meta:
        model = FeedbackModel
        fields = [
            'name',
            'message',
            'source',
            'created_at',
        ]

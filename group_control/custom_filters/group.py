from django.forms import TextInput
from django_filters import CharFilter
from django_filters.rest_framework import FilterSet

from group_control.models import GroupModel


class GroupModelFilter(FilterSet):
    name = CharFilter(
        field_name="name", label="Group Name", lookup_expr='icontains',
        widget=TextInput(attrs={'placeholder': 'Group Name', 'class': 'form-control'}),
    )
    created_by = CharFilter(
        field_name="created_by", label="Created By (ID)",
        widget=TextInput(attrs={'placeholder': 'Created By (ID)', 'class': 'form-control'}),
    )

    class Meta:
        model = GroupModel
        fields = [
            'name',
            'created_by',
        ]

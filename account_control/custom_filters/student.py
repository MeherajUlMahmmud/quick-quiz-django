from django.forms import TextInput
from django_filters import CharFilter
from django_filters.rest_framework import FilterSet

from account_control.models import StudentModel


class StudentModelFilter(FilterSet):
    user = CharFilter(
        field_name="user", label="User ID",
        widget=TextInput(attrs={'placeholder': 'User ID', 'class': 'form-control'}),
    )

    class Meta:
        model = StudentModel
        fields = [
            'user',
        ]

from django.forms import TextInput
from django_filters import CharFilter
from django_filters.rest_framework import FilterSet, ChoiceFilter

from group_control.models import GroupMemberModel


class GroupMemberModelFilter(FilterSet):
    group = CharFilter(
        field_name="group", label="Group ID",
        widget=TextInput(attrs={'placeholder': 'Group ID', 'class': 'form-control'}),
    )
    user = CharFilter(
        field_name="user", label="User ID",
        widget=TextInput(attrs={'placeholder': 'User ID', 'class': 'form-control'}),
    )
    is_admin = ChoiceFilter(
        field_name="is_admin", label="Is Admin",
        choices=((True, 'Yes'), (False, 'No')),
        widget=TextInput(attrs={'placeholder': 'Is Admin', 'class': 'form-control'})
    )
    is_moderator = ChoiceFilter(
        field_name="is_moderator", label="Is Moderator",
        choices=((True, 'Yes'), (False, 'No')),
        widget=TextInput(attrs={'placeholder': 'Is Moderator', 'class': 'form-control'})
    )

    class Meta:
        model = GroupMemberModel
        fields = [
            'group',
            'user',
            'is_admin',
            'is_moderator',
        ]

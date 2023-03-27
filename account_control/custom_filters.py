from django_filters import CharFilter
from django_filters.rest_framework import FilterSet, ChoiceFilter, DateTimeFromToRangeFilter

from account_control.models import UserModel


class UserModelFilter(FilterSet):
    username = CharFilter(field_name="username", label="Username", lookup_expr='icontains')
    email = CharFilter(field_name="email", label="Email", lookup_expr='icontains')
    name = CharFilter(field_name="first_name", label="First Name", lookup_expr='icontains')
    is_student = ChoiceFilter(
        field_name="is_student", label="Is Student",
        choices=((True, 'Yes'), (False, 'No'))
    )
    is_teacher = ChoiceFilter(
        field_name="is_teacher", label="Is Teacher",
        choices=((True, 'Yes'), (False, 'No'))
    )
    is_active = ChoiceFilter(
        field_name="is_active", label="Is Active",
        choices=((True, 'Yes'), (False, 'No'))
    )
    is_staff = ChoiceFilter(
        field_name="is_staff", label="Is Staff",
        choices=((True, 'Yes'), (False, 'No'))
    )
    is_admin = ChoiceFilter(
        field_name="is_admin", label="Is Admin",
        choices=((True, 'Yes'), (False, 'No'))
    )
    is_superuser = ChoiceFilter(
        field_name="is_superuser", label="Is Superuser",
        choices=((True, 'Yes'), (False, 'No'))
    )

    class Meta:
        model = UserModel
        fields = ['username',
                  'email',
                  'name',
                  'is_student',
                  'is_teacher',
                  'is_active',
                  'is_staff',
                  'is_admin',
                  'is_superuser',
                  ]

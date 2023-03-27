from django.contrib import admin

from account_control.models import UserModel, StudentModel, TeacherModel

admin.site.register(UserModel)
admin.site.register(StudentModel)
admin.site.register(TeacherModel)

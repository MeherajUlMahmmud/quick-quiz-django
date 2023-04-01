from django.db.models.signals import post_save
from django.dispatch import receiver

from account_control.models import UserModel, StudentModel, TeacherModel


@receiver(post_save, sender=UserModel, dispatch_uid="user_post_save")
def create_student_or_teacher(sender, instance, created, **kwargs):
    if created:
        if instance.is_student:
            StudentModel.objects.create(user=instance)
        if instance.is_teacher:
            TeacherModel.objects.create(user=instance)

#         send verification email

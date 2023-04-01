from django.db.models.signals import post_save
from django.dispatch import receiver

from group_control.models import GroupModel, GroupMemberModel


@receiver(post_save, sender=GroupModel, dispatch_uid="group_post_save")
def add_member(sender, instance, created, **kwargs):
    if created:
        GroupMemberModel.objects.create(group=instance, member=instance.created_by, is_admin=True)
        instance.total_members = 1
        instance.save(update_fields=['total_members'])

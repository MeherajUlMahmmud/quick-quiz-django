from django.db import models


class GroupMemberRequestStatus(models.TextChoices):
    PENDING = "Pending", "Pending"
    ACCEPTED = "Accepted", "Accepted"
    REJECTED = "Rejected", "Rejected"


class FeedbackSource(models.TextChoices):
    WEBSITE = "Website", "Website"
    APP = "App", "App"

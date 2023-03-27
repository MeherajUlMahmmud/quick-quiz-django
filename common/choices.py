from django.db import models


class GroupMemberRequestStatus(models.TextChoices):
    PENDING = "Pending", "Pending"
    ACCEPTED = "Accepted", "Accepted"
    REJECTED = "Rejected", "Rejected"


class PaymentStatus(models.TextChoices):
    PENDING = "Pending", "Pending"
    SUCCESS = "Success", "Success"
    FAILED = "Failed", "Failed"


class FeedbackSource(models.TextChoices):
    WEBSITE = "Website", "Website"
    APP = "App", "App"

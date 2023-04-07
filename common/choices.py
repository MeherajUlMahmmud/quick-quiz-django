from django.db import models


class ExamType(models.TextChoices):
    MCQ = "MCQ", "Multiple Choice"
    TF = "TF", "True-False"
    FITB = "FITB", "Fill in the Blank"


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


class IssueStatus(models.TextChoices):
    PENDING = "Pending", "Pending"
    WORKING = "Working", "Working"
    FIXED = "Fixed", "Fixed"

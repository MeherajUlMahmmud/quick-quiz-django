from django.contrib.auth.backends import UserModel
from django.db import models

from common.choices import PaymentStatus
from common.models import BaseModel


class PackageModel(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    time_unit = models.CharField(max_length=100, null=True, blank=True)
    time_value = models.IntegerField(null=True, blank=True)
    features = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'package'
        verbose_name = 'Package'
        verbose_name_plural = 'Packages'

    def __str__(self):
        return self.name


class SubscriptionModel(BaseModel):
    package = models.ForeignKey(PackageModel, on_delete=models.RESTRICT, related_name='subscriptions')
    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT, related_name='subscriptions')
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        db_table = 'subscription'
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'

    def __str__(self):
        return self.package.name


class SubscriptionPaymentModel(BaseModel):
    subscription = models.ForeignKey(SubscriptionModel, on_delete=models.RESTRICT, related_name='payments')
    payment_date = models.DateTimeField(null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)
    payment_method = models.CharField(max_length=100, null=True, blank=True)
    payment_status = models.CharField(max_length=100, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)

    class Meta:
        ordering = ['-created_at']
        db_table = 'subscription_payment'
        verbose_name = 'Subscription Payment'
        verbose_name_plural = 'Subscription Payments'

    def __str__(self):
        return self.subscription.package.name

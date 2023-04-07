# Generated by Django 4.1.7 on 2023-04-07 06:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscription_control', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionmodel',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='subscriptions', to='subscription_control.packagemodel'),
        ),
        migrations.AlterField(
            model_name='subscriptionmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='subscriptions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='subscriptionpaymentmodel',
            name='subscription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='payments', to='subscription_control.subscriptionmodel'),
        ),
    ]
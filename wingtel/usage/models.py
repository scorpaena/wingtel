from django.db import models

from wingtel.sprint_subscriptions.models import SprintSubscription


class DataUsageRecord(models.Model):
    """Raw data usage record for a subscription"""

    subscription = models.ForeignKey(
        SprintSubscription, null=True, on_delete=models.PROTECT
    )
    price = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    usage_date = models.DateTimeField(null=False)
    kilobytes_used = models.IntegerField(null=False)


class VoiceUsageRecord(models.Model):
    """Raw voice usage record for a subscription"""

    subscription = models.ForeignKey(
        SprintSubscription, null=True, on_delete=models.PROTECT
    )
    price = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    usage_date = models.DateTimeField(null=False)
    seconds_used = models.IntegerField(null=False)

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


class UsageMetrics(models.Model):

    id = models.BigIntegerField(primary_key=True)
    date = models.DateField(null=False)
    subscription = models.ForeignKey(SprintSubscription, on_delete=models.DO_NOTHING)
    kilobytes_price = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    kilobytes_used = models.IntegerField(null=False)
    seconds_price = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    seconds_used = models.IntegerField(null=False)

    class Meta:

        managed = False
        db_table = "usage_metrics"

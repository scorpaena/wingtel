from django.db import models
from wingtel.sprint_subscriptions.models import SprintSubscription


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

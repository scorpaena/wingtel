import django_filters as filters
from .models import UsageMetrics

class UsageMetricsPriceLimitFilter(filters.FilterSet):

    price_limit = filters.NumberFilter(name='kilobytes_price', lookup_type='gte')

    class Meta:
        model = UsageMetrics
        fields = [
            'kilobytes_price',
            'seconds_price',
            'price_limit',
        ]
        # fields = {
        #     'kilobytes_price': ['gte',],
        #     'seconds_price': ['gte',],
        # }

    # id = models.BigIntegerField(primary_key=True)
    # date = models.DateField(null=False)
    # subscription = models.ForeignKey(SprintSubscription, on_delete=models.DO_NOTHING)
    # kilobytes_price = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    # kilobytes_used = models.IntegerField(null=False)
    # seconds_price = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    # seconds_used = models.IntegerField(null=False)
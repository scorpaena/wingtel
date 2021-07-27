from django_filters import rest_framework as filters
from django.db.models import Q, Sum
from .models import UsageMetrics


class UsageMetricsPriceLimitFilter(filters.FilterSet):

    price = filters.NumberFilter(field_name="price", method="price_limit")

    def price_limit(self, queryset, name, value):
        return queryset.filter(
            Q(kilobytes_price__gte=value) | Q(seconds_price__gte=value)
        )

    class Meta:
        model = UsageMetrics
        fields = [
            "price",
        ]


class UsageMetricsByIdAndTypeFilter(filters.FilterSet):

    usage_type = filters.CharFilter(field_name="usage_type", method="by_usage_type")
    date_from = filters.DateFilter(field_name="date", lookup_expr="gte")
    date_to = filters.DateFilter(field_name="date", lookup_expr="lt")

    def by_usage_type(self, queryset, name, value):
        if value == "data":
            return queryset.values("subscription_id").annotate(
                kilobytes_total_price=Sum("kilobytes_price")
            )
        elif value == "voice":
            return queryset.values("subscription_id").annotate(
                seconds_total_price=Sum("seconds_price")
            )
        else:
            return queryset

    class Meta:
        model = UsageMetrics
        fields = ["usage_type", "date_from", "date_to"]

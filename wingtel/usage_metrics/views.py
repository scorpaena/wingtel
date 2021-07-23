from django.db.models import Q, Sum
from rest_framework import generics
from .models import UsageMetrics
from .serializers import (
    UsageMetricsSerializer,
    UsageMetricsPriceLimitSerializer,
    UsageDataMetricsByPeriodSerializer,
    UsageVoiceMetricsByPeriodSerializer,
)


class UsageMetricsView(generics.ListAPIView):
    queryset = UsageMetrics.objects.all()
    serializer_class = UsageMetricsSerializer


class UsageMetricsPriceLimitView(generics.ListAPIView):
    serializer_class = UsageMetricsPriceLimitSerializer

    def get_queryset(self):
        price = self.kwargs["price"]
        return UsageMetrics.objects.filter(
            Q(kilobytes_price__gte=price) | Q(seconds_price__gte=price)
        )


class UsageMetricsByIdAndTypeView(generics.ListAPIView):
    def get_usage_type(self):
        return self.kwargs["usage_type"]

    def get_queryset(self):
        usage_type = self.get_usage_type()
        date_from = self.kwargs["date_from"]
        date_to = self.kwargs["date_to"]
        queryset = UsageMetrics.objects.filter(
            Q(date__gte=date_from) & Q(date__lt=date_to)
        )
        if usage_type == "data":
            return queryset.values("subscription_id").annotate(
                kilobytes_total_price=Sum("kilobytes_price")
            )
        elif usage_type == "voice":
            return queryset.values("subscription_id").annotate(
                seconds_total_price=Sum("seconds_price")
            )
        else:
            return queryset

    def get_serializer_class(self):
        usage_type = self.get_usage_type()
        if usage_type == "data":
            return UsageDataMetricsByPeriodSerializer
        elif usage_type == "voice":
            return UsageVoiceMetricsByPeriodSerializer
        else:
            return UsageMetricsSerializer

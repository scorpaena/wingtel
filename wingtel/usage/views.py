from django.db.models import Q, Sum
from rest_framework import generics
from .models import UsageMetrics
from .serializers import (
    UsageMetricsSerializer,
    UsageMetricsPriceLimitSerializer,
    UsageDataMetricsByPeriodSerializer,
    UsageVoiceMetricsByPeriodSerializer,
)
from .filters import UsageMetricsPriceLimitFilter, UsageMetricsByIdAndTypeFilter


class UsageMetricsView(generics.ListAPIView):
    queryset = UsageMetrics.objects.all()
    serializer_class = UsageMetricsSerializer


class UsageMetricsPriceLimitView(generics.ListAPIView):
    queryset = UsageMetrics.objects.all()
    serializer_class = UsageMetricsPriceLimitSerializer
    filterset_class = UsageMetricsPriceLimitFilter


class UsageMetricsByIdAndTypeView(generics.ListAPIView):
    queryset = UsageMetrics.objects.all()
    filterset_class = UsageMetricsByIdAndTypeFilter

    def get_usage_type(self):
        return self.request.GET["usage_type"]

    def get_serializer_class(self):
        usage_type = self.get_usage_type()
        if usage_type == "data":
            return UsageDataMetricsByPeriodSerializer
        elif usage_type == "voice":
            return UsageVoiceMetricsByPeriodSerializer
        else:
            return UsageMetricsSerializer

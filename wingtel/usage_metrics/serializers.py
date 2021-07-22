from rest_framework import serializers
from .models import UsageMetrics


class UsageMetricsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsageMetrics
        fields = [
            "date",
            "subscription_id",
            "kilobytes_price",
            "kilobytes_used",
            "seconds_price",
            "seconds_used",
        ]
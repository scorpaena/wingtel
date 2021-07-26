from rest_framework import serializers
from .models import UsageMetrics


class UsageMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsageMetrics
        fields = [
            "id",
            "date",
            "subscription_id",
            "kilobytes_price",
            "kilobytes_used",
            "seconds_price",
            "seconds_used",
        ]


class UsageMetricsPriceLimitSerializer(serializers.ModelSerializer):

    exceeds_kilobytes_price_by = serializers.SerializerMethodField()
    exceeds_seconds_price_by = serializers.SerializerMethodField()

    class Meta:
        model = UsageMetrics
        fields = [
            "id",
            "subscription_id",
            "kilobytes_price",
            "exceeds_kilobytes_price_by",
            "seconds_price",
            "exceeds_seconds_price_by",
        ]
    
    def get_price_from_url(self):
        return int(self.context["request"].GET["price"])

    def get_exceeds_kilobytes_price_by(self, obj):
        try:
            price_delta = self.get_price_from_url() - obj.kilobytes_price
        except TypeError:
            return None
        return price_delta

    def get_exceeds_seconds_price_by(self, obj):
        try:
            price_delta = self.get_price_from_url() - obj.seconds_price
        except TypeError:
            return None
        return price_delta


class UsageDataMetricsByPeriodSerializer(serializers.ModelSerializer):

    kilobytes_total_price = serializers.DecimalField(decimal_places=2, max_digits=8)

    class Meta:
        model = UsageMetrics
        fields = [
            "subscription_id",
            "kilobytes_total_price",
        ]


class UsageVoiceMetricsByPeriodSerializer(serializers.ModelSerializer):

    seconds_total_price = serializers.DecimalField(decimal_places=2, max_digits=8)

    class Meta:
        model = UsageMetrics
        fields = [
            "subscription_id",
            "seconds_total_price",
        ]

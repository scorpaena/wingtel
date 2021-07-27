import pytest
from datetime import date
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from wingtel.sprint_subscriptions.models import SprintSubscription
from wingtel.usage.models import DataUsageRecord, VoiceUsageRecord, UsageMetrics
from wingtel.usage.serializers import UsageMetricsPriceLimitSerializer

today = date.today()


@pytest.fixture
def user(db):
    return User.objects.create(username="foo", password="bar123$%")


@pytest.fixture
def subscription(db, user):
    return SprintSubscription.objects.create(user=user)


@pytest.fixture
def datausage(db, subscription):
    return DataUsageRecord.objects.create(
        subscription=subscription,
        usage_date=today,
        kilobytes_used=10,
        price=10,
    )


@pytest.fixture
def voiceusage(db, subscription):
    return VoiceUsageRecord.objects.create(
        subscription=subscription,
        usage_date=today,
        seconds_used=10,
        price=15,
    )


@pytest.fixture
def factory():
    return APIRequestFactory()


def test_serializer_context(factory, datausage, voiceusage):
    obj = UsageMetrics.objects.last()
    request = factory.get("/usage_metrics/price_limit/?price=5")
    serializer = UsageMetricsPriceLimitSerializer(context={"request": request})
    assert serializer.get_price_from_url() == 5
    assert serializer.get_exceeds_kilobytes_price_by(obj) == -5
    assert serializer.get_exceeds_seconds_price_by(obj) == -10

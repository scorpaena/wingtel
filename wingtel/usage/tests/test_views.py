import pytest
from datetime import date, timedelta
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from wingtel.sprint_subscriptions.models import SprintSubscription
from wingtel.usage.models import DataUsageRecord, VoiceUsageRecord, UsageMetrics

today = date.today()
tomorrow = today + timedelta(days=1)


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
        price=10,
    )


@pytest.fixture
def client(user):
    return APIClient()


def test_usage_metrics_view(client, datausage, voiceusage):
    request = client.get("/usage_metrics/")
    assert request.status_code == 200
    assert request.data["count"] == 1


def test_usage_metrics_price_limit_view(client, datausage, voiceusage):
    request = client.get("/usage_metrics/price_limit/?price=10")
    assert request.status_code == 200
    assert request.data["count"] == 1


def test_usage_metrics_price_limit_view_empty(client, datausage, voiceusage):
    request = client.get("/usage_metrics/price_limit/?price=20")
    assert request.status_code == 200
    assert request.data["count"] == 0


def test_usage_metrics_by_type_data_view(client, datausage, voiceusage):
    request = client.get("/usage_metrics/by_usage_type/?usage_type=data")
    assert request.status_code == 200
    assert request.data["count"] == 1


def test_usage_metrics_by_type_voice_view(client, datausage, voiceusage):
    request = client.get("/usage_metrics/by_usage_type/?usage_type=voice")
    assert request.status_code == 200
    assert request.data["count"] == 1


def test_usage_metrics_by_type_voice_date_view(client, datausage, voiceusage):
    request = client.get(
        f"/usage_metrics/by_usage_type/?usage_type=voice&date_from={today}&date_to={tomorrow}"
    )
    assert request.status_code == 200
    assert request.data["count"] == 1


def test_usage_metrics_by_type_voice_date_neg_view(client, datausage, voiceusage):
    request = client.get(
        f"/usage_metrics/by_usage_type/?usage_type=voice&date_from={today}&date_to={today}"
    )
    assert request.status_code == 200
    assert request.data["count"] == 0

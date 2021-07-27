import pytest
from datetime import date
from django.contrib.auth.models import User
from wingtel.sprint_subscriptions.models import SprintSubscription
from wingtel.usage.models import DataUsageRecord, VoiceUsageRecord, UsageMetrics

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
    )


@pytest.fixture
def voiceusage(db, subscription):
    return VoiceUsageRecord.objects.create(
        subscription=subscription,
        usage_date=today,
        seconds_used=10,
    )


def test_db_is_not_empty(datausage, voiceusage):
    assert User.objects.count() == 1
    assert SprintSubscription.objects.count() == 1
    assert DataUsageRecord.objects.count() == 1
    assert VoiceUsageRecord.objects.count() == 1
    assert UsageMetrics.objects.count() == 1


def test_usage_metrics_model_id_field(datausage, voiceusage):
    usage_metrics = UsageMetrics.objects.last()
    id = usage_metrics._meta.get_field("id").verbose_name
    assert id == "id"


def test_usage_metrics_model_subscription_field(datausage, voiceusage):
    usage_metrics = UsageMetrics.objects.last()
    subscription = usage_metrics._meta.get_field("subscription").verbose_name
    assert subscription == "subscription"


def test_usage_metrics_model_kilobytes_price_field(datausage, voiceusage):
    usage_metrics = UsageMetrics.objects.last()
    kilobytes_price = usage_metrics._meta.get_field("kilobytes_price").verbose_name
    assert kilobytes_price == "kilobytes price"


def test_usage_metrics_model_kilobytes_used_field(datausage, voiceusage):
    usage_metrics = UsageMetrics.objects.last()
    kilobytes_used = usage_metrics._meta.get_field("kilobytes_used").verbose_name
    assert kilobytes_used == "kilobytes used"


def test_usage_metrics_model_seconds_price_field(datausage, voiceusage):
    usage_metrics = UsageMetrics.objects.last()
    seconds_price = usage_metrics._meta.get_field("seconds_price").verbose_name
    assert seconds_price == "seconds price"


def test_usage_metrics_model_seconds_used_field(datausage, voiceusage):
    usage_metrics = UsageMetrics.objects.last()
    seconds_used = usage_metrics._meta.get_field("seconds_used").verbose_name
    assert seconds_used == "seconds used"

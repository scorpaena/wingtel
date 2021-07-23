from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from rest_framework import routers

from wingtel.att_subscriptions.views import ATTSubscriptionViewSet
from wingtel.plans.views import PlanViewSet
from wingtel.purchases.views import PurchaseViewSet
from wingtel.sprint_subscriptions.views import SprintSubscriptionViewSet
from wingtel.usage_metrics.views import (
    UsageMetricsView,
    UsageMetricsPriceLimitView,
    UsageMetricsByIdAndTypeView,
)
from wingtel.usage_metrics.dateconverter import YearMonthDayConverter


router = routers.DefaultRouter()

router.register(r"att_subscriptions", ATTSubscriptionViewSet)
router.register(r"plans", PlanViewSet)
router.register(r"purchases", PurchaseViewSet)
router.register(r"sprint_subscriptions", SprintSubscriptionViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("usage_metrics/", UsageMetricsView.as_view(), name="usage_metrics"),
    path(
        "usage_metrics/price_limit=<int:price>",
        UsageMetricsPriceLimitView.as_view(),
        name="price_limit",
    ),
    path(
        "usage_metrics/usage_type=<usage_type>&date_from=<yyyy-mm-dd:date_from>&date_to=<yyyy-mm-dd:date_to>",
        UsageMetricsByIdAndTypeView.as_view(),
        name="usage_type_by_date",
    ),
    url(r"^api/", include((router.urls, "api"), namespace="api")),
]

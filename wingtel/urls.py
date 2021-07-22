from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from rest_framework import routers

from wingtel.att_subscriptions.views import ATTSubscriptionViewSet
from wingtel.plans.views import PlanViewSet
from wingtel.purchases.views import PurchaseViewSet
from wingtel.sprint_subscriptions.views import SprintSubscriptionViewSet
from wingtel.usage_metrics.views import UsageMetricsView

router = routers.DefaultRouter()

router.register(r'att_subscriptions', ATTSubscriptionViewSet)
router.register(r'plans', PlanViewSet)
router.register(r'purchases', PurchaseViewSet)
router.register(r'sprint_subscriptions', SprintSubscriptionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usage-metrics/', UsageMetricsView.as_view(), name='usage_metrics'),
    url(r'^api/', include((router.urls, 'api'), namespace='api')),
]

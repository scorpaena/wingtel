from django.shortcuts import render
from rest_framework import generics
from .models import UsageMetrics
from .serializers import UsageMetricsSerializer


class UsageMetricsView(generics.ListAPIView):
	queryset = UsageMetrics.objects.all()
	serializer_class = UsageMetricsSerializer

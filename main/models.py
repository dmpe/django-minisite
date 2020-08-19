from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
# from django_prometheus.models import ExportModelOperationsMixin
from rest_framework.authtoken.models import Token

 # ExportModelOperationsMixin('firm_recommendation'), see https://github.com/korfuri/django-prometheus/issues/217
class Firm_Recommendation(
    models.Model
):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    starting_date = models.DateField()
    ending_date = models.DateField()

    POSITIONING = (
        ("Small", "S"),
        ("Mid", "M"),
        ("Large", "L"),
    )
    POSITION = (
        ("Short", "S"),
        ("Long", "L"),
        ("Pair-Trade", "PT"),
    )
    positioning = models.CharField(max_length=10, choices=POSITIONING)
    position = models.CharField(max_length=10, choices=POSITION)

    description = models.CharField(max_length=500)

    PERF = (
        ("DAX", "DAX"),
        ("Sector Europe", "SEC_EUR"),
        ("None (for Pair-Trade)", "NONE"),
    )
    outperformance = models.CharField(max_length=30, choices=PERF)

    TIME_HOR = (
        ("1 Week", "1w"),
        ("2 Weeks", "2w"),
        ("1 Month", "1m"),
        ("3 Month", "3m"),
        ("6 Month", "6m"),
        ("1 Year", "1y"),
    )
    time_horizon = models.CharField(max_length=10, choices=TIME_HOR)
    bloomberg_ticker_1 = models.CharField(max_length=50)
    bloomberg_ticker_2 = models.CharField(
        max_length=50, blank=True, null=True, default=None
    )

    class Meta:
        ordering = ["starting_date"]
        verbose_name_plural = "Recommendations"
        verbose_name = "Recommendation"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

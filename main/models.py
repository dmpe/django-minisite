from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Firm_Recommendation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    starting_date = models.DateField()
    ending_date = models.DateField()

    POSITIONING = (
        ('S', 'Small'),
        ('M', 'Mid'),
        ('L', 'Large'),
    )
    POSITION = (
        ('S', 'Long'),
        ('M', 'Short'),
        ('PT', 'Pair-Trade'),
    )
    positioning = models.CharField(max_length=10, choices=POSITIONING)
    position = models.CharField(max_length=10, choices=POSITION)

    description = models.CharField(max_length=500)

    PERF = (
        ('DAX', 'DAX'),
        ('SEC_EUR', 'Sector Europe'),
        ('NONE', 'None (for Pair-Trade)'),
    )
    outperformance = models.CharField(max_length=10, choices=PERF)

    TIME_HOR = (
        ('1w', '1 Week'),
        ('2w', '2 Weeks'),
        ('1m', '1 Month'),
        ('3m', '3 Month'),
        ('6m', '6 Month'),
        ('1y', '1 Year'),
    )
    time_horizon = models.CharField(max_length=10, choices=TIME_HOR)
    bloomberg_ticker_1 = models.CharField(max_length=50)
    bloomberg_ticker_2 = models.CharField(max_length=50, blank=True, null=True, default = None)


    class Meta:
        ordering = ["starting_date"]
        verbose_name_plural = "Recommendations"
        verbose_name = "Recommendation"

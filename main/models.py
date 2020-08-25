from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token
import uuid


class Firm_Recommendation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # another unique id - potentially to be used later
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)

    class Positioning(models.TextChoices):
        SMALL = "S", _("Small")
        MID = "M", _("Mid")
        LARGE = "L", _("Large")

    class Position(models.TextChoices):
        SHORT = "S", _("Short")
        LONG = "L", _("Long")
        PAIR = "PT", _("Pair-Trade")

    class Time(models.TextChoices):
        ONEWEEK = "1w", _("1 Week")
        TWOWEEKS = "2w", _("2 Weeks")
        ONEMONTH = "1m", _("1 Month")
        THREEMONTHS = "3m", _("3 Month")
        SIXMONTHS = "6m", _("6 Month")
        ONEYEAR = "1y", _("1 Year")

    class Performance(models.TextChoices):
        DAX = "DAX", _("DAX")
        SEC_EUR = "SEC_EUR", _("Sector Europe")
        NONE = "NONE", _("None (for Pair-Trade)")

    # Automatically set the field to now every time the object is saved. Useful for “last-modified” timestamps.
    pub_date = models.DateTimeField('date_published', auto_now=True)
    starting_date = models.DateField()
    ending_date = models.DateField()

    positioning = models.CharField(max_length=10, choices=Positioning.choices, default=Positioning.SMALL)
    position = models.CharField(max_length=10, choices=Position.choices, default=Position.SHORT)

    description = models.CharField(max_length=500)

    outperformance = models.CharField(max_length=30, choices=Performance.choices, default=Performance.DAX)

    time_horizon = models.CharField(max_length=10, choices=Time.choices, default=Time.ONEWEEK)
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

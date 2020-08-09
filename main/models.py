from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Firm_Recommendation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)



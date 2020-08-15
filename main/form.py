from django import forms
from rest_framework import fields
from . import models

class RecommendationSingleRowForm(forms.ModelForm):
    class Meta:
        model = models.Firm_Recommendation
        fields = "__all__"

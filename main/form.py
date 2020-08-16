from django import forms
from rest_framework import fields

from . import models


class RecommendationSingleRowEditForm(forms.ModelForm):
    class Meta:
        model = models.Firm_Recommendation
        fields = "__all__"

class RecommendationSingleRowCreateForm(forms.ModelForm):
    class Meta:
        model = models.Firm_Recommendation
        fields = "__all__"

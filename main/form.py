from django import forms
from . import models

class RecommendationSingleRowForm(forms.ModelForm):
    class Meta:
        model = models.Firm_Recommendation

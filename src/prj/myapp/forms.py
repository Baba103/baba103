from django import forms
from .models import PointOfSale, Commune

class PointOfSaleForm(forms.ModelForm):
    commune = forms.ModelChoiceField(
        queryset=Commune.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = PointOfSale
        fields = ['nom', 'type', 'gps_lat', 'gps_lon', 'commune']

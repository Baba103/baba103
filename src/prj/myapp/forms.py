from django import forms
from .models import PointOfSale, Commune

class PointOfSaleForm(forms.ModelForm):
    commune = forms.ModelChoiceField(
        queryset=Commune.objects.all(),  # ✅ Récupération directe depuis la BDD
        empty_label="Sélectionnez une Commune",  # ✅ Option par défaut
        widget=forms.Select(attrs={'class': 'form-control'})  # ✅ Ajout de classes Bootstrap
    )

    class Meta:
        model = PointOfSale
        fields = '__all__'

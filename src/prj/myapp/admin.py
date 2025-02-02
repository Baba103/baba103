from django.contrib import admin
from .models import Moughataa, Commune, Product, PointOfSale, ProductPrice, ProductType, CartProduct, Cart

from import_export.admin import ExportMixin
from import_export import resources
from .models import Wilaya  # Import uniquement les modèles nécessaires
#from .models import Inpc


# Définir une ressource pour Wilaya
class WilayaResource(resources.ModelResource):
    class Meta:
        model = Wilaya
        fields = ('id', 'code', 'name')  # Spécifiez les champs à exporter/importer
        export_order = ('id', 'code', 'name')  # Ordre des champs

# Enregistrer Wilaya avec les fonctionnalités d'import/export
class WilayaAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = WilayaResource
    list_display = ('code', 'name')
    search_fields = ('name', 'code')

# ✅ Enregistrement unique du modèle Wilaya avec la classe WilayaAdmin
admin.site.register(Wilaya, WilayaAdmin)



# Enregistrer les autres modèles sans fonctionnalités spécifiques
admin.site.register(Moughataa)
admin.site.register(Commune)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(PointOfSale)
admin.site.register(ProductPrice)
admin.site.register(Cart)
admin.site.register(CartProduct)
#admin.site.register(Inpc)

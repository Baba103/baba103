from import_export import resources
from .models import Wilaya

from import_export import resources
from myapp.models import Wilaya

class WilayaResource(resources.ModelResource):
    class Meta:
        model = Wilaya
        exclude = ('id',)  # Exclure l'ID
        import_id_fields = ['code']  # Utiliser "code" comme identifiant unique

from .models import Moughataa

class MoughataaResource(resources.ModelResource):
    class Meta:
        model = Moughataa
        
from import_export import resources
from myapp.models import Commune

class CommuneResource(resources.ModelResource):
    class Meta:
        model = Commune
        exclude = ('id',)  # Exclure l'ID
        import_id_fields = ['nom']  # Utiliser "nom" comme identifiant unique

from .models import PointOfSale

class PointOfSaleResource(resources.ModelResource):
    class Meta:
        model = PointOfSale
       
from import_export import resources
from .models import ProductType

class ProductTypeResource(resources.ModelResource):
    class Meta:
        model = ProductType
       

from import_export import resources
from .models import Product

from import_export import resources
from .models import Product

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product


from import_export import resources
from .models import ProductPrice

class ProductPriceResource(resources.ModelResource):
    class Meta:
        model = ProductPrice

from import_export import resources
from .models import Cart

class CartResource(resources.ModelResource):
    class Meta:
        model = Cart

from import_export import resources
from .models import CartProduct

class CartProductResource(resources.ModelResource):
    class Meta:
        model = CartProduct

from django.contrib import admin
from .models import Wilaya,Moughataa,Commune,Product,PointOfSale,ProductPrice,ProductType,CartProduct



# Register your models here.
admin.site.register(Wilaya)
admin.site.register(Moughataa)
admin.site.register(Commune)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(PointOfSale)
admin.site.register(ProductPrice)

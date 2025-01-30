from django.urls import path
from openpyxl import load_workbook
import openpyxl
from django.urls import path
from .views import InpcListView  # Assurez-vous que cette vue existe
from .views import dashboard_view,get_product_price_data,bar_chart_product_prices,bar_chart_all_products_prices,pie_product_categories

from . import views
from .views import INPCCalculateView  # Import de la vue
from .views import  WilayaListView, WilayaDetailView, WilayaCreateView, WilayaUpdateView, WilayaDeleteView,MoughataaListView, MoughataaDetailView, MoughataaCreateView, MoughataaUpdateView, MoughataaDeleteView, CommuneListView, CommuneDetailView, CommuneCreateView, CommuneUpdateView, CommuneDeleteView, ProductTypeListView, ProductTypeDetailView, ProductTypeCreateView, ProductTypeUpdateView, ProductTypeDeleteView, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, PointOfSaleListView, PointOfSaleDetailView, PointOfSaleCreateView, PointOfSaleUpdateView, PointOfSaleDeleteView, ProductPriceListView, ProductPriceDetailView, ProductPriceCreateView, ProductPriceUpdateView, ProductPriceDeleteView, CartListView, CartDetailView, CartCreateView, CartUpdateView, CartDeleteView, CartProductListView, CartProductDetailView, CartProductCreateView, CartProductUpdateView, CartProductDeleteView, WilayaExportView, WilayaImportView , home
from .views import MoughataaImportView,MoughataaExportView , CommuneImportView, CommuneExportView,PointOfSaleExportView,PointOfSaleImportView,ProductTypeImportView,ProductTypeExportView,ProductExportView,ProductImportView,ProductPriceExportView,ProductPriceImportView,CartExportView,CartImportView,CartProductExportView,CartProductImportView 
urlpatterns = [
    path("", dashboard_view, name="home"),  # 🏠 Redirige l'accueil vers le dashboard
    path("dashboard/", dashboard_view, name="dashboard"),
    #  Routes pour Wilaya
    path('wilayas/', WilayaListView.as_view(), name='wilaya_list'),
    path('wilayas/<int:pk>/', WilayaDetailView.as_view(), name='wilaya_detail'),
    path('wilayas/new/', WilayaCreateView.as_view(), name='wilaya_create'),
    path('wilayas/<int:pk>/edit/', WilayaUpdateView.as_view(), name='wilaya_update'),
    path('wilayas/<int:pk>/delete/', WilayaDeleteView.as_view(), name='wilaya_delete'),
    path('wilayas/export/', WilayaExportView.as_view(), name='wilaya_export'),
    path('wilayas/import/', WilayaImportView.as_view(), name='wilaya_import'),
    
     # ✅ Routes pour Moughataa
    path('moughataas/', MoughataaListView.as_view(), name='moughataa_list'),
    path('moughataas/<int:pk>/', MoughataaDetailView.as_view(), name='moughataa_detail'),
    path('moughataas/new/', MoughataaCreateView.as_view(), name='moughataa_create'),
    path('moughataas/<int:pk>/edit/', MoughataaUpdateView.as_view(), name='moughataa_update'),
    path('moughataas/<int:pk>/delete/', MoughataaDeleteView.as_view(), name='moughataa_delete'),
    path('moughataas/export/', MoughataaExportView.as_view(), name='moughataa_export'),
    path('moughataas/import/', MoughataaImportView.as_view(), name='moughataa_import'),
    # 📍 Routes pour Commune
    path('communes/', CommuneListView.as_view(), name='commune_list'),
    path('communes/<int:pk>/', CommuneDetailView.as_view(), name='commune_detail'),
    path('communes/new/', CommuneCreateView.as_view(), name='commune_create'),
    path('communes/<int:pk>/edit/', CommuneUpdateView.as_view(), name='commune_update'),
    path('communes/<int:pk>/delete/', CommuneDeleteView.as_view(), name='commune_delete'),
       # Autres URLs pour Wilaya et Moughataa
    path('communes/export/', CommuneExportView.as_view(), name='commune_export'),
    path('communes/import/', CommuneImportView.as_view(), name='commune_import'),
    

    # ✅ Routes pour Type de Produit
    path('producttypes/', ProductTypeListView.as_view(), name='producttype_list'),
    path('producttypes/<int:pk>/', ProductTypeDetailView.as_view(), name='producttype_detail'),
    path('producttypes/new/', ProductTypeCreateView.as_view(), name='producttype_create'),
    path('producttypes/<int:pk>/edit/', ProductTypeUpdateView.as_view(), name='producttype_update'),
    path('producttypes/<int:pk>/delete/', ProductTypeDeleteView.as_view(), name='producttype_delete'),
    path('producttypes/export/', ProductTypeExportView.as_view(), name='producttype_export'),
    path('producttypes/import/', ProductTypeImportView.as_view(), name='producttype_import'),


    # ✅ Routes pour Produit
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/new/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/export/', ProductExportView.as_view(), name='product_export'),
    path('products/import/', ProductImportView.as_view(), name='product_import'),

    # ✅ Routes pour Point de Vente
    path('pointofsales/', PointOfSaleListView.as_view(), name='pointofsale_list'),
    path('pointofsales/<int:pk>/', PointOfSaleDetailView.as_view(), name='pointofsale_detail'),
    path('pointofsales/new/', PointOfSaleCreateView.as_view(), name='pointofsale_create'),
    path('pointofsales/<int:pk>/edit/', PointOfSaleUpdateView.as_view(), name='pointofsale_update'),
    path('pointofsales/<int:pk>/delete/', PointOfSaleDeleteView.as_view(), name='pointofsale_delete'),
    path('pointofsales/export/', PointOfSaleExportView.as_view(), name='pointofsale_export'),
    path('pointofsales/import/', PointOfSaleImportView.as_view(), name='pointofsale_import'),


    # ✅ Routes pour Prix des Produits
    path('productprices/', ProductPriceListView.as_view(), name='productprice_list'),
    path('productprices/<int:pk>/', ProductPriceDetailView.as_view(), name='productprice_detail'),
    path('productprices/new/', ProductPriceCreateView.as_view(), name='productprice_create'),
    path('productprices/<int:pk>/edit/', ProductPriceUpdateView.as_view(), name='productprice_update'),
    path('productprices/<int:pk>/delete/', ProductPriceDeleteView.as_view(), name='productprice_delete'),
    path('productprices/export/', ProductPriceExportView.as_view(), name='productprice_export'),
    path('productprices/import/', ProductPriceImportView.as_view(), name='productprice_import'),
    


    
    
        # ✅ Routes pour Panier (Cart)
    path('carts/', CartListView.as_view(), name='cart_list'),
    path('carts/<int:pk>/', CartDetailView.as_view(), name='cart_detail'),
    path('carts/new/', CartCreateView.as_view(), name='cart_create'),
    path('carts/<int:pk>/edit/', CartUpdateView.as_view(), name='cart_update'),
    path('carts/<int:pk>/delete/', CartDeleteView.as_view(), name='cart_delete'),
    path('carts/export/', CartExportView.as_view(), name='cart_export'),
    path('carts/import/', CartImportView.as_view(), name='cart_import'),


    # ✅ Routes pour Produits dans un Panier (CartProduct)
    path('cartproducts/', CartProductListView.as_view(), name='cartproduct_list'),
    path('cartproducts/<int:pk>/', CartProductDetailView.as_view(), name='cartproduct_detail'),
    path('cartproducts/new/', CartProductCreateView.as_view(), name='cartproduct_create'),
    path('cartproducts/<int:pk>/edit/', CartProductUpdateView.as_view(), name='cartproduct_update'),
    path('cartproducts/<int:pk>/delete/', CartProductDeleteView.as_view(), name='cartproduct_delete'),
    path('cartproducts/export/', CartProductExportView.as_view(), name='cartproduct_export'),
    path('cartproducts/import/', CartProductImportView.as_view(), name='cartproduct_import'),
    path('calculate_inpc/', INPCCalculateView.as_view(), name='calculate_inpc'),
    path('inpc/', InpcListView.as_view(), name='inpc_list'),  # Définition de la route pour 'inpc_list'
    #path('price-evolution/<int:product_id>/<int:point_of_sale_id>/', views.price_evolution, name='price_evolution'),
    #path('price-comparison/<int:product_id>/', views.price_comparison, name='price_comparison'),
    path("dashboard/", dashboard_view, name="dashboard"),
    #path("chart-data/", get_chart_data, name="chart_data"),
    path("get-product-price-data/", get_product_price_data, name="get_product_price_data"),
    #path("charts/pie-product-prices/", pie_chart_data, name="pie_product_prices"),
    #path("charts/bar-product-prices/", bar_chart_data, name="bar_product_prices"),
    path("charts/bar-product-prices/", bar_chart_product_prices, name="bar_product_prices"),
    path("charts/bar-all-product-prices/", bar_chart_all_products_prices, name="bar_all_product_prices"),
    #p#ath("charts/pie-product-categories/", pie_chart_product_categories, name="pie_product_categories"),
    path("charts/pie-product-categories/", pie_product_categories, name="pie_product_categories"),







    
]



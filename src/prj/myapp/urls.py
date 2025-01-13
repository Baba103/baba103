from django.urls import path
from . import views
from .views import  WilayaListView, WilayaDetailView, WilayaCreateView, WilayaUpdateView, WilayaDeleteView,MoughataaListView, MoughataaDetailView, MoughataaCreateView, MoughataaUpdateView, MoughataaDeleteView, CommuneListView, CommuneDetailView, CommuneCreateView, CommuneUpdateView, CommuneDeleteView, ProductTypeListView, ProductTypeDetailView, ProductTypeCreateView, ProductTypeUpdateView, ProductTypeDeleteView, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, PointOfSaleListView, PointOfSaleDetailView, PointOfSaleCreateView, PointOfSaleUpdateView, PointOfSaleDeleteView, ProductPriceListView, ProductPriceDetailView, ProductPriceCreateView, ProductPriceUpdateView, ProductPriceDeleteView, home


urlpatterns = [
     path('', views.home, name='home'),  # ✅ Corrige ici
    #  Routes pour Wilaya
    path('wilayas/', WilayaListView.as_view(), name='wilaya_list'),
    path('wilayas/<int:pk>/', WilayaDetailView.as_view(), name='wilaya_detail'),
    path('wilayas/new/', WilayaCreateView.as_view(), name='wilaya_create'),
    path('wilayas/<int:pk>/edit/', WilayaUpdateView.as_view(), name='wilaya_update'),
    path('wilayas/<int:pk>/delete/', WilayaDeleteView.as_view(), name='wilaya_delete'),
    
     # ✅ Routes pour Moughataa
    path('moughataas/', MoughataaListView.as_view(), name='moughataa_list'),
    path('moughataas/<int:pk>/', MoughataaDetailView.as_view(), name='moughataa_detail'),
    path('moughataas/new/', MoughataaCreateView.as_view(), name='moughataa_create'),
    path('moughataas/<int:pk>/edit/', MoughataaUpdateView.as_view(), name='moughataa_update'),
    path('moughataas/<int:pk>/delete/', MoughataaDeleteView.as_view(), name='moughataa_delete'),
    # 📍 Routes pour Commune
    path('communes/', CommuneListView.as_view(), name='commune_list'),
    path('communes/<int:pk>/', CommuneDetailView.as_view(), name='commune_detail'),
    path('communes/new/', CommuneCreateView.as_view(), name='commune_create'),
    path('communes/<int:pk>/edit/', CommuneUpdateView.as_view(), name='commune_update'),
    path('communes/<int:pk>/delete/', CommuneDeleteView.as_view(), name='commune_delete'),
    

    # ✅ Routes pour Type de Produit
    path('producttypes/', ProductTypeListView.as_view(), name='producttype_list'),
    path('producttypes/<int:pk>/', ProductTypeDetailView.as_view(), name='producttype_detail'),
    path('producttypes/new/', ProductTypeCreateView.as_view(), name='producttype_create'),
    path('producttypes/<int:pk>/edit/', ProductTypeUpdateView.as_view(), name='producttype_update'),
    path('producttypes/<int:pk>/delete/', ProductTypeDeleteView.as_view(), name='producttype_delete'),

    # ✅ Routes pour Produit
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/new/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    # ✅ Routes pour Point de Vente
    path('pointofsales/', PointOfSaleListView.as_view(), name='pointofsale_list'),
    path('pointofsales/<int:pk>/', PointOfSaleDetailView.as_view(), name='pointofsale_detail'),
    path('pointofsales/new/', PointOfSaleCreateView.as_view(), name='pointofsale_create'),
    path('pointofsales/<int:pk>/edit/', PointOfSaleUpdateView.as_view(), name='pointofsale_update'),
    path('pointofsales/<int:pk>/delete/', PointOfSaleDeleteView.as_view(), name='pointofsale_delete'),

    # ✅ Routes pour Prix des Produits
    path('productprices/', ProductPriceListView.as_view(), name='productprice_list'),
    path('productprices/<int:pk>/', ProductPriceDetailView.as_view(), name='productprice_detail'),
    path('productprices/new/', ProductPriceCreateView.as_view(), name='productprice_create'),
    path('productprices/<int:pk>/edit/', ProductPriceUpdateView.as_view(), name='productprice_update'),
    path('productprices/<int:pk>/delete/', ProductPriceDeleteView.as_view(), name='productprice_delete'),

 

    
]



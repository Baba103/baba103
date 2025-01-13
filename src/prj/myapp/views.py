from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models.model import Wilaya, Moughataa, Commune, ProductType, Product, PointOfSale, ProductPrice

def home(request):
    return render(request, "home.html")  # ✅ Vérifie que le fichier home.html existe bien

# 📍 Liste des Wilayas
class WilayaListView(ListView):
    model = Wilaya
    template_name = "myapp/wilaya_list.html"  # ✅ Modification ici
    context_object_name = "wilayas"

# 📍 Détails d'une Wilaya
class WilayaDetailView(DetailView):
    model = Wilaya
    template_name = "myapp/wilaya_detail.html"  # ✅ Modification ici
    context_object_name = "wilaya"

# 📍 Ajouter une Wilaya
class WilayaCreateView(CreateView):
    model = Wilaya
    fields = '__all__'
    template_name = "myapp/wilaya_form.html"  # ✅ Modification ici
    success_url = reverse_lazy('wilaya_list')

# 📍 Modifier une Wilaya
class WilayaUpdateView(UpdateView):
    model = Wilaya
    fields = '__all__'
    template_name = "myapp/wilaya_form.html"  # ✅ Modification ici
    success_url = reverse_lazy('wilaya_list')

# 📍 Supprimer une Wilaya
class WilayaDeleteView(DeleteView):
    model = Wilaya
    template_name = "myapp/wilaya_confirm_delete.html"  # ✅ Modification ici
    success_url = reverse_lazy('wilaya_list')

# 📍 Liste des Moughataas
class MoughataaListView(ListView):
    model = Moughataa
    template_name = "myapp/moughataa_list.html"  # ✅ Modification ici
    context_object_name = "moughataas"

# 📍 Détails d'une Moughataa
class MoughataaDetailView(DetailView):
    model = Moughataa
    template_name = "myapp/moughataa_detail.html"  # ✅ Modification ici
    context_object_name = "moughataa"

# 📍 Ajouter une Moughataa
class MoughataaCreateView(CreateView):
    model = Moughataa
    fields = '__all__'
    template_name = "myapp/moughataa_form.html"  # ✅ Modification ici
    success_url = reverse_lazy('moughataa_list')

# 📍 Modifier une Moughataa
class MoughataaUpdateView(UpdateView):
    model = Moughataa
    fields = '__all__'
    template_name = "myapp/moughataa_form.html"  # ✅ Modification ici
    success_url = reverse_lazy('moughataa_list')

# 📍 Supprimer une Moughataa
class MoughataaDeleteView(DeleteView):
    model = Moughataa
    template_name = "myapp/moughataa_confirm_delete.html"  # ✅ Modification ici
    success_url = reverse_lazy('moughataa_list')

# 📍 Liste des Communes
class CommuneListView(ListView):
    model = Commune
    template_name = "myapp/commune_list.html"
    context_object_name = "communes"

# 📍 Détails d'une Commune
class CommuneDetailView(DetailView):
    model = Commune
    template_name = "myapp/commune_detail.html"
    context_object_name = "commune"

# 📍 Ajouter une Commune
class CommuneCreateView(CreateView):
    model = Commune
    fields = '__all__'
    template_name = "myapp/commune_form.html"
    success_url = reverse_lazy('commune_list')

# 📍 Modifier une Commune
class CommuneUpdateView(UpdateView):
    model = Commune
    fields = '__all__'
    template_name = "myapp/commune_form.html"
    success_url = reverse_lazy('commune_list')

# 📍 Supprimer une Commune
class CommuneDeleteView(DeleteView):
    model = Commune
    template_name = "myapp/commune_confirm_delete.html"
    success_url = reverse_lazy('commune_list')
    
    

# 📍 Liste des Types de Produits
class ProductTypeListView(ListView):
    model = ProductType
    template_name = "myapp/producttype_list.html"
    context_object_name = "producttypes"

# 📍 Détails d'un Type de Produit
class ProductTypeDetailView(DetailView):
    model = ProductType
    template_name = "myapp/producttype_detail.html"
    context_object_name = "producttype"

# 📍 Ajouter un Type de Produit
class ProductTypeCreateView(CreateView):
    model = ProductType
    fields = '__all__'
    template_name = "myapp/producttype_form.html"
    success_url = reverse_lazy('producttype_list')

# 📍 Modifier un Type de Produit
class ProductTypeUpdateView(UpdateView):
    model = ProductType
    fields = '__all__'
    template_name = "myapp/producttype_form.html"
    success_url = reverse_lazy('producttype_list')

# 📍 Supprimer un Type de Produit
class ProductTypeDeleteView(DeleteView):
    model = ProductType
    template_name = "myapp/producttype_confirm_delete.html"
    success_url = reverse_lazy('producttype_list')

# 📍 Liste des Produits
class ProductListView(ListView):
    model = Product
    template_name = "myapp/product_list.html"
    context_object_name = "products"

# 📍 Détails d'un Produit
class ProductDetailView(DetailView):
    model = Product
    template_name = "myapp/product_detail.html"
    context_object_name = "product"

# 📍 Ajouter un Produit
class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    template_name = "myapp/product_form.html"
    success_url = reverse_lazy('product_list')

# 📍 Modifier un Produit
class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name = "myapp/product_form.html"
    success_url = reverse_lazy('product_list')

# 📍 Supprimer un Produit
class ProductDeleteView(DeleteView):
    model = Product
    template_name = "myapp/product_confirm_delete.html"
    success_url = reverse_lazy('product_list')

# 📍 Liste des Points de Vente
class PointOfSaleListView(ListView):
    model = PointOfSale
    template_name = "myapp/pointofsale_list.html"
    context_object_name = "pointofsales"

# 📍 Détails d'un Point de Vente
class PointOfSaleDetailView(DetailView):
    model = PointOfSale
    template_name = "myapp/pointofsale_detail.html"
    context_object_name = "pointofsale"

# 📍 Ajouter un Point de Vente
class PointOfSaleCreateView(CreateView):
    model = PointOfSale
    fields = '__all__'
    template_name = "myapp/pointofsale_form.html"
    success_url = reverse_lazy('pointofsale_list')

# 📍 Modifier un Point de Vente
class PointOfSaleUpdateView(UpdateView):
    model = PointOfSale
    fields = '__all__'
    template_name = "myapp/pointofsale_form.html"
    success_url = reverse_lazy('pointofsale_list')

# 📍 Supprimer un Point de Vente
class PointOfSaleDeleteView(DeleteView):
    model = PointOfSale
    template_name = "myapp/pointofsale_confirm_delete.html"
    success_url = reverse_lazy('pointofsale_list')

# 📍 Liste des Prix des Produits
class ProductPriceListView(ListView):
    model = ProductPrice
    template_name = "myapp/productprice_list.html"
    context_object_name = "productprices"

# 📍 Détails d'un Prix de Produit
class ProductPriceDetailView(DetailView):
    model = ProductPrice
    template_name = "myapp/productprice_detail.html"
    context_object_name = "productprice"

# 📍 Ajouter un Prix de Produit
class ProductPriceCreateView(CreateView):
    model = ProductPrice
    fields = '__all__'
    template_name = "myapp/productprice_form.html"
    success_url = reverse_lazy('productprice_list')

# 📍 Modifier un Prix de Produit
class ProductPriceUpdateView(UpdateView):
    model = ProductPrice
    fields = '__all__'
    template_name = "myapp/productprice_form.html"
    success_url = reverse_lazy('productprice_list')

# 📍 Supprimer un Prix de Produit
class ProductPriceDeleteView(DeleteView):
    model = ProductPrice
    template_name = "myapp/productprice_confirm_delete.html"
    success_url = reverse_lazy('productprice_list')





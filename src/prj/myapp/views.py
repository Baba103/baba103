from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from import_export.formats.base_formats import CSV
import csv  # Bibliothèque standard de Python pour lire et écrire des fichiers CSV
from django.views import View
from django.http import HttpResponseRedirect
from .resources import WilayaResource
from .resources import MoughataaResource
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from openpyxl import load_workbook
import openpyxl
from .resources import CartProductResource

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models.model import Wilaya, Moughataa, Commune, ProductType, Product, PointOfSale, ProductPrice , Cart, CartProduct
from django.db.models import Q  # Pour la recherche avancée

@login_required
def home(request):
    return render(request, "home.html")  # ✅ Vérifie que le fichier home.html existe bien
# 📍 Liste des Wilayas

class WilayaListView(LoginRequiredMixin,ListView):
    model = Wilaya
    template_name = "myapp/wilaya_list.html"  # ✅ Modification ici
    context_object_name = "wilayas"

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q")  # Récupère le terme de recherche
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(code__icontains=query)
            )  # Recherche par nom ou code
        return queryset


# 📍 Détails d'une Wilaya
class WilayaDetailView(LoginRequiredMixin,DetailView):
    model = Wilaya
    template_name = "myapp/wilaya_detail.html"  # ✅ Modification ici
    context_object_name = "wilaya"

# 📍 Ajouter une Wilaya
class WilayaCreateView(LoginRequiredMixin,CreateView):
    model = Wilaya
    fields = '__all__'
    template_name = "myapp/wilaya_form.html"  # ✅ Modification ici
    success_url = reverse_lazy('wilaya_list')

# 📍 Modifier une Wilaya
class WilayaUpdateView(LoginRequiredMixin,UpdateView):
    model = Wilaya
    fields = '__all__'
    template_name = "myapp/wilaya_form.html"  # ✅ Modification ici
    success_url = reverse_lazy('wilaya_list')

# 📍 Supprimer une Wilaya
class WilayaDeleteView(LoginRequiredMixin,DeleteView):
    model = Wilaya
    template_name = "myapp/wilaya_confirm_delete.html"  # ✅ Modification ici
    success_url = reverse_lazy('wilaya_list')

# 📍 Liste des Moughataas avec recherche
class MoughataaListView(LoginRequiredMixin,ListView):
    model = Moughataa
    template_name = "myapp/moughataa_list.html"  # ✅ Modification ici
    context_object_name = "moughataas"

    # Logique de recherche
    def get_queryset(self):
        query = self.request.GET.get('q')  # Récupérer la requête de recherche
        if query:
            # Filtrer les moughataas par code, label ou wilaya
            return Moughataa.objects.filter(
                code__icontains=query
            ) | Moughataa.objects.filter(
                label__icontains=query
            ) | Moughataa.objects.filter(
                wilaya__name__icontains=query
            )
        # Retourner toutes les moughataas si aucune recherche
        return Moughataa.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')  # Ajouter la requête actuelle au contexte
        return context

    
    

    
    
# 📍 Détails d'une Moughataa
class MoughataaDetailView(LoginRequiredMixin,DetailView):
    model = Moughataa
    template_name = "myapp/moughataa_detail.html"  # ✅ Modification ici
    context_object_name = "moughataa"
    
    

# 📍 Ajouter une Moughataa
class MoughataaCreateView(LoginRequiredMixin,CreateView):
    model = Moughataa
    fields = '__all__'
    template_name = "myapp/moughataa_form.html"  # ✅ Modification ici
    success_url = reverse_lazy('moughataa_list')

# 📍 Modifier une Moughataa
class MoughataaUpdateView(LoginRequiredMixin,UpdateView):
    model = Moughataa
    fields = '__all__'
    template_name = "myapp/moughataa_form.html"  # ✅ Modification ici
    success_url = reverse_lazy('moughataa_list')

# 📍 Supprimer une Moughataa
class MoughataaDeleteView(LoginRequiredMixin,DeleteView):
    model = Moughataa
    template_name = "myapp/moughataa_confirm_delete.html"  # ✅ Modification ici
    success_url = reverse_lazy('moughataa_list')

# 📍 Liste des Communes avec fonctionnalité de recherche
class CommuneListView(LoginRequiredMixin,ListView):
    model = Commune
    template_name = "myapp/commune_list.html"  # Le fichier HTML correspondant
    context_object_name = "communes"  # Nom utilisé pour accéder aux données dans le template

    def get_queryset(self):
        """
        Retourne la liste des communes, filtrée par la requête de recherche si elle existe.
        """
        query = self.request.GET.get('q')  # Récupérer la requête de recherche depuis le paramètre 'q'
        if query:
            # Filtrer les communes par ID, nom ou moughataa associée
            return Commune.objects.filter(
                pk__icontains=query  # Recherche par ID
            ) | Commune.objects.filter(
                nom__icontains=query  # Recherche par Nom
            ) | Commune.objects.filter(
                moughataa__label__icontains=query  # Recherche par Moughataa
            )
        # Retourne toutes les communes si aucune recherche n'est effectuée
        return Commune.objects.all()

    def get_context_data(self, **kwargs):
        """
        Ajoute des données supplémentaires au contexte pour le template.
        """
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')  # Conserve la requête de recherche dans le contexte
        return context
    



# 📍 Détails d'une Commune
class CommuneDetailView(LoginRequiredMixin,DetailView):
    model = Commune
    template_name = "myapp/commune_detail.html"
    context_object_name = "commune"

# 📍 Ajouter une Commune
class CommuneCreateView(LoginRequiredMixin,CreateView):
    model = Commune
    fields = '__all__'
    template_name = "myapp/commune_form.html"
    success_url = reverse_lazy('commune_list')

# 📍 Modifier une Commune
class CommuneUpdateView(LoginRequiredMixin,UpdateView):
    model = Commune
    fields = '__all__'
    template_name = "myapp/commune_form.html"
    success_url = reverse_lazy('commune_list')

# 📍 Supprimer une Commune
class CommuneDeleteView(LoginRequiredMixin,DeleteView):
    model = Commune
    template_name = "myapp/commune_confirm_delete.html"
    success_url = reverse_lazy('commune_list')
    
    

# 📍 Liste des Types de Produits
class ProductTypeListView(ListView):
    model = ProductType
    template_name = "myapp/producttype_list.html"
    context_object_name = "producttypes"

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q")  # Récupère le terme de recherche
        if query:
            queryset = queryset.filter(
                Q(nom__icontains=query) | Q(description__icontains=query)
            )  # Recherche par nom ou catégorie
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "")  # Ajoute la requête au contexte
        return context


# 📍 Détails d'un Type de Produit
class ProductTypeDetailView(LoginRequiredMixin,DetailView):
    model = ProductType
    template_name = "myapp/producttype_detail.html"
    context_object_name = "producttype"

# 📍 Ajouter un Type de Produit
class ProductTypeCreateView(LoginRequiredMixin,CreateView):
    model = ProductType
    fields = '__all__'
    template_name = "myapp/producttype_form.html"
    success_url = reverse_lazy('producttype_list')

# 📍 Modifier un Type de Produit
class ProductTypeUpdateView(LoginRequiredMixin,UpdateView):
    model = ProductType
    fields = '__all__'
    template_name = "myapp/producttype_form.html"
    success_url = reverse_lazy('producttype_list')

# 📍 Supprimer un Type de Produit
class ProductTypeDeleteView(LoginRequiredMixin,DeleteView):
    model = ProductType
    template_name = "myapp/producttype_confirm_delete.html"
    success_url = reverse_lazy('producttype_list')

# 📍 Liste des Produits
class ProductListView(ListView):
    model = Product
    template_name = "myapp/product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q")  # Récupère le terme de recherche
        if query:
            queryset = queryset.filter(
                Q(nom__=query) |  # Recherche par nom
                Q(description__icontains=query) |  # Recherche par catégorie
                Q(unite_mesure__=query)  # Recherche par type de produit
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "")  # Ajoute la requête au contexte
        return context


# 📍 Détails d'un Produit
class ProductDetailView(LoginRequiredMixin,DetailView):
    model = Product
    template_name = "myapp/product_detail.html"
    context_object_name = "product"

# 📍 Ajouter un Produit
class ProductCreateView(LoginRequiredMixin,CreateView):
    model = Product
    fields = '__all__'
    template_name = "myapp/product_form.html"
    success_url = reverse_lazy('product_list')

# 📍 Modifier un Produit
class ProductUpdateView(LoginRequiredMixin,UpdateView):
    model = Product
    fields = '__all__'
    template_name = "myapp/product_form.html"
    success_url = reverse_lazy('product_list')

# 📍 Supprimer un Produit
class ProductDeleteView(LoginRequiredMixin,DeleteView):
    model = Product
    template_name = "myapp/product_confirm_delete.html"
    success_url = reverse_lazy('product_list')

# 📍 Liste des Points de Vente
class PointOfSaleListView(LoginRequiredMixin,ListView):
    model = PointOfSale
    template_name = "myapp/pointofsale_list.html"
    context_object_name = "pointofsales"

# 📍 Détails d'un Point de Vente
class PointOfSaleDetailView(LoginRequiredMixin,DetailView):
    model = PointOfSale
    template_name = "myapp/pointofsale_detail.html"
    context_object_name = "pointofsale"

# 📍 Ajouter un Point de Vente
class PointOfSaleCreateView(LoginRequiredMixin,CreateView):
    model = PointOfSale
    fields = '__all__'
    template_name = "myapp/pointofsale_form.html"
    success_url = reverse_lazy('pointofsale_list')

# 📍 Modifier un Point de Vente
class PointOfSaleUpdateView(LoginRequiredMixin,UpdateView):
    model = PointOfSale
    fields = '__all__'
    template_name = "myapp/pointofsale_form.html"
    success_url = reverse_lazy('pointofsale_list')

# 📍 Supprimer un Point de Vente
class PointOfSaleDeleteView(LoginRequiredMixin,DeleteView):
    model = PointOfSale
    template_name = "myapp/pointofsale_confirm_delete.html"
    success_url = reverse_lazy('pointofsale_list')

# 📍 Liste des Prix des Produits
class ProductPriceListView(LoginRequiredMixin,ListView):
    model = ProductPrice
    template_name = "myapp/productprice_list.html"
    context_object_name = "productprices"

# 📍 Détails d'un Prix de Produit
class ProductPriceDetailView(LoginRequiredMixin,DetailView):
    model = ProductPrice
    template_name = "myapp/productprice_detail.html"
    context_object_name = "productprice"

# 📍 Ajouter un Prix de Produit
class ProductPriceCreateView(LoginRequiredMixin,CreateView):
    model = ProductPrice
    fields = '__all__'
    template_name = "myapp/productprice_form.html"
    success_url = reverse_lazy('productprice_list')

# 📍 Modifier un Prix de Produit
class ProductPriceUpdateView(LoginRequiredMixin,UpdateView):
    model = ProductPrice
    fields = '__all__'
    template_name = "myapp/productprice_form.html"
    success_url = reverse_lazy('productprice_list')

# 📍 Supprimer un Prix de Produit
class ProductPriceDeleteView(LoginRequiredMixin,DeleteView):
    model = ProductPrice
    template_name = "myapp/productprice_confirm_delete.html"
    success_url = reverse_lazy('productprice_list')


# 📍 Liste des Paniers
class CartListView(LoginRequiredMixin,ListView):
    model = Cart
    template_name = "myapp/cart_list.html"
    context_object_name = "carts"

# 📍 Détails d'un Panier
class CartDetailView(LoginRequiredMixin,DetailView):
    model = Cart
    template_name = "myapp/cart_detail.html"
    context_object_name = "cart"

# 📍 Ajouter un Panier
class CartCreateView(LoginRequiredMixin,CreateView):
    model = Cart
    fields = '__all__'
    template_name = "myapp/cart_form.html"
    success_url = reverse_lazy('cart_list')

# 📍 Modifier un Panier
class CartUpdateView(LoginRequiredMixin,UpdateView):
    model = Cart
    fields = '__all__'
    template_name = "myapp/cart_form.html"
    success_url = reverse_lazy('cart_list')

# 📍 Supprimer un Panier
class CartDeleteView(LoginRequiredMixin,DeleteView):
    model = Cart
    template_name = "myapp/cart_confirm_delete.html"
    success_url = reverse_lazy('cart_list')

# 📍 Liste des Produits dans un Panier
class CartProductListView(LoginRequiredMixin,ListView):
    model = CartProduct
    template_name = "myapp/cartproduct_list.html"
    context_object_name = "cartproducts"
    
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')  # Recherche par produit, panier ou poids
        cartproducts = CartProduct.objects.all()

        if query:
            cartproducts = cartproducts.filter(
                Q(produit__nom__icontains=query) |
                Q(panier__nom__icontains=query) |
                Q(poids__icontains=query)
            )

        return render(request, self.template_name, {
            "cartproducts": cartproducts,
            "query": query,
        })
    

# 📍 Détails d'un Produit dans un Panier
class CartProductDetailView(DetailView):
    model = CartProduct
    template_name = "myapp/cartproduct_detail.html"
    context_object_name = "cartproduct"
# 📍 Ajouter un Produit dans un Panier
class CartProductCreateView(CreateView):
    model = CartProduct
    fields = '__all__'
    template_name = "myapp/cartproduct_form.html"
    success_url = reverse_lazy('cartproduct_list')

# 📍 Modifier un Produit dans un Panier
class CartProductUpdateView(UpdateView):
    model = CartProduct
    fields = '__all__'
    template_name = "myapp/cartproduct_form.html"
    success_url = reverse_lazy('cartproduct_list')

# 📍 Supprimer un Produit dans un Panier
class CartProductDeleteView(DeleteView):
    model = CartProduct
    template_name = "myapp/cartproduct_confirm_delete.html"
    success_url = reverse_lazy('cartproduct_list')




# Exporter les données au format CSV
class WilayaExportView(View):
    def get(self, request, *args, **kwargs):
        resource = WilayaResource()
        dataset = resource.export()

        # Déterminer le format d'exportation (CSV ou Excel) à partir d'un paramètre GET
        export_format = request.GET.get("format", "csv").lower()

        if export_format == "xlsx":
            response = HttpResponse(dataset.xlsx, content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            response['Content-Disposition'] = 'attachment; filename="wilayas.xlsx"'
        else:  # Par défaut, exporter en CSV
            response = HttpResponse(dataset.csv, content_type="text/csv")
            response['Content-Disposition'] = 'attachment; filename="wilayas.csv"'

        return response


class MoughataaExportView(View):
    def get(self, request, *args, **kwargs):
        resource = MoughataaResource()
        dataset = resource.export()

        # Déterminer le format d'exportation (CSV ou Excel) à partir d'un paramètre GET
        export_format = request.GET.get("format", "csv").lower()

        if export_format == "xlsx":
            response = HttpResponse(
                dataset.xlsx,
                content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
            response['Content-Disposition'] = 'attachment; filename="moughataas.xlsx"'
        else:  # Par défaut, exporter en CSV
            response = HttpResponse(dataset.csv, content_type="text/csv")
            response['Content-Disposition'] = 'attachment; filename="moughataas.csv"'

        return response


from myapp.resources import CommuneResource

class CommuneExportView(View):
    def get(self, request, *args, **kwargs):
        resource = CommuneResource()
        dataset = resource.export()

        # Vérifier le format d'exportation demandé (CSV ou Excel)
        export_format = request.GET.get("format", "csv").lower()

        if export_format == "xlsx":
            response = HttpResponse(
                dataset.xlsx,
                content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
            response['Content-Disposition'] = 'attachment; filename="communes.xlsx"'
        else:  # Par défaut, exporter en CSV
            response = HttpResponse(dataset.csv, content_type="text/csv")
            response['Content-Disposition'] = 'attachment; filename="communes.csv"'

        return response

class PointOfSaleExportView(View):
    def get(self, request, *args, **kwargs):
        resource = PointOfSaleResource()  # Remplacez par votre resource pour PointOfSale
        dataset = resource.export()

        # Déterminer le format d'exportation (CSV ou Excel) à partir d'un paramètre GET
        export_format = request.GET.get("format", "csv").lower()

        if export_format == "xlsx":
            response = HttpResponse(
                dataset.xlsx,
                content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
            response['Content-Disposition'] = 'attachment; filename="point_of_sales.xlsx"'
        else:  # Par défaut, exporter en CSV
            response = HttpResponse(dataset.csv, content_type="text/csv")
            response['Content-Disposition'] = 'attachment; filename="point_of_sales.csv"'

        return response


from .resources import ProductTypeResource

class ProductTypeExportView(View):
    def get(self, request, *args, **kwargs):
        resource = ProductTypeResource()  # Classe resource pour ProductType
        dataset = resource.export()

        # Export en Excel
        response = HttpResponse(
            dataset.xlsx,
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response['Content-Disposition'] = 'attachment; filename="product_types.xlsx"'
        return response
    
class ProductExportView(View):
    def get(self, request, *args, **kwargs):
        resource = ProductResource()  # Classe resource pour Product
        dataset = resource.export()

        response = HttpResponse(
            dataset.xlsx,
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response['Content-Disposition'] = 'attachment; filename="products.xlsx"'
        return response


from .resources import ProductPriceResource

class ProductPriceExportView(View):
    def get(self, request, *args, **kwargs):
        resource = ProductPriceResource()  # Utilisation de la classe resource
        dataset = resource.export()

        response = HttpResponse(
            dataset.xlsx,
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response['Content-Disposition'] = 'attachment; filename="product_prices.xlsx"'
        return response
    
from django.http import HttpResponse
from .resources import CartResource

class CartExportView(View):
    def get(self, request, *args, **kwargs):
        resource = CartResource()  # Utilisation de la classe resource
        dataset = resource.export()

        response = HttpResponse(
            dataset.xlsx,
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response['Content-Disposition'] = 'attachment; filename="carts.xlsx"'
        return response


# 📤 Exporter CartProduct en Excel
class CartProductExportView(View):
    def get(self, request, *args, **kwargs):
        resource = CartProductResource()
        dataset = resource.export()
        response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="cartproducts.xlsx"'
        return response

from django.shortcuts import render
from django.http import HttpResponseRedirect
from myapp.resources import WilayaResource
from tablib import Dataset
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class WilayaImportView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        # Affiche le formulaire pour importer un fichier
        return render(request, "myapp/wilaya_import.html")

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        if not file:
            return render(request, "myapp/wilaya_import.html", {"errors": ["Aucun fichier n'a été fourni."]})

        try:
            # Vérifier l'extension du fichier
            if file.name.endswith('.xlsx') or file.name.endswith('.xls'):
                # Charger le fichier Excel avec openpyxl
                workbook = load_workbook(file)
                sheet = workbook.active  # Récupère la première feuille
                data = []
                for row in sheet.iter_rows(min_row=2, values_only=True):  # Sauter l'en-tête
                    if row[0] and row[1]:  # Assurez-vous que les colonnes 'code' et 'name' existent
                        data.append([row[0], row[1]])  # Ajoute 'code' et 'name' à la liste
            else:
                return render(request, "myapp/wilaya_import.html", {"errors": ["Le fichier doit être au format Excel (.xlsx ou .xls)."]})
        except Exception as e:
            return render(request, "myapp/wilaya_import.html", {"errors": [f"Erreur lors de la lecture du fichier Excel : {str(e)}"]})

        # Préparer le dataset pour l'importation
        resource = WilayaResource()
        dataset = Dataset()
        dataset.headers = ['code', 'name']  # Définir les colonnes attendues
        for row in data:
            dataset.append(row)  # Ajouter les lignes extraites du fichier Excel

        try:
            # Simulation d'importation avec dry_run=True
            result = resource.import_data(dataset, dry_run=True)
            if not result.has_errors():
                resource.import_data(dataset, dry_run=False)  # Import réel
                return HttpResponseRedirect('/wilayas/')
            else:
                return render(request, "myapp/wilaya_import.html", {"errors": result.row_errors})
        except Exception as e:
            return render(request, "myapp/wilaya_import.html", {"errors": [str(e)]})




class MoughataaImportView(View):
    def get(self, request, *args, **kwargs):
        # Affiche le formulaire pour importer un fichier
        return render(request, "myapp/moughataa_import.html")

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        if not file:
            return render(request, "myapp/moughataa_import.html", {"errors": ["Aucun fichier n'a été fourni."]})

        try:
            # Vérification de l'extension du fichier
            if file.name.endswith('.xlsx') or file.name.endswith('.xls'):
                # Lecture du fichier Excel
                workbook = load_workbook(file)
                sheet = workbook.active  # Récupère la première feuille
                data = []
                for row in sheet.iter_rows(min_row=2, values_only=True):  # Sauter l'en-tête
                    if row[0] and row[1] and row[2]:  # Vérifie que les colonnes nécessaires existent
                        data.append([row[0], row[1], row[2]])  # 'code', 'label', 'wilaya'
            else:
                return render(request, "myapp/moughataa_import.html", {"errors": ["Le fichier doit être au format Excel (.xlsx ou .xls)."]})
        except Exception as e:
            return render(request, "myapp/moughataa_import.html", {"errors": [f"Erreur lors de la lecture du fichier Excel : {str(e)}"]})

        # Préparation des données pour l'importation
        resource = MoughataaResource()
        dataset = Dataset()
        dataset.headers = ['code', 'label', 'wilaya']  # Définir les colonnes attendues
        for row in data:
            try:
                # Trouver l'instance de Wilaya basée sur son nom
                wilaya = Wilaya.objects.get(name=row[2])
                # Ajouter les données au dataset
                dataset.append([row[0], row[1], wilaya.pk])
            except Wilaya.DoesNotExist:
                return render(request, "myapp/moughataa_import.html", {
                    "errors": [f"La Wilaya '{row[2]}' n'existe pas dans la base de données."]
                })

        try:
            # Simulation d'importation avec dry_run=True
            result = resource.import_data(dataset, dry_run=True)
            if not result.has_errors():
                # Import réel si pas d'erreurs
                resource.import_data(dataset, dry_run=False)
                return HttpResponseRedirect('/moughataas/')
            else:
                return render(request, "myapp/moughataa_import.html", {"errors": result.row_errors})
        except Exception as e:
            return render(request, "myapp/moughataa_import.html", {"errors": [str(e)]})



from myapp.resources import CommuneResource



class CommuneImportView(View):
    def get(self, request, *args, **kwargs):
        # Affiche le formulaire pour importer un fichier
        return render(request, "myapp/commune_import.html")

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        if not file:
            return render(request, "myapp/commune_import.html", {"errors": ["Aucun fichier n'a été fourni."]})

        # Vérifier si le fichier est un fichier Excel
        if not (file.name.endswith('.xls') or file.name.endswith('.xlsx')):
            return render(request, "myapp/commune_import.html", {"errors": ["Seuls les fichiers Excel sont acceptés."]})

        try:
            # Lecture du fichier Excel
            workbook = openpyxl.load_workbook(file)
            sheet = workbook.active  # Obtenir la première feuille du fichier

            # Vérification des colonnes attendues
            required_columns = ['nom', 'moughataa']
            detected_columns = [cell.value for cell in sheet[1]]  # Lire les en-têtes de la première ligne
            missing_cols = [col for col in required_columns if col not in detected_columns]

            if missing_cols:
                return render(request, "myapp/commune_import.html", {
                    "errors": [
                        f"Le fichier Excel est invalide. Colonnes manquantes : {', '.join(missing_cols)}",
                        f"Colonnes détectées : {', '.join(detected_columns or [])}"
                    ]
                })

            # Préparation des données pour l'importation
            resource = CommuneResource()
            dataset = Dataset()
            dataset.headers = required_columns

            # Lire les données à partir de la deuxième ligne
            for row in sheet.iter_rows(min_row=2, values_only=True):
                try:
                    nom, moughataa_label = row
                    # Trouver l'instance de Moughataa basée sur son label
                    moughataa = Moughataa.objects.get(label=moughataa_label)
                    dataset.append([nom, moughataa.pk])
                except Moughataa.DoesNotExist:
                    return render(request, "myapp/commune_import.html", {
                        "errors": [f"La Moughataa '{moughataa_label}' n'existe pas dans la base de données."]
                    })

            # Simulation d'importation avec dry_run=True
            result = resource.import_data(dataset, dry_run=True)
            if not result.has_errors():
                # Import réel si pas d'erreurs
                resource.import_data(dataset, dry_run=False)
                return HttpResponseRedirect('/communes/')
            else:
                return render(request, "myapp/commune_import.html", {"errors": result.row_errors})

        except Exception as e:
            return render(request, "myapp/commune_import.html", {"errors": [f"Erreur lors de la lecture du fichier : {str(e)}"]})



from django.http import HttpResponseRedirect
from .resources import PointOfSaleResource


class PointOfSaleImportView(View):
    def get(self, request, *args, **kwargs):
        # Affiche le formulaire pour importer un fichier
        return render(request, "myapp/pointofsale_import.html")

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        if not file:
            return render(request, "myapp/pointofsale_import.html", {"errors": ["Aucun fichier n'a été fourni."]})

        # Vérifier si le fichier est un fichier Excel
        if not (file.name.endswith('.xls') or file.name.endswith('.xlsx')):
            return render(request, "myapp/pointofsale_import.html", {"errors": ["Seuls les fichiers Excel sont acceptés."]})

        try:
            # Lecture du fichier Excel
            workbook = load_workbook(file)
            sheet = workbook.active  # Obtenir la première feuille du fichier

            # Préparation des données pour l'importation
            resource = PointOfSaleResource()
            dataset = Dataset()
            dataset.headers = ['name', 'location', 'contact']  # Colonnes attendues

            for row in sheet.iter_rows(min_row=2, values_only=True):
                if all(row):  # Vérifie que toutes les colonnes sont remplies
                    dataset.append(row)

            # Simulation d'importation avec dry_run=True
            result = resource.import_data(dataset, dry_run=True)
            if not result.has_errors():
                # Import réel si pas d'erreurs
                resource.import_data(dataset, dry_run=False)
                return HttpResponseRedirect('/pointofsales/')
            else:
                return render(request, "myapp/pointofsale_import.html", {"errors": result.row_errors})

        except Exception as e:
            return render(request, "myapp/pointofsale_import.html", {"errors": [f"Erreur lors de la lecture du fichier Excel : {str(e)}"]})



class ProductTypeImportView(View):
    def get(self, request, *args, **kwargs):
        # Affiche le formulaire pour importer un fichier
        return render(request, "myapp/producttype_import.html")

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        if not file:
            return render(request, "myapp/producttype_import.html", {"errors": ["Aucun fichier n'a été fourni."]})

        # Vérifier si le fichier est un fichier Excel
        if not (file.name.endswith('.xls') or file.name.endswith('.xlsx')):
            return render(request, "myapp/producttype_import.html", {"errors": ["Seuls les fichiers Excel sont acceptés."]})

        try:
            # Lecture du fichier Excel
            workbook = load_workbook(file)
            sheet = workbook.active  # Obtenir la première feuille du fichier

            # Préparation des données pour l'importation
            resource = ProductTypeResource()
            dataset = Dataset()
            dataset.headers = ['name', 'description']  # Colonnes attendues

            for row in sheet.iter_rows(min_row=2, values_only=True):
                if all(row):  # Vérifie que toutes les colonnes sont remplies
                    dataset.append(row)

            # Simulation d'importation avec dry_run=True
            result = resource.import_data(dataset, dry_run=True)
            if not result.has_errors():
                # Import réel si pas d'erreurs
                resource.import_data(dataset, dry_run=False)
                return HttpResponseRedirect('/producttypes/')
            else:
                return render(request, "myapp/producttype_import.html", {"errors": result.row_errors})

        except Exception as e:
            return render(request, "myapp/producttype_import.html", {"errors": [f"Erreur lors de la lecture du fichier Excel : {str(e)}"]})



class ProductImportView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "myapp/product_import.html")

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        if not file:
            return render(request, "myapp/product_import.html", {"errors": ["Aucun fichier n'a été fourni."]})

        if not (file.name.endswith('.xls') or file.name.endswith('.xlsx')):
            return render(request, "myapp/product_import.html", {"errors": ["Seuls les fichiers Excel sont acceptés."]})

        try:
            workbook = load_workbook(file)
            sheet = workbook.active

            resource = ProductResource()
            dataset = Dataset()
            dataset.headers = ['code', 'nom', 'categorie']  # Colonnes attendues

            for row in sheet.iter_rows(min_row=2, values_only=True):
                if all(row):
                    dataset.append(row)

            result = resource.import_data(dataset, dry_run=True)
            if not result.has_errors():
                resource.import_data(dataset, dry_run=False)
                return HttpResponseRedirect('/products/')
            else:
                return render(request, "myapp/product_import.html", {"errors": result.row_errors})

        except Exception as e:
            return render(request, "myapp/product_import.html", {"errors": [f"Erreur : {str(e)}"]})


from django.http import HttpResponseRedirect
from .resources import ProductPriceResource


class ProductPriceImportView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "myapp/productprice_import.html")

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        if not file:
            return render(request, "myapp/productprice_import.html", {"errors": ["Aucun fichier n'a été fourni."]})

        if not (file.name.endswith('.xls') or file.name.endswith('.xlsx')):
            return render(request, "myapp/productprice_import.html", {"errors": ["Seuls les fichiers Excel sont acceptés."]})

        try:
            workbook = load_workbook(file)
            sheet = workbook.active

            resource = ProductPriceResource()
            dataset = Dataset()
            dataset.headers = ['produit', 'point_vente', 'valeur', 'date_from', 'date_to']  # Colonnes attendues

            for row in sheet.iter_rows(min_row=2, values_only=True):
                if all(row):
                    dataset.append(row)

            result = resource.import_data(dataset, dry_run=True)
            if not result.has_errors():
                resource.import_data(dataset, dry_run=False)
                return HttpResponseRedirect('/productprices/')
            else:
                return render(request, "myapp/productprice_import.html", {"errors": result.row_errors})

        except Exception as e:
            return render(request, "myapp/productprice_import.html", {"errors": [f"Erreur : {str(e)}"]})



from .resources import CartResource

class CartImportView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "myapp/cart_import.html")

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        if not file:
            return render(request, "myapp/cart_import.html", {"errors": ["Aucun fichier n'a été fourni."]})

        if not (file.name.endswith('.xls') or file.name.endswith('.xlsx')):
            return render(request, "myapp/cart_import.html", {"errors": ["Seuls les fichiers Excel sont acceptés."]})

        try:
            workbook = load_workbook(file)
            sheet = workbook.active

            resource = CartResource()
            dataset = Dataset()
            dataset.headers = ['code', 'name', 'description']  # Colonnes attendues

            for row in sheet.iter_rows(min_row=2, values_only=True):
                if all(row):
                    dataset.append(row)

            result = resource.import_data(dataset, dry_run=True)
            if not result.has_errors():
                resource.import_data(dataset, dry_run=False)
                return HttpResponseRedirect('/carts/')
            else:
                return render(request, "myapp/cart_import.html", {"errors": result.row_errors})

        except Exception as e:
            return render(request, "myapp/cart_import.html", {"errors": [f"Erreur : {str(e)}"]})

# 📥 Importer CartProduct depuis un fichier Excel
class CartProductImportView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "myapp/cartproduct_import.html")

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        if not file:
            return render(request, "myapp/cartproduct_import.html", {"errors": ["Aucun fichier n'a été fourni."]})

        try:
            # Charger le fichier Excel
            dataset = Dataset()
            imported_data = dataset.load(file.read(), format='xlsx')

            # Vérifier les colonnes nécessaires
            required_columns = ['produit', 'panier', 'poids']
            detected_columns = dataset.headers
            missing_cols = [col for col in required_columns if col not in detected_columns]

            if missing_cols:
                return render(request, "myapp/cartproduct_import.html", {
                    "errors": [
                        f"Le fichier Excel est invalide. Colonnes manquantes : {', '.join(missing_cols)}",
                        f"Colonnes détectées : {', '.join(detected_columns or [])}"
                    ]
                })

            resource = CartProductResource()
            result = resource.import_data(dataset, dry_run=True)

            if not result.has_errors():
                resource.import_data(dataset, dry_run=False)
                return HttpResponseRedirect('/cartproducts/')
            else:
                return render(request, "myapp/cartproduct_import.html", {"errors": result.row_errors})

        except Exception as e:
            return render(request, "myapp/cartproduct_import.html", {"errors": [f"Erreur lors de l'importation : {str(e)}"]})



from django.shortcuts import render, redirect
from django.views import View
from .models import ProductPrice, CartProduct, INPC
from datetime import datetime
from django.db.models import Sum

class CalculateINPCView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "myapp/calculate_inpc.html")

    def post(self, request, *args, **kwargs):
        # Récupérer le mois sélectionné
        mois_str = request.POST.get("mois")  # Format attendu: 'YYYY-MM'
        try:
            mois = datetime.strptime(mois_str, "%Y-%m")
        except ValueError:
            return render(request, "myapp/calculate_inpc.html", {"errors": ["Format du mois invalide."]})

        # Récupérer les prix des produits actifs pendant le mois donné
        prix_produits = ProductPrice.objects.filter(
            date_from__lte=mois,
            date_to__gte=mois
        )

        # Récupérer les poids associés aux produits dans les paniers
        produits_dans_paniers = CartProduct.objects.filter(
            produit__in=[p.produit for p in prix_produits]
        )

        # Calculer l'INPC
        numerateur = 0
        denominateur = 0

        for prix in prix_produits:
            # Trouver le poids associé au produit dans les paniers
            poids = produits_dans_paniers.filter(produit=prix.produit).aggregate(Sum("poids"))["poids__sum"] or 0
            numerateur += prix.valeur * poids
            denominateur += poids

        if denominateur == 0:
            return render(request, "myapp/calculate_inpc.html", {"errors": ["Impossible de calculer l'INPC (dénominateur nul)."]})

        inpc_valeur = numerateur / denominateur

        # Sauvegarder l'INPC dans la base de données
        inpc, created = INPC.objects.get_or_create(mois=mois, defaults={"valeur": inpc_valeur})
        if not created:
            inpc.valeur = inpc_valeur
            inpc.save()

        return redirect("inpc_list")

from django.views.generic import ListView

class INPCListView(ListView):
    model = INPC
    template_name = "myapp/inpc_list.html"
    context_object_name = "inpcs"

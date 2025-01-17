from django.db import models




#  Modèle pour Wilaya (Région)
class Wilaya(models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=252)

    def __str__(self):
        return self.name

# Modèle pour Moughataa (Subdivision d'une Wilaya)
class Moughataa(models.Model):
    code = models.CharField(max_length=45, unique=True)
    label = models.CharField(max_length=45)
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE)

    def __str__(self):
        return self.label
    
class Commune(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    moughataa = models.ForeignKey(Moughataa, on_delete=models.CASCADE, related_name="communes")

    def __str__(self):
        return f"{self.nom} ({self.moughataa.nom})"
    
# ✅ Modèle Type de Produit
class ProductType(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom

# ✅ Modèle Produit
class Product(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    type_produit = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name="produits")
    unite_mesure = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

# ✅ Modèle Point de Vente
class PointOfSale(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=50, choices=[('Marché', 'Marché'), ('Supermarché', 'Supermarché'), ('Autre', 'Autre')])
    gps_lat = models.FloatField()
    gps_lon = models.FloatField()
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE, related_name="points_de_vente")

    def __str__(self):
        return self.nom

# ✅ Modèle Prix du Produit
class ProductPrice(models.Model):
    produit = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="prix")
    point_vente = models.ForeignKey(PointOfSale, on_delete=models.CASCADE, related_name="prix")
    valeur = models.FloatField()
    date_from = models.DateField()
    date_to = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.produit.nom} - {self.valeur} MRO"

# ✅ Modèle Panier (Groupe de Produits)
class Cart(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom

# ✅ Modèle Relation Panier-Produit avec Pondération
class CartProduct(models.Model):
    produit = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="paniers")
    panier = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="produits")
    poids = models.FloatField()
    date_from = models.DateField()
    date_to = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.produit.nom} dans {self.panier.nom} - {self.poids}%"

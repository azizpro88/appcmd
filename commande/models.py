from django.db import models
from datetime import datetime
# Create your models here.

class Article(models.Model):
    nom_article=models.CharField(max_length=200)
    def __str__(self):
        return self.nom_article

class Fournisseur(models.Model):
    nom_fournisseur=models.CharField(max_length=200)
    def __str__(self):
        return  self.nom_fournisseur

class Site(models.Model):
    nom_site=models.CharField(max_length=200)
    def __str__(self):
        return self.nom_site
    
class LigneCommande(models.Model):
    num_cmd=models.IntegerField('N° de commande')
    def __str__(self):
        return str(self.num_cmd ) 
    class Meta:
        ordering=['-num_cmd']

class Commande(models.Model):
    lignecommande=models.ForeignKey(LigneCommande,on_delete=models.CASCADE)
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    fournisseur=models.ForeignKey(Fournisseur,on_delete=models.CASCADE)
    site=models.ForeignKey(Site,on_delete=models.CASCADE)
    quantite_commande=models.IntegerField("Quantité Commandé",default=0)
    quantite_recue=models.IntegerField("Quantité Reçue",default=0)
    ecart=models.CharField("Ecart",max_length=200,null=True)
    date_commande =models.DateTimeField('Date de Commande',default=datetime.now)
   

    def __str__(self):
        return str(self.date_commande)
    
    class Meta:
        ordering=['-date_commande']


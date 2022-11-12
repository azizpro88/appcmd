from django.contrib import admin
from .models import Article,Fournisseur,Site,Commande,LigneCommande

# Register your models here.
admin.site.site_header="GESTION COMMANDE"
admin.site.site_title="Gestion Commande"
class CommandeAdmin(admin.ModelAdmin):
   list_display= ['id','lignecommande','article','fournisseur','site','quantite_commande','quantite_recue','ecart','date_commande']  
   list_display_links=['id','lignecommande','article','date_commande']
   list_filter = ['lignecommande','date_commande','site']
   search_fields = ['lignecommande']
   
  

class ArticleAdmin(admin.ModelAdmin):
   search_fields=['nom_article']

class SiteAdmin(admin.ModelAdmin):
       search_fields=['nom_site']

class FournisseurAdmin(admin.ModelAdmin):
       search_fields=['nom_fournisseur']

class LignecmdAdmin(admin.ModelAdmin):
       search_fields=['num_cmd']

admin.site.register(Article,ArticleAdmin)
admin.site.register(Fournisseur,FournisseurAdmin)
admin.site.register(Site,SiteAdmin)
admin.site.register(LigneCommande,LignecmdAdmin)
admin.site.register(Commande,CommandeAdmin)

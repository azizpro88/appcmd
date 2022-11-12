from django.shortcuts import render,get_object_or_404
from .models import Commande
from django.contrib import messages
# Create your views here.

def index(request):

    if 'search' in request.GET:
        search=request.GET['search']
        if search=='':
            search=0
        liste=Commande.objects.filter(lignecommande=search)
    else:
        liste=Commande.objects.all()
    context={
         'liste':liste
    }
    messages.info(request,'ok')
    return render(request,'liste_commande.html',context)


def admin(request):
    return render(request,"./admin/")
    #return render(request,"http://127.0.0.1:8000/admin/")

#def detail_page(request,id):
    #obj=get_object_or_404(Commande,pk=id)
    #return render(request,'detail.html',{'obj':obj})
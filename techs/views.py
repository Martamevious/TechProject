from django.shortcuts import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.validators import *

# Create your views here.
def home(request):
   article=Article.objects.all()
   context={"article":article}
   return render(request, "index.html",context)



#FONCTIONS DE CLIENTS

def login(request):
    if request.method != 'POST':
        return render(request, "client/login.html")
    elif request.method == 'POST':
        email = request.POST.get('email',None)
        password = request.POST.get('password',None)
        return render(request, "client/accueil.html")
    
# login_required(login_url=login)
# def client(request):
#    client=User.objects.all()
#    context={"client":client} 
#    return render(request,"client/accueil.html", context)

def accueil(request):
    return render(request, "client/accueil.html")

def register(request):
    return render(request, "client/register.html")
  
def sign_up(request):
    
    if request.method == 'POST':
        nom = request.POST.get('nom',None)
        email = request.POST.get('email',None)
        password = request.POST.get('password',None)
        repassword = request.POST.get('repassword',None)
        
        if password != repassword:
            error = True
            message = "Les deux mots de passe ne correspondent pas !"
            context = {
                'error':error,
                'message':message
            }
            return render(request, "client/register.html",context)
        elif password == repassword:
           Client.objects.create(nomClient=nom,emailClient=email,passwordClient=password,confirmationClient=repassword)
        return render(request, "login.html")
    elif request.method != 'POST':
       return render(request, "client/register.html")
           
    

# login_required
def client(request):
    return render(request, "accueil.html")


#FONCTIONS DE VENDEURS

def loginV(request):
    return render(request, "vendeur/loginVendeur.html")

def accueilV(request):
    return render(request, "vendeur/accueilVendeur.html")

def registerV(request):
    return render(request, "vendeur/registerVendeur.html")
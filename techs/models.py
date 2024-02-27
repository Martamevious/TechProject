from django.db import models

# Create your models here.
class Client(models.Model):
    nomClient = models.CharField(max_length=20)
    emailClient = models.CharField(max_length=20)
    passwordClient = models.CharField(max_length=20)
    confirmationClient = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.nomClient
     

class Vendeur(models.Model):
    nomVendeur = models.CharField(max_length=20)
    emailVendeur = models.CharField(max_length=20)
    passwordVendeur = models.CharField(max_length=20)
    confirmationVendeur = models.CharField(max_length=20)
    boutique = models.CharField(max_length=20)
    abonnement = models.CharField(max_length=20)
     
    def __str__(self) -> str:
        return self.nomVendeur
 
class Category(models.Model):
    name=models.CharField(max_length=120)
    
    def __str__(self) -> str:
            return self.name 


class Article(models.Model):
    title=models.CharField(max_length=15)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    category=models.CharField(max_length=30)
    desc=models.TextField()
    image=models.ImageField(upload_to='', blank=True)
    vendeur=models.ForeignKey(Vendeur,on_delete=models.CASCADE)
    vendeur=models.CharField(max_length=30)
    prix=models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return self.title   
    
# class Commande(models.Model):
#     title=models.CharField(max_length=15)
#     category=models.ForeignKey(Category,on_delete=models.CASCADE)
#     category=models.CharField(max_length=30)
#     desc=models.TextField()
#     image=models.ImageField(upload_to='', blank=True)
#     vendeur=models.ForeignKey(Vendeur,on_delete=models.CASCADE)
#     boutique=models.CharField(max_length=30)
#     prix=models.CharField(max_length=10)
    
#     def __str__(self) -> str:
#         return self.title 

class Admin(models.Model):
    nom = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    confirmation = models.CharField(max_length=20)
    vendeur=models.ForeignKey(Vendeur,on_delete=models.CASCADE)
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nom
    
    
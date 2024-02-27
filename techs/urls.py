from django.urls import *
from techs.views import *



urlpatterns = [
    path('', home, name="home"),
    path('Register',sign_up, name="sign_up"),
    path('Register', register, name="register"),
    path('Login', login, name="login"),
    path('Client', accueil, name="accueil"),
    path('Vendeur', accueilV, name="accueilV"),
    path('Login Vendeur', loginV, name="loginV"),
    path('Register Vendeur', registerV, name="registerV"),
]
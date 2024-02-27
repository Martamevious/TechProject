from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Client)
admin.site.register(Vendeur)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Admin)
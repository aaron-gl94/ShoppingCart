from django.contrib import admin
from .models import Product

class ProdAdmin(admin.ModelAdmin):
	list_display = ('nombre','description')	
	ordering = ('nombre',)
	search_fields = ('nombre',)
		
admin.site.register(Product,ProdAdmin)
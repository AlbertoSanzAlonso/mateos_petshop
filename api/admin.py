from django.contrib import admin
from .models import Product
from import_export.admin import ImportExportModelAdmin

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'price', 'stock', 'created_at')  # columnas en la lista
    list_filter = ('created_at', 'price', 'stock')  # filtros en la barra lateral
    search_fields = ('name', 'description')  # campo de búsqueda
    ordering = ('-created_at',)  # orden descendente por fecha


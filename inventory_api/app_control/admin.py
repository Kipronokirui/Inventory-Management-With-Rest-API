from django.contrib import admin
from .models import Inventory, InventoryGroup, Shop, Invoice, InvoiceItem

# Register your models here
admin.site.register((Inventory, InventoryGroup, Shop, Invoice, InvoiceItem))

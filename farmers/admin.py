from django.contrib import admin
from .models import SellerProfile, Inventory
# Register your models here.
class SellerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'shop_name')

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('seller', 'crops', 'price', 'quantity')

admin.site.register(SellerProfile, SellerAdmin)
admin.site.register(Inventory, InventoryAdmin)


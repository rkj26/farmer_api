from django.contrib import admin
from .models import SellerProfile, Inventory, UserProfile, Cart


# Register your models here.
class SellerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'shop_name', 'address', 'longitude', 'latitude')


class InventoryAdmin(admin.ModelAdmin):
    list_display = ('seller', 'crops', 'price', 'quantity')


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'address', 'longitude', 'latitude')


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'seller', 'item', 'price', 'quantity')


admin.site.register(SellerProfile, SellerAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(UserProfile, UserAdmin)

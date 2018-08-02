from django.contrib import admin
from .models import Item, ItemGroup, Price, Topping, Order, Cart

# Register your models here.
admin.site.register(ItemGroup)
admin.site.register(Item)
admin.site.register(Price)
admin.site.register(Topping)
admin.site.register(Order)
admin.site.register(Cart)


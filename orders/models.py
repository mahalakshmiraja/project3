from django.db import models
from django.contrib import admin
from decimal import Decimal


class ItemGroup(models.Model):
    groupName = models.CharField(max_length=64)

    def __str__(self):
        return f"Group ID of {self.groupName} is: {self.id}"


class Item(models.Model):
    itemName = models.CharField(max_length=64)
    itemGroupId = models.ForeignKey(ItemGroup, on_delete=models.CASCADE)
    displayName = models.CharField(max_length=64, default="")
    def __str__(self):
        return f"{self.displayName}"



class Price(models.Model):

    size = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4,decimal_places=2)
    itemId = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return f"Price of {self.size} {self.itemId} is {self.price}"

class Topping(models.Model):
    toppingName = models.CharField(max_length=64)
    toppingPrice = models.DecimalField(max_digits=4,decimal_places=2)

    def __str__(self):
        return f"Price of {self.toppingName} is {self.toppingPrice}"



class Cart(models.Model):
    cartItem =  models.ForeignKey(Price, on_delete=models.CASCADE)
    user =  models.CharField(max_length=64)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.user} has {self.cartItem} in cart"

class Order(models.Model):
    orderItem = models.CharField(max_length=64)
    quantity = models.IntegerField()


    def __str__(self):
        return f"{self.orderItem} is ordered "


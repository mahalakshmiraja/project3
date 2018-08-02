from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.urls import reverse
from .models import Item, Price, ItemGroup, Cart
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message" : None})
    userName = request.user.username
    cart = None
    if userName is None or len(userName) == 0:
        cart = Cart.objects.all()
    else:
        cart = Cart.objects.filter(user=userName)
    context = {
        "user": request.user,
        "menu": Item.objects.all(),
        "cost": Price.objects.all(),
        "itemGroup":ItemGroup.objects.all(),
        "cart":cart
    }

    return render(request,"orders/index.html", context)


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    print(username)
    print(password)
    print(user)
    if user is not None:
        print(user)
        login(request, user)
        print("test")
        return HttpResponseRedirect(reverse("index"))
    else:
        print("test1")
        return render(request, "orders/login.html", {"message": "Invalid credentials"})


def newuser_view(request):
    print("newuser_view")
    if request.method == 'GET':
        return render(request, "orders/newuser.html")
    if request.method == 'POST':
        username = request.POST["usernme"]
        password = request.POST["passwrd"]
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        email1 = request.POST["email"]
        hashedPassword = make_password(password)
        print(username)
        print(password)
        # print(first_name)
        # print(last_name)
        # print(email1)

        if len(email1) > 0:
            newUser = User.objects.create_user(username=username,
                                 email=email1,
                                 password=password)
            newUser.save()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, "orders/login.html", {"message": "Invalid credentials"})

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged Out"})


def cart(request):
    if request.method == 'POST':
        print("Add to cart")
        print(request.POST)
        itemPriceId = request.POST['itemPriceId']
        print(itemPriceId)
        userName = request.user.username
        print(userName)
        cart = Cart(user=userName, quantity = 1, cartItem_id=itemPriceId)
        cart.save()
        return HttpResponseRedirect(reverse("index"))

def my_orders(request):
    print("This is my order")
    print(request.POST)
    userName = request.user.username
    cartItems = Cart.objects.filter(user=userName)
    prices = []
    for i in cartItems:
        prices.append(i.cartItem.price)

    context = {
         "cart" : cartItems,
         "total" : sum(prices)
    }

    return render(request,"orders/checkout.html", context)

def cartItemDelete(request):
    print("Delete to cart")
    cartItemId = request.POST['cartItemId']
    print(cartItemId)
    userName = request.user.username
    print(userName)
    Cart.objects.filter(id=cartItemId).delete()
    return HttpResponseRedirect(reverse("orderItem"))




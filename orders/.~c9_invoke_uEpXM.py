from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.urls import reverse
from .models import Item, Price, ItemGroup
from django.http import JsonResponse

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message" : None})
    context = {
        "user": request.user,
        "menu": Item.objects.all(),
        "cost": Price.objects.all(),
        "itemGroup":ItemGroup.objects.all()

    }

    return render(request,"orders/index.html", context)


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))

    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials"})

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged Out"})


# @require_http_methods(["GET", "POST"])
def add_to_cart(request):
    if request.method == 'POST':
        print("Add to cart")
        print(request.POST)
        itemPriceId = request.POST['itemPriceId']
        print(itemPriceId)
        # cost = Price.objects.get(pk=cartItems.id) #getting the liked posts
        # m = Cart(post=cost) # Creating Cart Object
        # m.save()  # saving it to store in database
        return HttpResponse("Item added succesfully in cart!") #


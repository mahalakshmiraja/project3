from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("newuser", views.newuser_view, name="newuser"),
    path("cartItem", views.cart, name="cartItem"),
    path("orderItem", views.my_orders, name="orderItem"),
    path("cartItemDelete", views.cartItemDelete, name="cartItemDelete")
 ]

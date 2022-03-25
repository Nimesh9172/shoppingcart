from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [

    path('',views.store,name="store"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('updateitem/',views.updateItem,name="updateitem"),
    path("processorder/",views.processOrder,name="processorder"),


    path("login/",views.CustomLoginView.as_view(), name="login"),
    path("logout/",LogoutView.as_view(next_page='login'), name="logout"),
    path("register/",views.RegisterPage.as_view(),name='register'),
]
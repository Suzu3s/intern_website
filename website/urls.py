from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    
    path('navbar/', views.navbar),
    path('contact/', views.contact, name="contact"),
    path('About_us/', views.about_us, name="about_us"),
    path('delivery/', views.delivery, name="delivery"),

    path('register/', views.registerPage, name="register"),

	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    path('products/', views.products, name="products"),
    path('cart/', views.cart, name="cart"),


]
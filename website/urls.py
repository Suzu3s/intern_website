from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    
    path('navbar/', views.navbar),
    path('contact/', views.contact, name="contact"),

    path('register/', views.registerPage, name="register"),

	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

]
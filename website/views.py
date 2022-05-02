import email
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth.models import User, auth

from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'website/index.html')




    #----------------------------------------original
def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				print("account has been created")
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'website/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'website/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')



def navbar(request):
     return render(request, 'website/navbar.html')        


def contact(request):
    return render(request, 'website/contact.html')
    return redirect('home')

def about_us(request):
    return render(request, 'website/About_us.html')
    return redirect('home')


def delivery(request):
     return render(request, 'website/delivery.html')	

def products(request):
	return render(request, 'website/products.html')
	return redirect('home')

def cart(request):
	return render(request, 'website/cart.html')
	return redirect('home')	

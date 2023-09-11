from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, CustomLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


#register view
def registerview(request):
    if request.method== "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid:
            user= form.save()
            login(request, user)
            return redirect('home')
        else:
            form= RegistrationForm()
    
    context={
        'form':form
    }
    return render(request, 'registration.html', context)

#login view

def custom_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a success page or home page
            elif user is None:
                messages.error(request, "email or password incorrect")
                return redirect('login')
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})

#home view
@login_required(login_url= 'login')
def homepage(request):
    return render(request, 'homepage.html')

# Create your views here.

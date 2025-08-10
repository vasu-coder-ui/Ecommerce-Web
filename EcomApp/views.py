from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

from django.contrib import messages
from .forms import SignUpForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  # Saves user to DB
            messages.success(request, "Your account has been created! You can now log in.")
            return redirect('/signin_page/')  # Replace with your login URL name
    else:
        form = SignUpForm()
    return render(request, 'EcomApp/signup.html',{'form':form})




from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {username}!")
            return redirect("/home_page/")  # Redirect to home page
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")

    return render(request, "EcomApp/signin.html")


def home_view(request):
    return render(request, "EcomApp/home.html")



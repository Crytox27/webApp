from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegistrationForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = RegistrationForm()
    return render(response, "users/register.html", {"form":form})

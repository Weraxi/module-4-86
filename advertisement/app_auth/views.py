from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
# from django.urls import reverse
from django.contrib.auth import login, logout, authenticate

from .forms import MyUserCreationForm


@login_required(login_url=reverse_lazy("login"))
def profile_view(request):
    return render(request, "app_auth/profile.html")


def login_view(request):
    redirect_url = reverse("profile")
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, "app_auth/login.html")

    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect(redirect_url)

    context = {"error": "Пользователь не найден"}

    return render(request, "app_auth/login.html", context=context)


def logout_view(request):
    redirect_url = reverse("login")
    logout(request)
    return redirect(redirect_url)


def register_view(request):
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=request.POST["password1"])
            login(request, user=user)
            return redirect(reverse("profile"))
    else:
        form = MyUserCreationForm()
    context = {
        "form": form
    }
    return render(request, "app_auth/register.html", context)

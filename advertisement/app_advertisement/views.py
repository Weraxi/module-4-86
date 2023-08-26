from django.shortcuts import render, reverse, redirect
from .models import Advertisement
from .forms import AdvertisementForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
def index(request):
    advertisements = Advertisement.objects.all()
    context = {"advertisements": advertisements}
    return render(request, "app_advertisement/index.html", context=context)
def top_sellers(request):
    return render(request, "app_advertisement/top-sellers.html")

@login_required(login_url=reverse_lazy("login"))
def post_advertisement(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = form.save(commit=False)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {"form": form}
    return render(request, "app_advertisement/advertisement-post.html", context)
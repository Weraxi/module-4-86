from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.db.models import Count

from .models import Advertisement
from .forms import AdvertisementForm


User = get_user_model()


def index(request):
    title = request.GET.get("query")
    if title:
        advertisements = Advertisement.objects.filter(title__iexact=title)
    else:
        advertisements = Advertisement.objects.all()
    context = {"advertisements": advertisements, "title": title}

    return render(request, "app_advertisement/index.html", context=context)


def top_sellers(request):
    users = User.objects.annotate(
        adv_count=Count("advertisement")
    ).order_by('-adv_count')

    context = {
        "users": users
    }
    print(users[0].username)
    return render(request, "app_advertisement/top-sellers.html", context=context)


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


def advertisement_view(request, pk):
    advertisement = Advertisement.objects.get(pk=pk)
    context = {
        "advertisement": advertisement,
    }
    return render(request, "app_advertisement/advertisement.html", context)
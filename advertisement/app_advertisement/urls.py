from django.urls import path
from .views import index, top_sellers, post_advertisement, advertisement_view
urlpatterns = [
    path("", index, name="main-page"),
    path("top-sellers/", top_sellers, name="top-sellers"),
    path('advertisement-post/', post_advertisement, name="adv-post"),
    path("advertisement/<int:pk>", advertisement_view, name="adv"),
]
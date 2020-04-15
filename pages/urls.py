from django.urls import path
from .views import HomePageView,AboutPageView,ContactPageView,GalleryView


urlpatterns = [
    path('',HomePageView.as_view(),name="home"),
    path('about/',AboutPageView.as_view(),name="about"),
    path('contact/',ContactPageView.as_view(),name="contact"),
    path('gallery/',GalleryView.as_view(),name='gallery'),
]
from django.urls import path
from .views import UpdateProfileView

urlpatterns = [
    path('edit/',UpdateProfileView.as_view(),name='edit-profile')
]
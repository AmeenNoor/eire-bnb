from django.urls import path
from .views import AccommodationList

urlpatterns = [
    path('accommodations/', AccommodationList.as_view(), name='accommodation_list'),
]

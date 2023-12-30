from django.urls import path
from .views import AccommodationList, AccommodationDetail

urlpatterns = [
    path('accommodation/', AccommodationList.as_view(), name='accommodation_list'),
    path('accommodation/<int:pk>', AccommodationDetail.as_view(),
         name='accommodation_detail'),
]

from django.urls import path
from .views import Home, AccommodationList, AccommodationDetail, BookAccommodationView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('accommodation/', AccommodationList.as_view(), name='accommodation_list'),
    path('accommodation/<int:pk>', AccommodationDetail.as_view(),
         name='accommodation_detail'),
    path('accommodation/<int:pk>/booking', BookAccommodationView.as_view(),
         name='book_accommodation'),
]

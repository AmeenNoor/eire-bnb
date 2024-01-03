from django.urls import path
from .views import Home, AccommodationList, AccommodationDetail, BookAccommodationView, BookingHistoryView, UpdateBookingView, CancelBookingView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('accommodation/', AccommodationList.as_view(), name='accommodation_list'),
    path('accommodation/<int:pk>', AccommodationDetail.as_view(),
         name='accommodation_detail'),
    path('accommodation/<int:pk>/booking', BookAccommodationView.as_view(),
         name='book_accommodation'),
    path('booking/history/', BookingHistoryView.as_view(), name='booking_history'),
    path('booking/update/<int:pk>/',
         UpdateBookingView.as_view(), name='update_booking'),
    path('booking/cancel/<int:pk>/',
         CancelBookingView.as_view(), name='cancel_booking'),
]

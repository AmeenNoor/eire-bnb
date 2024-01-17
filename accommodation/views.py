from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Accommodation, Booking
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms



class Home(TemplateView):
    """
    View to display Home page
    """
    template_name = 'home.html'


class AccommodationList(ListView):
    """
    View to display all list of all accommodations with their attributes
    """
    model = Accommodation
    context_object_name = 'accommodations'
    template_name = 'accommodation_list.html'


class AccommodationDetail(DetailView):
    """
    View to display accommodation details
    """
    model = Accommodation
    template_name = 'accommodation_detail.html'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'phone_number', 'email',
                  'number_of_guests', 'check_in_date', 'check_out_date']
        widgets = {
            'check_in_date': forms.DateInput(attrs={'type': 'date'}, format='%d/%m/%Y'),
            'check_out_date': forms.DateInput(attrs={'type': 'date'}, format='%d/%m/%Y'),
        }


class BookAccommodationView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'book_accommodation.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        accommodation_id = self.kwargs.get('pk')
        accommodation = Accommodation.objects.get(pk=accommodation_id)
        form.instance.accommodation = accommodation
        form.save()
        return super().form_valid(form)


class BookingHistoryView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking_history.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class UpdateBookingView(LoginRequiredMixin, UpdateView):
    model = Booking
    fields = ['first_name', 'last_name',
              'phone_number', 'email', 'number_of_guests', 'check_in_date', 'check_out_date', 'accommodation']
    template_name = 'update_booking.html'
    success_url = reverse_lazy('booking_history')

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class CancelBookingView(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = 'cancel_booking.html'
    success_url = reverse_lazy('booking_history')

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

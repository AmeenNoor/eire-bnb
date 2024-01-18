from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Accommodation, Booking
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.utils import timezone
from django.contrib import messages
from django.core.exceptions import ValidationError


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

    def clean(self):
        cleaned_data = super().clean()
        check_in_date = cleaned_data.get('check_in_date')
        check_out_date = cleaned_data.get('check_out_date')

        if check_in_date and check_in_date < timezone.now().date():
            raise ValidationError('Check-in date must be in the future.')

        if check_out_date and (check_out_date <= check_in_date or check_out_date < timezone.now().date()):
            raise ValidationError('Ensure that the check-out date is later than the check-in date ')

class BookAccommodationView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'book_accommodation.html'
    success_url = reverse_lazy('booking_history')

    def form_valid(self, form):
        form.instance.user = self.request.user
        accommodation_id = self.kwargs.get('pk')
        accommodation = Accommodation.objects.get(pk=accommodation_id)
        form.instance.accommodation = accommodation

        existing_bookings = Booking.objects.filter(
            accommodation=accommodation,
            check_out_date__gt=form.cleaned_data['check_in_date'],
            check_in_date__lt=form.cleaned_data['check_out_date'],
        )

        if existing_bookings.exists():
            messages.error(
                self.request, 'Accommodation is not available for the selected dates.')
            return self.form_invalid(form)

        form.save()
        messages.success(self.request, 'Booking successful!',
                         extra_tags='success_booking')
        # https://stackoverflow.com/questions/43588876/how-can-i-add-additional-data-to-django-messages
        return super().form_valid(form)

class BookingHistoryView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking_history.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class UpdateBookingView(LoginRequiredMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'update_booking.html'
    success_url = reverse_lazy('booking_history')

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        accommodation_id = form.instance.accommodation.pk
        accommodation = Accommodation.objects.get(pk=accommodation_id)

        existing_bookings = Booking.objects.filter(
            accommodation=accommodation,
            check_out_date__gt=form.cleaned_data['check_in_date'],
            check_in_date__lt=form.cleaned_data['check_out_date'],
        )

        if existing_bookings.exists():
            messages.error(
                self.request, 'Accommodation is not available for the selected dates.')
            return self.form_invalid(form)

        messages.success(
            self.request, 'Booking updated successfully!', extra_tags='update_booking')
        return super().form_valid(form)


class CancelBookingView(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = 'cancel_booking.html'
    success_url = reverse_lazy('booking_history')

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request, 'Booking canceled successfully!', extra_tags='cancel_booking')
        return super().delete(request, *args, **kwargs)


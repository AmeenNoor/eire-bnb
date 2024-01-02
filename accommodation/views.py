from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Accommodation, Booking
from django.urls import reverse_lazy


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


class BookAccommodationView(CreateView):
    model = Booking
    fields = ['first_name', 'last_name',
              'phone_number', 'email', 'number_of_guests', 'check_in_date', 'check_out_date']
    template_name = 'book_accommodation.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        # Ensure the correct kwarg name is used here
        accommodation_id = self.kwargs.get('pk')
        accommodation = Accommodation.objects.get(pk=accommodation_id)
        form.instance.accommodation = accommodation
        form.save()  # Save the form to commit the booking
        return super().form_valid(form)

from django.shortcuts import render
from django.views.generic import ListView
from .models import Accommodation


class AccommodationList(ListView):
    """
    View to display all list of all accommodations with their attributes
    """
    model = Accommodation
    queryset = Accommodation.objects.all()
    template_name = 'accommodation_list.html'

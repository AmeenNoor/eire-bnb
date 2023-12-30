from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Accommodation


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

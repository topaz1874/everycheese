from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from .models import Cheese

class CheeseListView(ListView):
    model = Cheese

class CheeseDetailView(DetailView):
    model = Cheese
    
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.
from .models import Cheese

class CheeseListView(ListView):
    model = Cheese

class CheeseDetailView(DetailView):
    model = Cheese

class CheeseCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Cheese
    fields = ('name', 'description', 'firmness', 'country_of_origin')
    success_message = "New cheese created!"

class CheeseUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Cheese
    fields = ('name', 'description', 'firmness', 'country_of_origin')
    success_message = "You've updated successed!"
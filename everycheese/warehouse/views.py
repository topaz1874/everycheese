#-*-coding:utf-8 -*-

from django.shortcuts import render, Http404

# Create your views here.
from django.forms import ModelForm
from django.forms import widgets
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import WarehouseItem, Trans


class WarehouseListView(ListView):
    model = WarehouseItem
    template_name = 'warehouse/warehouse_list.html'


class WarehouseCreateView(CreateView):
    model = WarehouseItem
    template_name = 'warehouse/warehouse_form.html'
    fields = '__all__'
    success_url = '/warehouse'

class TransCreateForm(ModelForm):
    class Meta:
        model = Trans
        fields = '__all__'
        widgets = {'trans_date': widgets.SelectDateWidget(),}


class TransCreateView(CreateView):
    model = Trans
    form_class = TransCreateForm
    template_name = 'warehouse/warehouse_form.html'
    success_url = '/warehouse'


    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = self.get_form()
        if form.is_valid():
            trans_item = form.cleaned_data['item']
            trans_amount =  form.cleaned_data['trans_amount']
            trans_item.amount += trans_amount
            trans_item.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class WarehouseDetailView(DetailView):
    model = WarehouseItem
    template_name = 'warehouse/warehouse_detail.html'

    # queryset = WarehouseItem.objects.filter(trans__trans_amount__gt=0)
    
    # def get_object(self, queryset=None):
    #     obj = super(WarehouseDetailView, self).get_object()
    #     print obj
    #     return obj

    # def get_queryset(self):
    #     qs = super(WarehouseDetailView, self).get_queryset()
    #     return qs

    # def get_context_data(self, **kwargs):
    #     context = super(WarehouseDetailView, self).get_context_data(**kwargs)
    #     # obj = context['object']
    #     # context['tran_in'] = obj.trans_set.filter(trans_amount__gt=0)
    #     print context
    #     return context

class WarehouseUpdateView(UpdateView):
    model = WarehouseItem
    fields = '__all__'
    template_name = 'warehouse/warehouse_form.html'
    success_url = '/warehouse'

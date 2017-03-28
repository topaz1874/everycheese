#-*-coding:utf-8 -*-

from django.shortcuts import render, Http404

# Create your views here.
from django.forms import ModelForm
from django.forms import widgets
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.dates import DateDetailView,DayArchiveView
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

class TransDetailView(DayArchiveView):
    model = Trans
    date_field = "trans_date"
    queryset = Trans.objects.all()

    def get_context_data(self, **kwargs):
        
        day_items = self.get_dated_items()[2]
        previous_day =  day_items.get('previous_day', None)
        next_day = day_items.get('next_day', None)
        if previous_day:
            previous_day = Trans.objects.filter(trans_date=previous_day)[0]
            kwargs['previous_url'] = previous_day.get_absolute_url()
        if next_day:
            next_day = Trans.objects.filter(trans_date=next_day)[0]
            kwargs['next_url'] = next_day.get_absolute_url()

        return super(TransDetailView, self).get_context_data(**kwargs)


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


from django.http import JsonResponse
from django.template.loader import render_to_string

class WarehouseItemForm(ModelForm):
    class Meta:
        model = WarehouseItem
        fields = '__all__'

def warehousejscreate(request):

    form = WarehouseItemForm()
    context = {'form': form}
    html_form = render_to_string('warehouse/item_form.html',context, request=request)

    return JsonResponse({'html_form': html_form})






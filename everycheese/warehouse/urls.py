from django.conf.urls import url
from . import views

urlpatterns = (
    url(
        regex=r'^$',
        view=views.WarehouseListView.as_view(),
        name='list'),
    url(
        r'^add/$',
        views.TransCreateView.as_view(),
        name='add'),
    url(
        r'^create/$',
        views.WarehouseCreateView.as_view(),
        name='create'),  
     url(
        r'^(?P<slug>[-\w]+)/$',
        views.WarehouseDetailView.as_view(),
        name='detail'),
     url(
        r'^(?P<slug>[-\w]+)/update/$',
        views.WarehouseUpdateView.as_view(),
        name='update'),
 
    )
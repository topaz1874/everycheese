from django.conf.urls import url
from . import views

urlpatterns = (
    url(
        regex=r'^$',
        view=views.CheeseListView.as_view(),
        name='list'),
     url(
        r'^create/$',
        views.CheeseCreateView.as_view(),
        name='create'),   
     url(
        r'^(?P<slug>[-\w]+)/$',
        views.CheeseDetailView.as_view(),
        name='detail'),
     url(
        r'^(?P<slug>[-\w]+)/update/$',
        views.CheeseUpdateView.as_view(),
        name='update'),

    )
from django.conf.urls import url
from . import views

urlpatterns = (
    url(
        regex=r'^$',
        view=views.CheeseListView.as_view(),
        name='list'),
    url(
        r'^(?P<slug>[-\w]+)/$',
        views.CheeseDetailView.as_view(),
        name='detail'),

    )
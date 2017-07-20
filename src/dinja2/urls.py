# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'dinja2'

urlpatterns = [
    url(r'', TemplateView.as_view(template_name="dinja2/base.html")),

    # SomeModel
    url(r"^SomeModel/$", view=views.SomeModelList.as_view(), name='SomeModelList'),
    url(r"^SomeModel/create$", view=views.SomeModelCreate.as_view(), name='SomeModelCreate'),
    url(r"^SomeModel/(?P<pk>\d+)/delete$", view=views.SomeModelDelete.as_view(), name='SomeModelDelete'),
    url(r"^SomeModel/(?P<pk>\d+)/update$", view=views.SomeModelUpdate.as_view(), name='SomeModelUpdate'),
    url(r"^SomeModel/(?P<pk>\d+)/$", view=views.SomeModelDetail.as_view(), name='SomeModelDetail'),

    # AndAnother
    url(r"^AndAnother/$", view=views.AndAnotherList.as_view(), name='AndAnotherList'),
    url(r"^AndAnother/create$", view=views.AndAnotherCreate.as_view(), name='AndAnotherCreate'),
    url(r"^AndAnother/(?P<pk>\d+)/delete$", view=views.AndAnotherDelete.as_view(), name='AndAnotherDelete'),
    url(r"^AndAnother/(?P<pk>\d+)/update$", view=views.AndAnotherUpdate.as_view(), name='AndAnotherUpdate'),
    url(r"^AndAnother/(?P<pk>\d+)/$", view=views.AndAnotherDetail.as_view(), name='AndAnotherDetail'),
]

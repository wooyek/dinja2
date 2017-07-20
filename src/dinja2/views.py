# -*- coding: utf-8 -*-
from django_powerbank.views.auth import StaffRequiredMixin
from django_powerbank.views.mixins import ReturnUrlMx
from pascal_templates.views import CreateView, DeleteView, DetailView, ListView, UpdateView

from . import models


class SomeModelCreate(ReturnUrlMx, StaffRequiredMixin, CreateView):
    model = models.SomeModel


class SomeModelDelete(ReturnUrlMx, StaffRequiredMixin, DeleteView):
    model = models.SomeModel


class SomeModelDetail(StaffRequiredMixin, DetailView):
    model = models.SomeModel


class SomeModelUpdate(ReturnUrlMx, StaffRequiredMixin, UpdateView):
    model = models.SomeModel


class SomeModelList(StaffRequiredMixin, ListView):
    model = models.SomeModel


class AndAnotherCreate(ReturnUrlMx, StaffRequiredMixin, CreateView):
    model = models.AndAnother


class AndAnotherDelete(ReturnUrlMx, StaffRequiredMixin, DeleteView):
    model = models.AndAnother


class AndAnotherDetail(StaffRequiredMixin, DetailView):
    model = models.AndAnother


class AndAnotherUpdate(ReturnUrlMx, StaffRequiredMixin, UpdateView):
    model = models.AndAnother


class AndAnotherList(StaffRequiredMixin, ListView):
    model = models.AndAnother

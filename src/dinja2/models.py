# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_powerbank.db.models.base import BaseModel


class SomeModel(BaseModel):
    foo = models.CharField(verbose_name=_("foo"), max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = _('somemodel')


class AndAnother(BaseModel):
    foo = models.CharField(verbose_name=_("foo"), max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = _('andanother')

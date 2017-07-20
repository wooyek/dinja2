#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_dinja2
------------

Tests for `dinja2` models module.
"""

from django.test import TestCase

from dinja2 import models
from tests import factories


class TestDinja2(TestCase):

    def test_something(self):
        assert models
        factories.UserFactory

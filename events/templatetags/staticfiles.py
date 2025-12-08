"""Compat shim so `{% load staticfiles %}` keeps working under Django 5."""

from django.templatetags.static import register  # re-export built-in static tags


__all__ = ["register"]

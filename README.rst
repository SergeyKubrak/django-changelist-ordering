

Usage
===============

settings.py
-------
::

    INSTALLED_APPS = (
        ...
        'changelist_ordering',
    )

model.py
-------
::

    from django.db import models

    class Example(models.Model):
        title = models.CharField(max_length=100)
        order = models.IntegerField(max_length=3, default=999)


admin.py
-------
::

    from django.contrib import admin
    from changelist_ordering.admin import ChangeListOrdering

    class ExampleAdmin(ChangeListOrdering):
        ordering = ('order',)

    admin.site.register(Example, ExampleAdmin)



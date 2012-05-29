

Usage
===============

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
    from changelist_ordering import ChangeListOrdering

    class ExampleAdmin(ChangeListOrdering):
        ordering = ('order',)

    admin.site.register(Example, ExampleAdmin)



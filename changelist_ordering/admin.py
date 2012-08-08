import json
from django.contrib import admin
from django.http import HttpResponseBadRequest, HttpResponse
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _, ugettext

class ChangeListOrdering(admin.ModelAdmin):

    def __init__(self, *args, **kwargs):
        super(ChangeListOrdering, self).__init__(*args, **kwargs)

        self.list_display = list(self.list_display)

        self.change_list_template = [
            'changelist_ordering.html',
            ]

    def changelist_view(self, request, extra_context=None, *args, **kwargs):
        """
        Handle the changelist view, the django view for the model instances
        change list/actions page.
        """

        if 'actions_column' not in self.list_display:
            self.list_display.append('actions_column')

        # handle common AJAX requests
        if request.is_ajax():
            cmd = request.POST.get('__cmd')
            if cmd == 'change_ordering':
                return self._change_ordering(request)
            else:
                return HttpResponseBadRequest('Oops. AJAX request not understood.')

        self._refresh_changelist_caches()


        return super(ChangeListOrdering, self).changelist_view(request, extra_context, *args, **kwargs)


    def _actions_column(self, instance):
        return ['<span id="page_marker-%d" class="page_marker">&nbsp;</span>&nbsp;<div class="drag_handle"></div>'% instance.id,]

    def actions_column(self, instance):
            return u' '.join(self._actions_column(instance))

    actions_column.allow_tags = True
    actions_column.short_description = _('ordering')

    def _refresh_changelist_caches(self):
        """
        Refresh information used to show the changelist tree structure such as
        inherited active/inactive states etc.

        XXX: This is somewhat hacky, but since it's an internal method, so be it.
        """

        pass

    def _change_ordering(self, request):
        position = json.loads(request.POST['position'])

        for value in position:
            self.model.objects.filter(pk=value).update(order=position.index(value))

        return HttpResponse('OK')
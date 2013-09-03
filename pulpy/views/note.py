from datetime import datetime
from pyramid.response import Response
from sqlalchemy.exc import DBAPIError

from pyramid.httpexceptions import (
    HTTPNotFound,
    HTTPFound,
    HTTPForbidden,
)
from pyramid.security import (
    remember,
    forget,
    authenticated_userid
)
from pyramid.view import (
    view_config,
)
from pulpy.models.meta import DBSession
from pulpy.models import (
    Note,
)

from pulpy.forms import (
    NoteCreateForm,
)


class NoteViews(object):

    def __init__(self, request):
        self.request = request

    @view_config(route_name='index',
                 renderer='pulpy:templates/note/list.mako',
                 permission='view')
    def notes(self):
        """ Get a paginated list of notes. """

        page = int(self.request.params.get('page', 1))
        notes = Note.page(self.request, page)
        return {'paginator': notes,
                'title': 'My notes',
                }

    @view_config(route_name='note_new',
                 renderer='pulpy:templates/note/edit.mako',
                 permission='create')
    def note_create(self):
        """ New note view. """

        form = NoteCreateForm(self.request.POST,
                                  csrf_context=self.request.session)

        if self.request.method == 'POST' and form.validate():
            n = Note()
            form.populate_obj(n)
            n.user_id = authenticated_userid(self.request)
            DBSession.add(n)
            self.request.session.flash('Note %s created' %
                                       (n.title), 'success')
            return HTTPFound(location=self.request.route_url('index'))
        return {'title': 'New note',
                'form': form,
                'action': 'note_new'}

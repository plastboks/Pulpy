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
    Noterevision,
)

from pulpy.forms import (
    NoteCreateForm,
    NoteEditForm,
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
            nr = Noterevision()
            nr.body = form.body.data
            del form.body

            n = Note()
            form.populate_obj(n)
            n.user_id = authenticated_userid(self.request)
            DBSession.add(n)
            DBSession.flush()

            nr.note_id = n.id
            DBSession.add(nr)
            self.request.session.flash('Note %s created' %
                                       (n.title), 'success')
            return HTTPFound(location=self.request.route_url('index'))
        return {'title': 'New note',
                'form': form,
                'action': 'note_new'}

    @view_config(route_name='note_edit',
                 renderer='pulpy:templates/note/edit.mako',
                 permission='edit')
    def note_edit(self):
        """ Edit note view. """

        id = int(self.request.matchdict.get('id'))

        n = Note.by_id(id)
        if not n:
            return HTTPNotFound()

        """ Authorization check. """
        if n.user_id is not authenticated_userid(self.request):
            return HTTPForbidden()

        form = NoteEditForm(self.request.POST, n,
                                csrf_context=self.request.session)

        if self.request.method == 'POST' and form.validate():
            nr = Noterevision()
            nr.body = form.body.data
            del form.body

            form.populate_obj(n)

            nr.note_id = n.id
            DBSession.add(nr)

            self.request.session.flash('Note %s updated' %
                                       (n.title), 'status')
            return HTTPFound(location=self.request.route_url('index'))

        # get the last revision and insert into body
        form.body.data = n.revisions[-1].body
        return {'title': 'Edit note',
                'form': form,
                'id': id,
                'note': n,
                'action': 'note_edit'}

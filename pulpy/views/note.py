from datetime import datetime
from pyramid.response import Response
from sqlalchemy.exc import DBAPIError
from markdown import Markdown
from hashlib import sha1

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

import transaction


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

            self.request.session.flash('Note "%s" created' %
                                       (n.title), 'success')
            return HTTPFound(location=self.request.route_url('note_view',
                                                             id=n.id))
        return {'title': 'New note',
                'form': form,
                'revisions': False,
                'action': 'note_new'}

    @view_config(route_name='note_view',
                 renderer='pulpy:templates/note/view.mako',
                 permission='view')
    def note_view(self):
        """ Note view. """

        id = int(self.request.matchdict.get('id'))

        n = Note.by_id(id)
        if not n:
            return HTTPNotFound()

        """ Authorization check. """
        if n.user_id is not authenticated_userid(self.request):
            return HTTPForbidden()

        md = Markdown(output_format='html5')
        cur_revision = n.revisions[-1]

        return {'note': n,
                'title': n.title,
                'body': md.convert(cur_revision.body),
                }

    @view_config(route_name='note_edit',
                 renderer='pulpy:templates/note/edit.mako',
                 permission='edit')
    def note_edit(self):
        """ Edit note view. """

        id = int(self.request.matchdict.get('id'))
        revision = self.request.params.get('revision')

        n = Note.by_id(id)
        if not n:
            return HTTPNotFound()

        """ Authorization check. """
        if n.user_id is not authenticated_userid(self.request):
            return HTTPForbidden()

        form = NoteEditForm(self.request.POST, n,
                            csrf_context=self.request.session)
        cur_revision = n.revisions[-1]

        if self.request.method == 'POST' and form.validate():
            # generate a sha1 hash from both the new and old
            # revision body, then compare them. Only if these
            # hashes do not compare, create a new revision.
            sha1_cur = sha1(cur_revision.body).hexdigest()
            sha1_new = sha1(form.body.data).hexdigest()
            if sha1_cur != sha1_new:
                nr = Noterevision()
                nr.body = form.body.data
                nr.note_id = n.id
                DBSession.add(nr)
                DBSession.flush()
            del form.body

            form.populate_obj(n)
            DBSession.add(n)

            self.request.session.flash('Note "%s" updated' %
                                       (n.title), 'status')
            return HTTPFound(location=self.request.route_url('note_view',
                                                             id=n.id))

        # Get the current revision and insert into form body.
        # This seems a bit retarted, and the current revision object
        # should maybe be a foreign object in the database.
        if (revision
           and filter(lambda rev: rev.id == int(revision), n.revisions)):
            form.body.data = Noterevision().by_id(int(revision)).body
            displayed_revision = revision
        else:
            form.body.data = cur_revision.body
            displayed_revision = cur_revision.id

        return {'title': 'Edit note',
                'form': form,
                'id': id,
                'note': n,
                'revisions': [(r) for r in reversed(n.revisions)],
                'revision': displayed_revision,
                'action': 'note_edit'}

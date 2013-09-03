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

from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from pyramid.httpexceptions import (
    HTTPFound,
    HTTPNotFound,
)

from pyramid.view import (
    view_config,
    forbidden_view_config,
    notfound_view_config,
)

class MainViews(object):

    def __init__(self, request):
        self.request = request

    @notfound_view_config(renderer='pulpy:templates/error/notfound.mako')
    def notfound(self):
        """ Not found view """
        return {'title': '404 - Page not found',
                'message': '"%s" is not the page you are looking for' %
                           self.request.path
                }

    @forbidden_view_config(renderer='string')
    def forbidden(self):
        """ Forbidden view """
        return HTTPFound(self.request.route_url('login'))

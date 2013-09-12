from datetime import datetime
from pyramid.response import Response
from sqlalchemy.exc import DBAPIError

from pyramid.httpexceptions import (
    HTTPNotFound,
    HTTPFound,
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
    User,
)
from pulpy.forms import (
    AccountEditForm,
)


class AccountViews(object):

    def __init__(self, request):
        self.request = request

    @view_config(route_name='profile',
                 renderer='pulpy:templates/account/profile.mako',
                 permission='edit')
    def profile(self):
        """ Edit self user view. Method handles both post and get
        requests.
        """

        a = authenticated_userid(self.request)
        u = User.by_id(a)
        form = AccountEditForm(self.request.POST,
                               u,
                               csrf_context=self.request.session)

        if self.request.method == 'POST' and form.validate():
            form.populate_obj(u)
            u.id = a
            if u.password:
                u.password = u.pm.encode(form.password.data)
            else:
                del u.password
            self.request.session.update({'dateformat': u.datetime_format})
            self.request.session.flash('User %s updated' %
                                       (u.email), 'status')
            return HTTPFound(location=self.request.route_url('profile'))
        return {'title': 'Profile edit',
                'form': form,
                'myid': a,
                'user': u,
                'action': 'profile'
                }

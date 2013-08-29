from pyramid.threadlocal import get_current_request

from pyramid.security import (
    Allow,
    Everyone,
    Authenticated,
    authenticated_userid,
    has_permission,
)

from pulpy.models import User


class EntryFactory(object):
    """
    A standard Pyramid EntryFactory object snagged and extended
    from one of the pyramid tutorials @ readthedocs.

    This is just a simple mockup class for the begining of the
    project.
    """
    __name__ = None
    __parent__ = None
    __acl__ = [(Allow, Authenticated, 'view'),
               (Allow, Authenticated, 'create'),
               (Allow, Authenticated, 'edit'),
               ]

    def __init__(self, request):
        pass


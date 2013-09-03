from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from pyramid.authentication import (
    AuthTktAuthenticationPolicy,
)
from pyramid.authorization import (
    ACLAuthorizationPolicy,
)
from pyramid.session import (
    UnencryptedCookieSessionFactoryConfig,
)
from pulpy.models.meta import (
    DBSession,
    Base,
)

from pulpy.security import (
    EntryFactory
)


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    authenPol = AuthTktAuthenticationPolicy('somesecret',
                                            hashalg='sha512')
    authorPol = ACLAuthorizationPolicy()
    sess_factory = UnencryptedCookieSessionFactoryConfig('someothersecret')

    config = Configurator(settings=settings,
                          authentication_policy=authenPol,
                          authorization_policy=authorPol,
                          root_factory='pulpy.security.EntryFactory',
                          session_factory=sess_factory,)

    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('index', '/')
    config.add_route('note_new', '/note/new')
    config.add_route('note_edit', '/note/edit/{id}')

    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('profile', '/profile')

    config.scan()
    return config.make_wsgi_app()

from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from rockon.resources import Root

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')
    config = Configurator(root_factory=Root, settings=settings, session_factory=session_factory)
    config.add_static_view('static', 'rockon:static')
    config.add_route('list', '/')
    config.add_route('new', '/new')
    config.add_route('close', '/close/{id}')
    config.scan()
    return config.make_wsgi_app()


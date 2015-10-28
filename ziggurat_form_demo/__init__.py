from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a WSGI application.

    It is usually called by the PasteDeploy framework during
    ``paster serve``.
    """
    settings = dict(settings)
    settings.setdefault('jinja2.i18n.domain', 'ziggurat_form_demo')

    config = Configurator(settings=settings)
    config.add_translation_dirs('locale/')
    config.include('pyramid_jinja2')
    config.add_jinja2_extension('jinja2.ext.do')
    config.add_jinja2_search_path('ziggurat_form_demo:templates/')
    config.add_route('/', '/')
    config.add_route('forms', '/form/{view}')
    config.scan()
    config.add_static_view('static', 'static')

    return config.make_wsgi_app()

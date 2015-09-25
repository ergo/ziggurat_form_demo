from pyramid.i18n import TranslationStringFactory
from pyramid.view import view_config
from ziggurat_form.form import ZigguratForm
from .test_schemas import UserSchema

_ = TranslationStringFactory('ziggurat_form_demo')


@view_config(route_name='/', renderer='index.jinja2')
def index(request):
    return {}


@view_config(route_name='forms', match_param='view=basic_form', renderer='index.jinja2')
def basic_form(request):
    data = {'password': 'xx', "phones": [{}], "subperson": {}, "user_name": "us"}

    form = ZigguratForm(UserSchema)
    form.set_data(request.POST)
    if request.method == "POST" and form.validate():
        pass

    return {"form": form}

from pyramid.i18n import TranslationStringFactory
from pyramid.view import view_config, view_defaults
from ziggurat_form.form import ZigguratForm

from .schemas.test_schemas import (
    UserSchema,
    PhonesSchema,
    UserLoginSchema,
    UserRegisterSchema
)
from .schemas.deformdemo_schemas import (
    TextWidgetSchema,
    TextWidgetReadOnly,
    TextWidgetWithCssSchema
)

_ = TranslationStringFactory('ziggurat_form_demo')


@view_config(route_name='/', renderer='index.jinja2')
def index(request):
    return {}


class FormView(object):

    def __init__(self, form, **kwargs):
        self.form = form
        self.kwargs = kwargs

    def form_view(self, request, data):
        form = ZigguratForm(self.form)
        if request.method == 'POST':
            form.set_data(request.POST)
            form.validate()
        elif data:
            form.set_data(data)

        return {"form": form}

    def __call__(self, func):
        def wrapped(View):
            return self.form_view(View.request, func(View.request))
        return wrapped


@view_defaults(route_name="forms", renderer="form_page.jinja2")
class DemoFormView(object):

    def __init__(self, request):
        self.request = request

    @FormView(UserLoginSchema)
    @view_config(match_param='view=user_login_form')
    def user_login_form(self):
        return None

    @FormView(UserRegisterSchema)
    @view_config(match_param='view=user_register_form')
    def user_register_form(self):
        return None

    @FormView(UserSchema)
    @view_config(match_param='view=basic_form')
    def basic_form(self):
        return {'password': 'xx', "phones": [{}], "subperson": {},
                "user_name": "us"}

    @FormView(PhonesSchema)
    @view_config(match_param='view=phones_form')
    def phones_form(self):
        return {
            "prefix": 1,
            "aaaa": "bbbb",
            "phones": [{'number': '1', 'location': 'dadada'},
                       {'y': 5},
                       {'number': 'abc'},
                       {},
                       {'location': 'warsaw', 'number': 123}],
            "suffix": "bla"
        }

    @FormView(TextWidgetSchema)
    @view_config(match_param='view=textwidget_form')
    def textwidget_form(self):
        return None

    @FormView(TextWidgetWithCssSchema)
    @view_config(match_param='view=textwidget_with_css_form')
    def textwidget_with_css_form(self):
        return None

    @FormView(TextWidgetReadOnly)
    @view_config(match_param='view=textwidget_readonly')
    def textwidget_readonly(self):
        return {"text": "I'm readonly text!"}

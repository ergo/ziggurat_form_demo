from pyramid.i18n import TranslationStringFactory
from pyramid.view import view_config, view_defaults
from pyramid.events import subscriber, BeforeRender
from ziggurat_form.form import ZigguratForm

from .schemas.test_schemas import (
    UserSchema,
    PhonesSchema,
    UserLoginSchema,
    SelectWidgetSchema,
    UserRegisterSchema
)
from .schemas.deformdemo_schemas import (
    TextWidgetSchema,
    CheckboxWidgetSchema,
    TextWidgetWithCssSchema,
    TextWidgetReadOnlySchema
)

_ = TranslationStringFactory('ziggurat_form_demo')


@subscriber(BeforeRender)
def add_global(event):
    event['getattr'] = getattr


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
        wrapped.__doc__ = func.__doc__
        return wrapped


@view_defaults(route_name="forms", renderer="form_page.jinja2")
class DemoFormView(object):

    def __init__(self, request):
        self.request = request

    @FormView(UserLoginSchema)
    @view_config(match_param='view=user_login_form')
    def user_login_form(self):
        """ User login
        """

    @FormView(UserRegisterSchema)
    @view_config(match_param='view=user_register_form')
    def user_register_form(self):
        """ User register
        """
        return {'password': 'xx'}

    @FormView(UserSchema)
    @view_config(match_param='view=basic_form')
    def basic_form(self):
        """ Basic form
        """
        return {'password': 'xx', "phones": [{}], "subperson": {},
                "user_name": "us"}

    @FormView(PhonesSchema)
    @view_config(match_param='view=phones_form')
    def phones_form(self):
        """ List of phones
        """
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
        """ Text Input Widget
        """

    @FormView(TextWidgetWithCssSchema)
    @view_config(match_param='view=textwidget_with_css_form')
    def textwidget_with_css_form(self):
        """ Text Input Widget with CSS class
        """

    @FormView(TextWidgetReadOnlySchema)
    @view_config(match_param='view=textwidget_readonly')
    def textwidget_readonly(self):
        """ Text Input Widget readonly"""
        return {"text": "I'm readonly text!"}

    @FormView(SelectWidgetSchema)
    @view_config(match_param='view=selectwidget_schema')
    def selectwidget_schema(self):
        """ Select Widget
        """

    @FormView(CheckboxWidgetSchema)
    @view_config(match_param='view=checkboxwidget_schema')
    def checkboxwidget_schema(self):
        """ Checkbox Widget
        """
        return {'want': False, 'want2': True}

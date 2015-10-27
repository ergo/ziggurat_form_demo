import colander
from ziggurat_form.widgets import (
    TextWidget,
    FormInvalid,
    TupleWidget,
    ConfirmWidget,
    MappingWidget,
    PasswordWidget,
    PositionalWidget
)


class TextWidgetSchema(colander.Schema):
    """
    http://deformdemo.repoze.org/textinput/
    """
    text = colander.SchemaNode(
        colander.String(),
        validator=colander.Length(max=100),
        widget=TextWidget(size=60),
        description='Enter some text')


class TextWidgetWithCssSchema(colander.Schema):
    """
    http://deformdemo.repoze.org/textinput_with_css_class/
    """
    text = colander.SchemaNode(
        colander.String(),
        validator=colander.Length(max=100),
        widget=TextWidget(class_=['ziggurat-widget-with-style', 'test']),
        description='Enter some text')


class TextWidgetReadOnly(colander.Schema):
    text = colander.SchemaNode(
        colander.String(),
        widget=TextWidget(readonly=True),
    )

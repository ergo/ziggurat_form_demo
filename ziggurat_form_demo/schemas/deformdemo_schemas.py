import colander
from ziggurat_form.widgets import (
    TextWidget,
    CheckboxWidget,
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


class TextWidgetReadOnlySchema(colander.Schema):
    text = colander.SchemaNode(
        colander.String(),
        widget=TextWidget(readonly=True),
    )


class CheckboxWidgetSchema(colander.MappingSchema):
    """
    http://deformdemo.repoze.org/checkbox/
    """
    want = colander.SchemaNode(
        colander.Boolean(),
        description='Check this box!',
        widget=CheckboxWidget(),
        title='I Want It!'
    )
    want2 = colander.SchemaNode(
        colander.Boolean(),
        description='Check this box!',
        widget=CheckboxWidget(),
        title='I Want It!'
    )

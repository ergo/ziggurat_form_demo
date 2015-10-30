import colander
from ziggurat_form.widgets import (
    TextWidget,
    HiddenWidget,
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


class FieldDefaultsSchema(colander.Schema):
    """
    http://deformdemo.repoze.org/fielddefaults/
    """
    artist = colander.SchemaNode(
        colander.String(),
        default='Grandaddy',
        description='Song name')
    album = colander.SchemaNode(
        colander.String(),
        default='Just Like the Fambly Cat')
    song = colander.SchemaNode(
        colander.String(),
        description='Song name')


class HiddenMissingSchema(colander.Schema):
    """
    http://deformdemo.repoze.org/hiddenmissing/
    """
    title = colander.SchemaNode(
        colander.String())
    number = colander.SchemaNode(
        colander.Integer(),
        widget=HiddenWidget(),
        missing=colander.null,
    )

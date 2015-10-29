import colander
from ziggurat_form.widgets import (
    TextWidget,
    FormInvalid,
    TupleWidget,
    SelectWidget,
    ConfirmWidget,
    MappingWidget,
    PasswordWidget,
    PositionalWidget
)

choices = (
    ('', '- Select -'),
    ('habanero', 'Habanero'),
    ('jalapeno', 'Jalapeno'),
    ('chipotle', 'Chipotle')
)

grouped_choices = {
    '': (
        ('', '- Select -'),
    ),
    'hot': (
        ('habanero', 'Habanero'),
        ('jalapeno', 'Jalapeno'),
        ('chipotle', 'Chipotle')
    ),
    'honey': (
        ('honey', 'Honey'),
        ('marshmallow', 'Marshmallow'),
    )
}


class Friend(colander.TupleSchema):
    rank = colander.SchemaNode(colander.Int(),
                               validator=colander.Range(0, 9999))
    name = colander.SchemaNode(colander.String())


class Phone(colander.MappingSchema):
    location = colander.SchemaNode(colander.String(),
                                   validator=colander.OneOf(['home', 'work']))
    number = colander.SchemaNode(colander.String())


class Friends(colander.SequenceSchema):
    friend = Friend()


class Phones(colander.SequenceSchema):
    phone = Phone()


class Person(colander.MappingSchema):
    name = colander.SchemaNode(colander.String())
    age = colander.SchemaNode(colander.Int(),
                              validator=colander.Range(0, 200))
    friends = Friends()
    phones = Phones()


class AddressSchema(colander.MappingSchema):
    street = colander.SchemaNode(
        colander.String(), validator=colander.Length(min=3))
    city = colander.SchemaNode(
        colander.String(), validator=colander.Length(min=3))


def test_validator(field):
    # print('validating', field, field.form)
    raise FormInvalid("Custom validation error")
    return True


def username_validator(field):
    if field.data == 'admin':
        return True

    raise FormInvalid('Custom validation message: Needs to be "admin"')


class UserSchema(colander.MappingSchema):
    user_name = colander.SchemaNode(
        colander.String(),
        validator=colander.Length(min=3),
        widget=TextWidget(validators=[test_validator]))
    password = colander.SchemaNode(colander.String(),
                                   validator=colander.Length(min=3),
                                   title='Lilu Dallas Multipass!',
                                   description="Korben nice!",
                                   zorg='Not nice!',
                                   widget=TextWidget())
    email = colander.SchemaNode(colander.String(),
                                validator=colander.Length(min=3))

    address = AddressSchema()

    phones = Phones()

    optional_field = colander.SchemaNode(
        colander.String(), missing='OK',
        widget=TextWidget(validators=[test_validator]))

    subperson = Person()


class PhonesSchema(colander.MappingSchema):
    prefix = colander.SchemaNode(
        colander.String(), validator=colander.Length(min=3),
        widget=TextWidget(validators=[test_validator]))
    phones = Phones(widget=PositionalWidget(validators=[test_validator]))
    suffix = colander.SchemaNode(
        colander.String(), validator=colander.Length(min=3))


class UserLoginSchema(colander.MappingSchema):
    username = colander.SchemaNode(
        colander.String(), validator=colander.Length(min=3),
        widget=TextWidget(validators=[username_validator]),
        description='Value of "admin" will pass')

    password = colander.SchemaNode(
        colander.String(), validator=colander.Length(min=3),
        widget=PasswordWidget())


class UserRegisterSchema(colander.MappingSchema):
    username = colander.SchemaNode(
        colander.String(), validator=colander.Length(min=3),
        widget=TextWidget(validators=[username_validator]),
        description='Value of "admin" will pass')

    password = colander.SchemaNode(
        colander.String(), validator=colander.Length(min=3),
        widget=ConfirmWidget(PasswordWidget()))

    email = colander.SchemaNode(colander.String(), validator=colander.Email())


class SelectWidgetSchema(colander.MappingSchema):
    select = colander.SchemaNode(
        colander.String(),
        validator=colander.OneOf([x[0] for x in choices]),
        widget=SelectWidget(values=choices)
    )
    grouped_select = colander.SchemaNode(
        colander.String(),
        validator=colander.OneOf([x[0] for x in choices]),
        widget=SelectWidget(values=grouped_choices)
    )


class GroupSchema(colander.MappingSchema):
    pass

group_schema = GroupSchema()
group_schema.add(SelectWidgetSchema())


class GroupSchema2(colander.MappingSchema):
    foo = colander.SchemaNode(
        colander.String(),
        widget=TextWidget()
    )

schema = colander.Schema(name="foo")
schema1 = colander.Schema(name="foo1")
schema2 = colander.Schema(name="foo2")
schema3 = colander.Schema(name="foo3")
schema4 = colander.Schema(name="foo4")
schema1.add(schema2)
schema2.add(schema3)
schema3.add(schema4)
schema4.add(GroupSchema2(name="foo5"))
schema.add(schema1)
group_schema2 = colander.Schema()
group_schema2.add(schema)

schema = colander.Schema()
schema1 = colander.Schema()
schema2 = colander.Schema(name="foo100")
schema3 = colander.Schema()
schema4 = colander.Schema()
schema1.add(schema2)
schema2.add(schema3)
schema3.add(schema4)
schema4.add(GroupSchema2())
schema.add(schema1)
group_schema2.add(schema)

group_schema3 = GroupSchema()
group_schema3.add(UserRegisterSchema())

import colander

from ziggurat_form.widgets import TextWidget, MappingWidget, PositionalWidget, TupleWidget, FormInvalid, PasswordWidget, ConfirmWidget

choices = (
    ('', '- Select -'),
    ('habanero', 'Habanero'),
    ('jalapeno', 'Jalapeno'),
    ('chipotle', 'Chipotle')
)


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
    user_name = colander.SchemaNode(colander.String(),
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
    prefix = colander.SchemaNode(colander.String(), validator=colander.Length(min=3),
                                 widget=TextWidget(validators=[test_validator]))
    phones = Phones(widget=PositionalWidget(validators=[test_validator]))
    suffix = colander.SchemaNode(colander.String(), validator=colander.Length(min=3))


class UserLoginSchema(colander.MappingSchema):
    username = colander.SchemaNode(colander.String(), validator=colander.Length(min=3),
                                   widget=TextWidget(validators=[username_validator]),
                                   description='Value of "admin" will pass')

    password = colander.SchemaNode(colander.String(), validator=colander.Length(min=3),
                                   widget=PasswordWidget())

class UserRegisterSchema(colander.MappingSchema):
    username = colander.SchemaNode(colander.String(), validator=colander.Length(min=3),
                                   widget=TextWidget(validators=[username_validator]),
                                   description='Value of "admin" will pass')

    password = colander.SchemaNode(colander.String(), validator=colander.Length(min=3),
                                   widget=ConfirmWidget(TextWidget()))

    email = colander.SchemaNode(colander.String(), validator=colander.Email())

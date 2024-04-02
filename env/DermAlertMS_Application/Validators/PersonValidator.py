from wtforms import Form, StringField, validators
from datetime import date

class PersonValidator(Form):
    username = StringField('Patient username', validators=[
        validators.DataRequired(message="Debe ingresar el nombre de usuario"),
        validators.Length(max=15, message="Debe tener de máximo 15 caracteres"),
        validators.Regexp(r"^\S+$", message="El nombre de usuario no puede tener espacios en blanco")
    ])

    name = StringField('name', validators=[
        validators.DataRequired(message="Debe ingresar su nombre"),
        validators.Length(max=150, message="Debe tener de máximo 150 caracteres"),
        validators.Regexp(r"^\S+$", message="El nombre no puede tener espacios en blanco")
    ])

    last_name = StringField('last_name', validators=[
        validators.DataRequired(message="Debe ingresar su apellido"),
        validators.Length(max=150, message="Debe tener de máximo 150 caracteres"),
        validators.Regexp(r"^\S+$", message="El nombre no puede tener espacios en blanco")
    ])

    phone = StringField('phone', validators=[
        validators.DataRequired(message="Debe ingresar su número de teléfono"),
        validators.Length(max=30, message="Debe tener de máximo 30 caracteres"),
        validators.Regexp(r"^\S+$", message="El nombre no puede tener espacios en blanco")
    ])

    sex = StringField('sex', validators=[
        validators.DataRequired(message="Debe ingresar su sexo"),
        validators.Length(max=1, message="Debe tener de máximo 1 caracter"),
        validators.Regexp(r"^\S+$", message="El nombre no puede tener espacios en blanco")
    ])

    sex = StringField('sex', validators=[
        validators.DataRequired(message="Debe ingresar su sexo"),
        validators.Length(max=1, message="Debe tener de máximo 1 caracter"),
        validators.Regexp(r"^\S+$", message="El sexo no puede tener espacios en blanco")
    ])

    status = StringField('status', validators=[
        validators.DataRequired(message="Debe ingresar su estatus"),
        validators.Length(max=1, message="Debe tener de máximo 1 caracter"),
        validators.Regexp(r"^\S+$", message="El estatus no puede tener espacios en blanco")
    ])

    email = StringField('email', validators=[
        validators.DataRequired(message="Debe ingresar su email"),
        validators.Length(max=50, message="Debe tener de máximo 50 caracteres"),
        validators.Regexp(r"^\S+$", message="El estatus no puede tener espacios en blanco")
    ])

    password = StringField('password', validators=[
        validators.DataRequired(message="Debe ingresar su contraseña"),
        validators.Length(max=50, message="Debe tener de máximo 50 caracteres"),
        validators.Regexp(r"^\S+$", message="El estatus no puede tener espacios en blanco")
    ])

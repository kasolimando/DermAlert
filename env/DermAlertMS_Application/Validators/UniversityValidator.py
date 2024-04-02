from wtforms import Form, StringField, validators

class UniversityValidator(Form):
    description = StringField('University description', validators=[
        validators.DataRequired(message="Debe ingresar información para la universidad"),
        validators.Length(max=300, message="Debe tener un máximo 300 caracteres")
    ])

    created_by = StringField('Usuario', validators=[
        validators.DataRequired(message="Debe ingresar el nombre de usuario de la persona que lo registra"),
        validators.Length(max=15, message="Debe tener de máximo 15 caracteres"),
        validators.Regexp(r"^\S+$", message="El nombre de usuario no puede tener espacios en blanco")
    ])
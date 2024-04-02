from wtforms import Form, StringField, validators, IntegerField

class SurveyValidator(Form):
    description = StringField('description', validators=[
        validators.DataRequired(message="Debe ingresar información de la racomendación"),
        validators.Length(max=300, message="Debe tener un máximo 300 caracteres")
    ])

    entry_value = IntegerField('entry_value', validators=[
        validators.DataRequired(message="Debe ingresar información del porcenje de entrada"),
        validators.NumberRange(min=0, message="Debe tener ser un número mayor a 0")
    ])

    end_value = IntegerField('end_value', validators=[
        validators.DataRequired(message="Debe ingresar información del porcenje de fin"),
        validators.NumberRange(min=0, message="Debe tener ser un número mayor a 0")
    ])

    created_by = StringField('Usuario', validators=[
        validators.DataRequired(message="Debe ingresar el nombre de usuario de la persona que lo registra"),
        validators.Length(max=15, message="Debe tener de máximo 15 caracteres"),
        validators.Regexp(r"^\S+$", message="El nombre de usuario no puede tener espacios en blanco")
    ])
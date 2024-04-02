from wtforms import StringField, validators, IntegerField
from DermAlertMS_Application.Requests.RecommendationRequest import RecommendationRequest

class RecommendationValidator(RecommendationRequest):
    question = StringField('question', validators=[
        validators.DataRequired(message="Debe ingresar información para la pregunta"),
        validators.Length(max=500, message="Debe tener un máximo 500 caracteres")
    ])

    value = IntegerField('value', validators=[
        validators.DataRequired(message="Debe ingresar información para la pregunta"),
        validators.NumberRange(min=0, message="Debe tener ser un número mayor a 0")
    ])

    created_by = StringField('Usuario', validators=[
        validators.DataRequired(message="Debe ingresar el nombre de usuario de la persona que lo registra"),
        validators.Length(max=15, message="Debe tener de máximo 15 caracteres"),
        validators.Regexp(r"^\S+$", message="El nombre de usuario no puede tener espacios en blanco")
    ])
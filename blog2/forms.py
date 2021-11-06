# HEREDAMOS FLASKFORM
from flask_wtf import FlaskForm
# HEREDAMOS 4 COMPONENTES, CAJA DE TEXTO, BOTON SUBMIT, CAMPO PARA CLAVE y AREA DE TEXTO
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, BooleanField
# HEREDAMOS VALIDADORES, DATO REQUERIDO, EMAIL Y LARGO DE UN CAMPO
from wtforms.validators import DataRequired, Email, Length
from wtforms_sqlalchemy.fields import QuerySelectField

class SignupForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Registrar')

class PostForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired(), Length(max=128)])
    title_slug = StringField('Título slug', validators=[Length(max=128)])
    content = TextAreaField('Contenido')
    submit = SubmitField('Enviar')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Recuérdame')
    submit = SubmitField('Login')


class AlumnosForm(FlaskForm):
    apellido = StringField('Apellido', validators=[DataRequired(), Length(max=128)])
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=128)])
    dni = StringField('DNI', validators=[DataRequired()])
    domicilio = StringField('Domicilio', validators=[Length(max=128)])
    localidad = StringField('Localidad', validators=[DataRequired(), Length(max=128)])
    pais_nac = StringField('Pais de nacimiento', validators=[DataRequired(), Length(max=128)])
    estado_civil = StringField('Estado Civil', validators=[DataRequired(), Length(max=128)])
    sexo = StringField('Sexo', validators=[DataRequired(), Length(max=128)])
    submit = SubmitField('Login')

class ChoiceForm(FlaskForm):
    opts = QuerySelectField(query_factory=(), allow_blank=True)
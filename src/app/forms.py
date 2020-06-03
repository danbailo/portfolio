from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, Length
from wtforms.fields.html5 import EmailField
from wtforms.widgets import TextArea


class EmailForm(FlaskForm):
    name = StringField(validators=[
        DataRequired("Por favor, insira seu nome!"),
        Length(min=1, max=64)])
    email = EmailField(validators=[
        Email(message="Por favor, insira seu email!")])
    message = StringField(widget=TextArea(), validators=[
        DataRequired("Por favor, insira seu nome!")])

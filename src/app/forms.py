from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, Length
from wtforms.fields.html5 import EmailField
from wtforms.widgets import TextArea


class EmailForm(FlaskForm):
    name = StringField(
        "Nome",
        render_kw={
            "placeholder": "Seu Nome *",
            "label": "name"
        },
        validators=[
            DataRequired("Por favor, insira seu nome!"),
            Length(min=1, max=64)])

    subject = StringField(
        "Assunto",
        render_kw={
            "placeholder": "Assunto *",
            "label": "subject"
        },
        validators=[
            DataRequired("Por favor, insira assunto do email!")])

    email = EmailField(
        "Email",
        render_kw={
            "placeholder": "Seu Email *",
            "label": "email"
        },
        validators=[
            Email(message="Email inválido!"),
            DataRequired("Por favor, insira seu email!")])

    message = StringField(
        "Mensagem",
        render_kw={
            "placeholder": "Sua Mensagem *",
            "style": "width: 150%; min-height: 175px;",
            "label": "message"
        },
        widget=TextArea(),
        validators=[
            DataRequired("Por favor, sua mensagem!")])

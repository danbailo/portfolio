from flask import render_template, flash, url_for, redirect, request
from flask_mail import Message
from app import mail
from app.forms import EmailForm


def init_app(app):

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/send_email", methods=["GET", "POST"])
    def send_email():
        form = EmailForm()

        if form.validate_on_submit():
            print(form.name.data)
            print(form.email.data)
            print(form.message.data)
            msg = Message(
                subject="hello world",
                sender=f'{form.subject.data} <danbailotest@gmail.com>',
                recipients=["danbailoufms@gmail.com"],
                body=f"nome:{form.name.data}, email:{form.email.data},\
                       mensagem:{form.message.data}"
            )
            mail.send(msg)
            flash("Email enviado com sucesso!", "sucess")
            return redirect(url_for('index'))

        flash("Por favor, verifique os dados e tente novamente!", "warning")
        return render_template("email.html", form=form)

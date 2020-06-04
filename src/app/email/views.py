from flask import flash, redirect, render_template, url_for
from flask_mail import Message

from app import mail
from app.credentials import MAIL_DEFAULT_SENDER, RECIPIENTS
from app.forms import EmailForm

from . import email


@email.route("/send_email", methods=["GET", "POST"])
def send_email():
    form = EmailForm()

    if form.validate_on_submit():
        print(form.name.data)
        print(form.email.data)
        print(form.message.data)
        msg = Message(
            subject=form.subject.data,
            sender=f'{form.subject.data} {MAIL_DEFAULT_SENDER}',
            recipients=[RECIPIENTS],
            html=f"""
                    <h3>Nome: {form.name.data}</h3>
                    <h3>Email: {form.email.data}</h3>
                    <p>{form.message.data}</p>
                """,
        )
        mail.send(msg)
        flash("Email enviado com sucesso!", "sucess")
        return redirect(url_for('index'))

    flash("Por favor, verifique os dados e tente novamente!", "warning")
    return render_template("email.html", form=form)

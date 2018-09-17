from flask import render_template
from ..import mail
from flask_mail import Message


def mail_message(subject, template, to, **kwargs):
    sender_email = 'mutugieddie3@gmail.com'

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body = render_template(template + ".txt", **kwargs)
    email.html = render_template(template + ".html", **kwargs)
    mail.send(email)

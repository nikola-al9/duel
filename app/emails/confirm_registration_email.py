from celery import shared_task
from requests.models import PreparedRequest
from django.template.loader import get_template
from django.core.mail import EmailMessage
from config.settings.email import DEFAULT_FROM_EMAIL

def get_confirm_registration_token(token):
    req = PreparedRequest()
    url = 'http://localhost:8000/api/auth/registration_with_token/'
    params = {'reg_token': token}
    req.prepare_url(url, params)

    return req.url

@shared_task
def send_confirm_registration_email(name, _to, link, *args, **kwargs):
    """
    Send Email to Confirm account and set password
    """

    link = link.replace("&", "&amp;")

    header = 'Welcome to Duel'
    text = f"""
        Hi {name}
                <br>
        Confirm e-mail and set password on a <a href="{link}"><b>link</b></a>.
    """

    ctx = {
        "header": header,
        "text": text
    }
    subject = header
    message = get_template('confirm_registration.html').render(ctx)
    msg = EmailMessage(
        subject,
        message,
        DEFAULT_FROM_EMAIL,
        [_to],
    )
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()
    print("Mail successfully sent")
    return True
import os

from sendgrid import SendGridAPIClient, To
from sendgrid.helpers.mail import Mail


async def new_email(to_email: str, code: str):
    try:
        message = Mail(
            from_email='caiodtn@gmail.com',
            to_emails=[To(to_email, dynamic_template_data={'code': code})],
            subject='Reset Password'
        )

        message.template_id = os.getenv('TEMPLATE_ID_OWN')
        sg = SendGridAPIClient(os.getenv('SENDGRID_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
    except Exception as e:
        print(str(e))

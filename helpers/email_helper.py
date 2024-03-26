from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from dotenv import dotenv_values
from models.user_table import User
import jwt
from dotenv import load_dotenv
from fastapi.templating import Jinja2Templates
from typing import Optional

load_dotenv(".env")
templates = Jinja2Templates(directory="templates")
config_credentials = dotenv_values(".env")

conf = ConnectionConfig(
    MAIL_USERNAME=config_credentials.get('EMAIL', ''),
    MAIL_PASSWORD=config_credentials.get('PASS', ''),
    MAIL_FROM=config_credentials.get('EMAIL', ''),
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False
)


async def send_email(email: str, subject: str, template_name: str, instance: Optional[User] = None, token: Optional[str] = None):
    template_context = {"request": {}}

    if instance is not None:
        token_data = {
            "id": instance.id,
        }
        token = jwt.encode(token_data, config_credentials["SECRET"], algorithm="HS256")
        template_context["token"] = token

    template = templates.TemplateResponse(template_name, template_context)

    message = MessageSchema(
        subject=subject,
        recipients=[email],
        body=str(template.body, 'utf-8'),
        subtype="html"
    )

    fm = FastMail(conf)
    await fm.send_message(message=message)

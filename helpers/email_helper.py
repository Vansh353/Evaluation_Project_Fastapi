from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from dotenv import dotenv_values
from fastapi import status,HTTPException,Form,File, UploadFile,BackgroundTasks
from models.user_table import User

import jwt

import os
from dotenv import load_dotenv
load_dotenv(".env")
from fastapi_mail import ConnectionConfig
from dotenv import dotenv_values

config_credentials = dotenv_values(".env")

conf = ConnectionConfig(
    MAIL_USERNAME=config_credentials.get('EMAIL', ''),
    MAIL_PASSWORD=config_credentials.get('PASS', ''),
    MAIL_FROM=config_credentials.get('EMAIL', ''),
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS= True,
    MAIL_SSL_TLS= False,
    
    
)


async def send_email(email,instance:User):
    token_data = {
        "id" : instance.id,
    }
    token = jwt.encode(token_data, config_credentials["SECRET"],algorithm="HS256")

    template = f"""
    <!DOCTYPE html>
    <html>
    <head>
    </head>
    <body>
    <div style="display: flex; align-items:center:justify-content:center;flex-direction:coloumn">
    <h3>Account Verification </h3>
    <br>
    <p>Thanks for choosing seabasket, please click on the button below to verify your account</p>
    <a style="margin-top:1rem; padding:1rem; border-radius:0.5rem; font-size:1rem; text-decoration: none; background:"#027d8; color:white;" href="http://localhost:8000/verification/?token={token}">
    Verify your email</a>

    <p> Please Kindly ignore this message if you did not sign up for an account.Thanks</p>

    </div>
    </body>
    </html>
    """

    message = MessageSchema(
        subject="Account Verification",
        recipients=email,
        body=template,
        subtype="html"
    )

    fm = FastMail(conf)
    await fm.send_message(message=message)
import os
import smtplib
import ssl
# Import the email modules we'll need
from email.message import EmailMessage
import datetime
import password
import config

def do_send_email(lista_concursos):
    # Define email sender and receiver
    email_sender = config.email_sender
    email_password = password.email_password
    email_receiver = config.email_receiver

    # Set the subject and body of the email
    hoje = datetime.datetime.today().strftime('%d/%m/%Y')
    subject = f'Lista de concursos PMSC {hoje}'
    lista_concursos_str = '\n'.join([str(i) for i in lista_concursos])

    body = f"""
Oi linda, 
Segue lista de concursos PMSC atualizada:
    
{lista_concursos_str}
    
Vai com tudo!
te amo S2
"""

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

    except smtplib.SMTPException as e:
        print(f'Erro:> {e}')

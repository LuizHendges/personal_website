"""
Aula - Envio de E-mails com SMTP em Python

Nesta aula vemos como:
- Usar variáveis de ambiente com python-dotenv
- Leitura de arquivo HTML e substituição com Template
- Montagem de e-mail MIME em HTML
- Envio de e-mail via servidor SMTP do Gmail
"""

import os
import pathlib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()

# Caminho do arquivo HTML que será usado como corpo do e-mail
CAMINHO_HTML = pathlib.Path(__file__).parent / 'aula185.html'

# Dados de remetente e destinatário
remetente = os.getenv('FROM_EMAIL', '')
destinatario = remetente  # Envia para si mesmo

# Configurações do servidor SMTP do Gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD')

# Lê o HTML e substitui variáveis com Template
with open(CAMINHO_HTML, 'r') as f:
    texto_arquivo = f.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome='João')

# Montagem do e-mail como MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Este é o assunto do e-mail'

# Corpo do e-mail em HTML
corpo_email = MIMEText(texto_email, 'html', 'UTF-8')
mime_multipart.attach(corpo_email)

# Envio do e-mail pelo servidor SMTP
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()               # Identificação inicial (HELO)
    server.starttls()           # Inicia camada de segurança
    server.login(smtp_user, smtp_password)
    server.send_message(mime_multipart)
    print('E-mail enviado com sucesso!')

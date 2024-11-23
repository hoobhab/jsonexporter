import smtplib
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders


def sendMail(send_from, send_to, subject, message, pdf,
              server, port, password,
              use_tls=True):
    """Send an email with the Go Pack! packing list PDF attached. 
    Because Go Pack! sends the email to the user's own email account, 
    args send_from and send_to should refer to the same account. """
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(message))

    part = MIMEBase('application', "octet-stream")
    with open(pdf, 'rb') as file:
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename={}'.format(Path(pdf).name))
    msg.attach(part)

    smtp = smtplib.SMTP(server, port)
    if use_tls:
        smtp.starttls()
    smtp.login(send_from, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()

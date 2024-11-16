import smtplib
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders


def sendMail(send_from, send_to, subject, message, pdf,
              server="localhost", port=587, username='', password='',
              use_tls=True):
    """Send an email with the Go Pack! PDF attached. Because Go Pack! sends the email to the user, args send_from, send_to, and username should refer to the same account. """
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
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()

# Example usage:
# pdf_name = "packinglist.pdf"
# recipient = ["example@mail.com"]
# sendMail("example@mail.com", recipient, "Go Pack! Test Email", "This is a test email from Go Pack!", pdf_name, "smtp.gmail.com", 587, "example@mail.com", "app_password", True)


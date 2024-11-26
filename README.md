# jsonexporter
JSON to PDF microservice

How to request data:
The microservice requires a ZeroMQ message sent in the form of a JSON object. Example call:

socket.send_json({"filename" : "packinglist.json", "username" : email_user, "password" : email_pw, "server" : server, "port" : port})

The first key refers packing list JSON object, the second to the email username, and the third to the email's password. The fourth and fifth keys refer to the email server and port number.

How to receive data:
After requesting data from the microservice, it will do its work then reply with a confirmation of the PDF's generation and the filepath of where it was saved. If the request included email login info, it will also confirm that the PDF was emailed to the user. Example call:

message = socket.recv()

![uml](https://github.com/user-attachments/assets/5382e5bd-92d1-45f9-8687-f88d71504a9c)

Using the sendEmail function <br>
Example usage: <br>
recipient = ["example@mail.com"]
sendMail("example@mail.com", recipient, "Go Pack! Test Email", "This is a test email from Go Pack!", pdf_name, "smtp.gmail.com", 587, "app_password", True)

Packages Used
- smtplib: enables Simple Mail Transfer Protocol for the emailer function.
- pathlib: handles filesystem paths
- email: manages email messages
- zmq: message queueing service [Link](https://zeromq.org/)
- pdfdocument: provides a framework for creating PDFs with methods similar to html [Link](https://github.com/matthiask/pdfdocument/)

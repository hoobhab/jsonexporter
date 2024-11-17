# jsonexporter
JSON to PDF microservice

How to request data:
The microservice requires a ZeroMQ message sent in the form of a JSON object. Example call:

socket.send_json({"filename" : "packinglist.json", "username" : email_user, "password" : email_pw})

The first key refers to the filename of the packing list JSON file, the second to the email username, and the third to the email's password. The microservice uses the Gmail server to send emails, so the test program uses a Gmail account to test the email function.

How to receive data:
After requesting data from the microservice, it will do its work then reply with a confirmation of the PDF's generation and the filepath of where it was saved. If the request included email login info, it will also confirm that the PDF was emailed to the user. Example call:

message = socket.recv()

from pdfdocument.document import PDFDocument
from emailer import sendMail
import json
import smtplib
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
import time
import zmq

def exportPdf(filename):
    """Creates a pdf from the json file."""
    pdf = PDFDocument(filename)
    pdf.init_report()
    pdf.h2(f"{imported_list["ListName"]}")
    pdf.spacer()
    pdf.h3(f"Departure date: {imported_list["DepartDate"]}")
    pdf.h3(f"Return date: {imported_list["ReturnDate"]}")
    pdf.h3(f"Destination: {imported_list["Destination"]}")
    nested_list_contents = imported_list["ListContents"]
    pdf.spacer()
    pdf.h3("Your Items:")
    pdf.spacer()

    for index, item in enumerate(nested_list_contents):
        pdf.p(f"{index}. {nested_list_contents[index]["ItemName"]}\nCategory: {nested_list_contents[index]["ItemCategory"]}\nLocation: {nested_list_contents[index]["ItemLocation"]}\nPacked? {nested_list_contents[index]["Packed"]}")
        pdf.spacer()

    pdf.generate()
    
# In the case that the name of the json file is passed
if __name__ == "__main__":
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    while True:
        #import the packing list json filename through ZeroMQ. packinglist.json is a placeholder for now
        packing_list = socket.recv()
        print("Received JSON filename: %s" % packing_list)

        #load json into a dict
        with open(packing_list) as file:
            imported_list = json.load(file)

        exportPdf(f"{imported_list["ListName"]}.pdf")
        print(f"File {imported_list["ListName"]}.pdf generated")

        socket.send(b"PDF generated.")
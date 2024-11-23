from pdfdocument.document import PDFDocument
from emailer import *
import json, os, zmq

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
        checkbox = "[×]" if item["Packed"] == True else "[ ]"
        spacer = "·"
        list_item = f"{checkbox} {nested_list_contents[index]["ItemName"] :{spacer}<25} Category: {nested_list_contents[index]["ItemCategory"]:{spacer}<25} Location: {nested_list_contents[index]["ItemLocation"]}"
        pdf.p(list_item)

    pdf.generate()
    
if __name__ == "__main__":
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    while True:
        #receive the packing list json filename, and email login info, through ZeroMQ. 
        incoming_message = socket.recv_json()
        print("Received JSON filename: %s" % incoming_message["filename"])

        #load packing list json into a dict
        with open(incoming_message["filename"]) as file:
            imported_list = json.load(file)

        exportPdf(f"{imported_list["ListName"]}.pdf")
        print(f"File {imported_list["ListName"]}.pdf generated")

        if incoming_message["username"] and incoming_message["password"]:
            username = incoming_message["username"]
            password = incoming_message["password"]
            sendMail(username, [username], "Your Go Pack! Packing List", "This is your packing list from Go Pack!", f"{imported_list["ListName"]}.pdf", "smtp.gmail.com", 587, password, True)

            socket.send_string(f"PDF generated. File saved to folder {os.getcwd()}. Emailed to {username}.")
        else:
            socket.send_string(f"PDF generated. File saved to folder {os.getcwd()}")

from pdfdocument.document import PDFDocument
import json

packing_list = "packinglist.json"
#import the packing list json filename through ZeroMQ. packinglist.json is a placeholder for now

#load json into a dict
with open(packing_list) as file:
    imported_list = json.load(file)

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
    pdf.h3("Your Items:")
    pdf.spacer()

    pdf.p(nested_list_contents)
    # for index, item in enumerate(nested_list_contents):
    #     pdf.p(f"{index}. {nested_list_contents[0]}\nCategory: {nested_list_contents[1]}\nLocation: {nested_list_contents[2]}\nPacked? {nested_list_contents[3]}")

    pdf.generate()
    
if __name__ == "__main__":
    exportPdf("test.pdf")
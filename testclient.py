import zmq
import json

if __name__ == "__main__":
    context = zmq.Context()

    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")
    email_user = "hoobhab3@gmail.com"
    email_pw = "examplepassword"
    with open("packinglist.json") as file:
        import_list = json.load(file)
    server = "smtp.gmail.com"
    port = 587

    socket.send_json({"packing_list" : import_list, "username" : email_user, "password" : email_pw, "server" : server, "port": port})
    message = socket.recv()

    print(message)

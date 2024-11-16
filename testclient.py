import zmq

if __name__ == "__main__":
    context = zmq.Context()

    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")
    email_user = "hoobhab3@gmail.com"
    email_pw = "mgar lbvm uksp ngem"
    socket.send_json({"filename" : "packinglist.json", "username" : email_user, "password" : email_pw})
    # socket.send_json({"filename" : "packinglist.json", "username" : None, "password" : None})
    message = socket.recv()

    print(message)

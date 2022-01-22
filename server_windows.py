# Imports
import socket

s = socket.socket()
print("Socket successfully created")
# Set Same port for Both sides (Client and server)
port = 1998
# Empty quotes without IP shows socket is created to listen the client
s.bind(('', port))
print("socket connected to %s" % port)
# Socket start to listening
s.listen(5)
print("listening to client")
# Socket is running till the end of conversation
while True:
    # connection accepted by server socket.
    c, address = s.accept()
    print('Got connection from', address)

    while True:
        # Send request to the client
        request = input()
        c.send(request .encode())
        # Print client's reply to your request
        print("Client:", c.recv(2022).decode())
        if request == "bye":
            c.close()
            print("Connection terminated, goodbye from client")
            break




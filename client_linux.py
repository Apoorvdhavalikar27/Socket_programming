import socket
# Create the socket
s = socket.socket()
# Same port number that we used in Server End
port = 1998

# This is the local IP address of Windows
s.connect(('10.0.2.2', port))
while True:
    # data received
    print(s.recv(2022).decode())
    while True:
        response = input()
        s.send(response .encode())
        print("Server:", s.recv(2022).decode())
        if response == "bye":
            s.close()
            print("Connection terminated, Goodbye from Server!!!!")



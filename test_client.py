import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket() as s:
    read = s.makefile('r')
    write = s.makefile('w')
    s.connect((HOST, PORT))
    while True:
        command = input()
        write.write(command + '\n')
        write.flush()


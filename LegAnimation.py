import socket
from vpython import *
from time import *
from convert_stl import stl_to_triangles


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


stick = stl_to_triangles('model/stick.stl')
stick.pos = vec(0, 0, 0)
foot = stl_to_triangles('model/foot.stl')
foot.pos = vec(0, 80, -115)
adapter = stl_to_triangles('model/adapter.stl')
adapter.pos = vec(0, 0, 200)
angle=0
i=0


def forward():
    for j in range(10**5):
        rate(100000)
        foot.rotate(0.5 * 10**-5, axis=vec(1, 0, 0))
    print('Forward movement done')


def backward():
    for j in range(10**5):
        rate(100000)
        foot.rotate(-0.5 * 10**-5, axis=vec(1, 0, 0))
    print('Backward movement done')


s = socket.socket()
s.bind(('', PORT))
s.listen(1)
while True:
    conn, addr = s.accept()
    print(f'Connection established: {addr}')
    read = conn.makefile('r')
    write = conn.makefile('w')
    with conn, read, write:
        while True:
            data = read.readline()
            if not data:
                print(f'Stream message has been closed: {addr}')
                conn.close()
                break
            cmd = data.strip()
            print(f'Receive command: {cmd}')
            if cmd == 'f':
                forward()
            elif cmd == 'b':
                backward()



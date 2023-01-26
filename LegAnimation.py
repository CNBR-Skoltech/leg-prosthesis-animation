import socket
from vpython import *
from time import *
from convert_stl import stl_to_triangles


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
SCENE_WIDTH = 1920
SCENE_HEIGHT = 900
SCENE_TITLE = 'Proprio foot model'

stick = stl_to_triangles('model/stick.stl')
stick.pos = vec(30, 0, 180)
foot = stl_to_triangles('model/foot.stl')
foot.pos = vec(0, 0, 0)
adapter = stl_to_triangles('model/dimomixel.stl')
adapter.pos = vec(30, 0, 50)
angle=0
i=0


def forward():
    for j in range(10**5):
        rate(100000)
        foot.rotate(0.5 * 10**-5, axis=vec(0, 1, 0))
    print('Forward movement done')


def backward():
    for j in range(10**5):
        rate(100000)
        foot.rotate(-0.5 * 10**-5, axis=vec(0, 1, 0))
    print('Backward movement done')


# s = socket.socket()
# s.bind(('', PORT))
# s.listen(1)

scene.width = SCENE_WIDTH
scene.height = SCENE_HEIGHT
scene.title = SCENE_TITLE
x_hat = arrow(pos=vector(200, 0, 0), axis=vector(200,0,0), color=color.green)
y_hat = arrow(pos=vector(200, 0, 0), axis=vector(0,200,0), color=color.red)
z_hat = arrow(pos=vector(200, 0, 0), axis=vector(0,0,200), color=color.blue)
instructions = text(text="X - green\n Y - red\n Z - blue", pos=vector(-300, 0, 0), axis=vec(1, 0, 0), color=color.white, height=20)
while True:
    # foot.rotate(angle=0.001, axis=vec(0, 1, 0))
    # conn, addr = s.accept()
    forward()
    sleep(2)
    backward()
    sleep(2)
    # print(f'Connection established: {addr}')
    # read = conn.makefile('r')
    # write = conn.makefile('w')
    # with conn, read, write:
    #     while True:
    #         data = read.readline()
    #         if not data:
    #             print(f'Stream message has been closed: {addr}')
    #             conn.close()
    #             break
    #         cmd = data.strip()
    #         print(f'Receive command: {cmd}')
    #         if cmd == 'f':
    #             forward()
    #         elif cmd == 'b':
    #             backward()



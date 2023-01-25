import time

from vpython import *
from time import *
from convert_stl import stl_to_triangles


stick = stl_to_triangles('model/stick.stl')
stick.pos = vec(0, 0, 0)
foot = stl_to_triangles('model/foot.stl')
foot.pos = vec(0, 80, -115)
adapter = stl_to_triangles('model/adapter.stl')
adapter.pos = vec(0, 0, 200)
angle=0
i=0


def forward():
    # rate(10)
    for j in range(10**5):
        # rate(1000)
        foot.rotate(0.5 * 10**-5, axis=vec(1, 0, 0))


def backward():
    # rate(10)
    for j in range(10**5):
        # rate(1000)
        foot.rotate(-0.5 * 10**-5, axis=vec(1, 0, 0))


while True:
    rate(1)
    forward()
    sleep(2)
    backward()
    sleep(2)


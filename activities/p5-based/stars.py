from p5 import *
from math import *

COLORS = ["red", "green", "blue", "purple"]

def setup():
    size(300, 200)

def draw():
    count = 4 + (frame_count // 120) % 7
    angle = PI * frame_count / 180
    radius = height/3.5
    
    background("black")    
    stroke(255)
    stroke_weight(2)

    fill(COLORS[count % len(COLORS)])
    star(count, 1 * width/4, height/2, radius, angle=angle)
    
    fill(COLORS[(count+1) % len(COLORS)])
    polygon(count, 3 * width/4, height/2, radius, angle=-angle)

def star(n, cx, cy, radius, ratio=0.4, angle=0):
    external_radius = radius
    internal_radius = external_radius * ratio
    delta = PI / n 
    
    push_matrix()
    translate(cx, cy)
    rotate(angle)
    
    begin_shape()
    for i in range(n):
        a = -PI/2 + i * 2*PI / n
        b = a + delta
        vertex(external_radius * cos(a), external_radius * sin(a))
        vertex(internal_radius * cos(b), internal_radius * sin(b))
    end_shape(CLOSE)

    pop_matrix()

def polygon(n, cx, cy, radius, angle=0):
    push_matrix()
    translate(cx, cy)
    rotate(angle)
    
    begin_shape()
    for i in range(n):
        a = -PI/2 + i * 2*PI / n
        vertex(radius * cos(a), radius * sin(a))
    end_shape(CLOSE)

    pop_matrix()

run()

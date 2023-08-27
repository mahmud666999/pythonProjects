from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import numpy as np
import time
import random as rand
from random import random, sample


def randColor(): return sample([0, random(), 1], 3)


def draw_lines(x1, y1, x2, y2):
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    x1 = rand.randint(10, 400)
    y1 = rand.randint(10, 400)
    x2 = rand.randint(10, 400)
    y2 = rand.randint(10, 400)
    glColor3f(*randColor())
    draw_lines(x1, y1, x2, y2)

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)  # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")  # window name

t = 8
for i in range(t):
    glutDisplayFunc(showScreen)
    showScreen()
    time.sleep(0.7)
glutDisplayFunc(showScreen)

glutMainLoop()
from OpenGL.GL import *
from OpenGL.GLUT import *
import math
def drawPoints(x, y):
    glPointSize(1.0)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def iterate():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1920, 0.0, 1080, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# def circles_drawer():
#     midPointCircleAlgo(500,530,30)
#     midPointCircleAlgo(530,500,30)
#     midPointCircleAlgo(470,500,30)
#     midPointCircleAlgo(470, 470, 30)
def midPointCircleAlgo(X,Y,r):

    x = 0
    y = r
    decision = 1 - r
    while x <= y:
        x += 1
        if decision < 0:
            decision += 2 * x + 3
        else:
            y -= 1
            x += 1
            decision += 2 * (x - y) + 1
        drawPoints(X + x, Y + y)
        drawPoints(X - x, Y + y)
        drawPoints(X + x, Y - y)
        drawPoints(X - x, Y - y)
        drawPoints(X + y, Y + x)
        drawPoints(X - y, Y + x)
        drawPoints(X + y, Y - x)
        drawPoints(X - y, Y - x)


def draw_all_circles():
    midPointCircleAlgo(500, 530, 100)
    midPointCircleAlgo(530, 500, 100)
    midPointCircleAlgo(470, 500, 100)
    midPointCircleAlgo(500, 470, 100)


    midPointCircleAlgo(470, 530, 100)
    midPointCircleAlgo(530, 530, 100)
    midPointCircleAlgo(470, 470, 100)
    midPointCircleAlgo(530, 470, 100)
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    # midPointCircleAlgo(500, 530, 100)
    # midPointCircleAlgo(530, 500, 100)
    # midPointCircleAlgo(470, 500, 100)
    # midPointCircleAlgo(500, 470, 100)
    #
    #
    # midPointCircleAlgo(470, 530, 100)
    # midPointCircleAlgo(530, 530, 100)
    # midPointCircleAlgo(470, 470, 100)
    # midPointCircleAlgo(530, 470, 100)

    draw_all_circles()
    midPointCircleAlgo(500, 500, 100*math.sqrt(2))
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1920, 1080)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL project")
glutDisplayFunc(showScreen)
glutMainLoop()
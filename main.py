from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math


def draw_points(x, y):
    glPointSize(3)     # pixel size->by default 1 fix
    glBegin(GL_POINTS)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(x, y)  # PIXEL DEMONSTRATION CO_ORDINATES
    glEnd()

y_iterator=0
program_running = False
circle_drawn = False
circle_iterator=0
arrow_size_iterator=0

#FINDING THE GIVEN CORDINATES ZONE
def Find_zone(x_1, y_1, x_2, y_2):
    dx=x_2-x_1
    dy=y_2-y_1
    if abs(dx) > abs(dy):
        if dx >= 0 and dy >= 0:
            zone = 0
        elif dx >= 0 and dy <= 0:
            zone = 7
        elif dx <= 0 and dy >= 0:
            zone = 3
        elif dx <= 0 and dy <= 0:
            zone = 4
    else:
        if dx >= 0 and dy >= 0:
            zone = 1
        elif dx <= 0 and dy >= 0:
            zone = 2
        elif dx <= 0 and dy <= 0:
            zone = 5
        elif dx >= 0 and dy <= 0:
            zone = 6
    return zone


def convert_to_zone0(x, y, zone):
    if zone == 0: return x, y
    if zone == 1: return y, x
    if zone == 2: return y, -x
    if zone == 3: return -x, y
    if zone == 4: return -x, -y
    if zone == 5: return -y, -x
    if zone == 6: return -y, x
    if zone == 7: return x, -y


def convertoOrigin(x, y, zone):
    if zone == 0: return x, y
    if zone == 1: return y, x
    if zone == 2: return -y, x
    if zone == 3: return -x, y
    if zone == 4: return -x, -y
    if zone == 5: return -y, -x
    if zone == 6: return y, -x
    if zone == 7: return x, -y

#MID POINT ALGO
def midpoint_line(x1, y1, x2, y2, zone):
    dx=x2-x1
    dy=y2-y1
    d=2*dy-dx
    d_E=2*dy
    d_NE=2*dy-dx
    x=x1
    y=y1
    while (x<x2):
        x_p,y_p=convertoOrigin(x,y,zone)
        draw_points(x_p,y_p)
        if d<0:
            x+=1
            d+=d_E
        else:
            x+=1
            y+=1
            d+=d_NE

#LINE DRAWING
def line_drawing(x1, y1, x2, y2):  #START POINT & END POINT

    curr_z=Find_zone(x1, y1, x2, y2) #DETERMINING CURRENT ZONE
    x1_prime, y1_prime = convert_to_zone0(x1, y1, curr_z)  #CONVERTING TO ZONE 0 ORDER
    x2_prime, y2_prime = convert_to_zone0(x2, y2, curr_z)
    midpoint_line(x1_prime, y1_prime, x2_prime, y2_prime, curr_z) #NEW LINE IN ZONE 0


def iterate():
    glViewport(0, 0, 1920, 1080)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1920, 0.0, 1080, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def draw_text(x, y, text):
    glRasterPos2f(x, y)
    for character in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12,ord(character))

def showScreen():
    global y_iterator
    global circle_iterator
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    def draw_circle(center_x, center_y, radius, r, g, b, num_segments=100):
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(r, g, b)  # Set the color based on the provided r, g, b values
        glVertex2f(center_x, center_y)  # Center of the circle
        for i in range(num_segments + 1):
            angle = 2.0 * math.pi * i / num_segments
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            glVertex2f(x, y)
        glEnd()

    draw_circle(0 + y_iterator, 850, 75+circle_iterator, 1, 0, 0)
    draw_circle(0 + y_iterator, 850, 50+circle_iterator, 0, 1, 1)
    draw_circle(0 + y_iterator, 850, 25+circle_iterator, 0, 0, 1)
    draw_text(800, 40, f'Circle CoOrdinates: x={y_iterator + 0}, y=850')
    if program_running:
    # drawing bow
        line_drawing(960, 100+y_iterator, 960, 225+y_iterator)
        line_drawing(900, 225+y_iterator, 930, 300+y_iterator)
        line_drawing(960, 300+y_iterator, 990, 225+y_iterator)
        line_drawing(900, 225+y_iterator, 1020, 225+y_iterator)
        draw_text(800, 20, f'Bow Coordinates: x=960, y={y_iterator+225}')
        if 300+y_iterator>=1020:
            draw_text(800, 60, f'Game Over')


    glutSwapBuffers()
def timer_callback(value):
    global y_iterator
    global circle_iterator
    global arrow_size_iterator
    y_iterator += 20
    circle_iterator -=1
    arrow_size_iterator -=2
    glutPostRedisplay()  # Trigger a display update
    glutTimerFunc(1000, timer_callback, 0)

def keyboard_callback(key, x, y):
    global program_running
    if key == b's':
        program_running = True
    elif key == b'q':
        program_running = False

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1920, 1080)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL project")
glutDisplayFunc(showScreen)
glutTimerFunc(1000, timer_callback, 0)  # Start the timer
glutKeyboardFunc(keyboard_callback)
glutMainLoop()

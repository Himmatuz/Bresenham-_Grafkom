
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-50.0, 50.0, -50.0, 50.0)
    glPointSize(5)


def plot(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def bresenham_drawing_circle(r):

    x_center = 3
    y_center = 3

    r = 9
    x = 0
    y = r

    d = 3 - 2 * r

    plot(x + x_center, y + y_center)

    while y > x:

        if d < 0:
            x += 1
            d += 4 * x + 6
        else:
            x += 1
            y -= 1
            d += (4 * (x - y)) + 10 

        plot(x + x_center, y + y_center)

        plot(x + x_center, -y + y_center)

        plot(-x + x_center, -y + y_center)

        plot(-x + x_center, y + y_center)

        plot(y + x_center, x + y_center)

        plot(-y + x_center, x + y_center)

        plot(-y + x_center, -x + y_center)

        plot(y + x_center, -x + y_center)


def plotpoints():

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 1.0)

    glBegin(GL_LINES)

    glVertex2f(-50, 0)
    glVertex2f(50, 0)

    glVertex2f(0, -50)
    glVertex2f(0, 50)

    glEnd()

    bresenham_drawing_circle(40)

    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Bresenham Lingkaran")
    glutDisplayFunc(plotpoints)

    init()
    glutMainLoop()

main()


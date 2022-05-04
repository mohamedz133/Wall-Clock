from math import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from datetime import datetime

###################################################
######################################################## constants ###############################
seconds = 0
minutes = 0
houres  = 0

INTERVAL = 1000

##################################################    Drawing text   ###############################

FONT_DOWNSCALE = .0005
glutInit()
print(glutStrokeHeight(GLUT_STROKE_ROMAN))

def draw_text(string, x, y):
    glLineWidth(2)
    glColor(1, 0, 0)
    glPushMatrix()
    glTranslate(x, y, 0)
    glScale(FONT_DOWNSCALE, FONT_DOWNSCALE, 1)  # when writing text and see nothing downscale it to a very small value .001 and draw at center
    string = string.encode()  # conversion from Unicode string to byte string
    for c in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)
    glPopMatrix()


###################################   to satisfy reality #################################

def initGL():
    global seconds
    global minutes
    global houres
    now = datetime.now()
    Sec = int (now.strftime("%S"))
    Min = int (now.strftime("%M"))
    Hr = int (now.strftime("%H"))

    seconds = -6*Sec
    minutes = -4.1*Min
    houres = -30*Hr

##############################################  Drawing function ###############################
def draw_clock(x=0):

    global seconds
    global minutes
    global houres
    global INTERVAL
    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1, 1, -1, 1, -1, 3)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 0, 0, 0, -1, 0, 1, 0)

################################################## houres NUmbers  ########################

    glScale(.83,.83,0)
    draw_text("12", -.03, .8)
    draw_text("6", -.02, -.83)
    draw_text("1", .4, .7)
    draw_text("7", -.43, -.75)
    draw_text("11", -.45, .7)
    draw_text("5", .4, -.74)

    draw_text("3", .84, -.02)
    draw_text("9", -.86, -.02)

    draw_text("2", .7, .4)
    draw_text("10", -.75, .4)

    draw_text("4", .7, -.43)
    draw_text("8", -.73, -.43)

#####################################     Main Points  ####################

    glLoadIdentity()
    glColor(1, 0, 0)
    glPointSize(5)
    glScale(.83,.83,0)
    glBegin(GL_POINTS)
    glVertex2d(0,.9)
    glVertex2d(0, -.9)
    glVertex2d(-0.45, -.78)
    glVertex2d(0.45, .78)
    glVertex2d(-0.45, .78)
    glVertex2d(0.45, -.78)
    glVertex2d(0.78, .45)
    glVertex2d(-0.78, -.45)
    glVertex2d(-0.78, .45)
    glVertex2d(0.78, -.45)
    glVertex2d(0.9, 0)
    glVertex2d(-0.9, 0)
    glEnd()

#######################################   Frame Circle      ##################
    glLoadIdentity()
    glColor3ub(00, 0, 255)
    glLineWidth(3)
    glBegin(GL_LINE_LOOP)
    resolution = 1
    r = .81

    for ang in range(0, 360, resolution):  # parametric form of a circle (r*cos(theta),r*sin(theta))
        x = r * cos(ang * pi / 180)  # pi / 180 from angle to rad
        y = r * sin(ang * pi / 180)  # pi / 180 from angle to rad
        glVertex2d(x, y)  # 2 = coordL , d = float point NOT DIMENSION

    glEnd()

#######################################   minutes points      ##################
    glLoadIdentity()
    glColor3ub(0, 0, 255)
    glPointSize(5)
    glScale(.87,.87,0)

    glBegin(GL_POINTS)
    resolution = 6
    r = .9

    for ang in range(0, 360, resolution):  # parametric form of a circle (r*cos(theta),r*sin(theta))
        x = r * cos(ang * pi / 180)  # pi / 180 from angle to rad
        y = r * sin(ang * pi / 180)  # pi / 180 from angle to rad
        glVertex2d(x, y)  # 2 = coordL , d = float point NOT DIMENSION

    glEnd()

################################################## seconds points  ########################
    glLoadIdentity()
    glColor3ub(125, 125, 0)
    glPointSize(1)
    glScale(.88,.88,0)

    glBegin(GL_POINTS)
    resolution = 1
    r = .9

    for ang in range(0, 360, resolution):  # parametric form of a circle (r*cos(theta),r*sin(theta))
        x = r * cos(ang * pi / 180)  # pi / 180 from angle to rad
        y = r * sin(ang * pi / 180)  # pi / 180 from angle to rad
        glVertex2d(x, y)  # 2 = coordL , d = float point NOT DIMENSION

    glEnd()

#########################################   centre point     ########################
    glLoadIdentity()
    glColor(1, 1,1 )
    glPointSize(4)
    glBegin(GL_POINTS)
    glVertex2d(0, 0)
    glEnd()

##############################################   hours pointer     #################

    glLoadIdentity()
    glColor3f(1,0,0)
    glLineWidth(2.5)
    glScale(.65,.65,0)

    glRotatef(houres,0,0,.1)
    glBegin(GL_LINES)
    glVertex2d(0, 0)
    glVertex2d(0, .6)
    glEnd()

##############################################   minutes pointer     #################

    glLoadIdentity()
    glColor3ub(0, 0, 255)
    glLineWidth(1.5)
    glScale(.8,.8,0)
    glRotatef(minutes, 0, 0, .1)
    glBegin(GL_LINES)
    glVertex2d(0, 0)
    glVertex2d(.75, 0)
    glEnd()

##############################################   SECONDS pointer     #################

    glLoadIdentity()
    glColor3ub(125, 125, 0)
    glLineWidth(.5)
    glScale(.88,.88,0)

    glRotatef(seconds, 0, 0, .1)
    glBegin(GL_LINES)
    glVertex2d(0, 0)
    glVertex2d(0, .87)
    glEnd()
    glLoadIdentity()
##########################################   rotation condition    ########################



    seconds -= 3
    if seconds <= -360:
        if minutes <= -360:
            houres -= 30
            seconds = 0
            minutes = 0
        else:
            minutes -= 6
            seconds = 0
    glutTimerFunc(INTERVAL, draw_clock, 1)
    glutSwapBuffers()


####################################################  main  ###########################
glutInit()
glutInitWindowSize(600, 600)
glutInitWindowPosition(100, 80)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutCreateWindow(b"wall clock animation _ Mohamed Zaki")
initGL()
glutTimerFunc(INTERVAL, draw_clock, 1)
glutDisplayFunc(draw_clock)
glutMainLoop()

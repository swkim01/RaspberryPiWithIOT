#!/usr/bin/python
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import sys
import os.path, time, math
import RTIMU
 
SCREEN_SIZE = (800, 600)

def resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width) / float(height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #gluLookAt(-5.0, 0.0, -1.0,
    #          0.0, 0.0, 0.0,
    #          0.0, 0.0, -1.0)
    glTranslatef(0.0, 0.0, -5)
    glRotatef(90, 0.0, 1.0, 0.0)
    glRotatef(90, 1.0, 0.0, 0.0)
     
def init():
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glClearColor(0.0, 0.0, 0.2, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LEQUAL)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

def drawText(position, string):
    font=pygame.font.Font(None, 30)
    #font=pygame.font.SysFont("Courier", 18, True)
    textSurface = font.render(string, True, (255,255,255,255), (0,0,0,255))
    text = pygame.image.tostring(textSurface, "RGBA", True)
    glRasterPos3d(*position)
    glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text)

def run():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, OPENGL | DOUBLEBUF)
    resize(*SCREEN_SIZE)
    init()
    clock = pygame.time.Clock()
    cube = Cube((0.0, 0.0, 0.0))
    axis = Axis((0.0, 0.0, 0.0))

    SETTINGS_FILE = "RTIMULib"
    if not os.path.exists(SETTINGS_FILE + ".ini"):
        print("Settings file does not exist, will be created")

    s = RTIMU.Settings(SETTINGS_FILE)
    imu = RTIMU.RTIMU(s)

    print("IMU Name: " + imu.IMUName())

    if (not imu.IMUInit()):
        print("IMU Init Failed");
        sys.exit(1)
    else:
        print("IMU Init Succeeded");

    poll_interval = imu.IMUGetPollInterval()
    print("Recommended Poll Interval: %dmS\n" % poll_interval)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYUP and event.key == K_ESCAPE:
                return
 
        if imu.IMURead():
          # x, y, z = imu.getFusionData()
          # print("%f %f %f" % (x,y,z))
          data = imu.getIMUData()
          fusionPose = data["fusionPose"]
          string = "r: %3.2f p: %3.2f y: %3.2f" % (math.degrees(fusionPose[0]), 
              math.degrees(fusionPose[1]), math.degrees(fusionPose[2]))
          #print(string)
          x_angle = math.degrees(fusionPose[0])
          y_angle = math.degrees(fusionPose[1])
          z_angle = math.degrees(fusionPose[2])

          glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
 
          glPushMatrix()
          glLoadIdentity()
          glTranslatef(0.0,0.0,-5.0)
          drawText((-1.,-2.,0.), string)
          glPopMatrix()

          glPushMatrix()
          axis.render()
          glRotate(float(x_angle), 1, 0, 0)
          glRotate(float(y_angle), 0, 1, 0)
          glRotate(float(z_angle), 0, 0, 1)
          #axis.render()
          cube.render()
          glPopMatrix()

        pygame.display.flip()

class Axis(object):

    def __init__(self, position):
        self.position = position
 
    # Axis information
    num_lines = 3
 
    colors = [ (0, 1, 0),
               (0, 0, 1),
               (1, 0, 0) ]

    vertices = [ (2, 0, 0),
                 (0, 0, 0),
                 (0, 2, 0),
                 (0, 0, 0),
                 (0, 0, 2),
                 (0, 0, 0) ]
 
    def render(self):
        colors = self.colors
        vertices = self.vertices
 
        # Draw all 3 lines of the axis
        for line in xrange(self.num_lines):
            glColor3fv(colors[line])
            glLineWidth(5)
            glBegin(GL_LINES)
            glVertex3fv(vertices[line*2])
            glVertex3fv(vertices[line*2+1])
            glEnd()
 
class Cube(object):
 
    def __init__(self, position):
        self.position = position
 
    # Cube information
    num_faces = 6
 
    vertices = [ (-1.0, -0.2, 0.2),
                 (1.0, -0.2, 0.2),
                 (1.0, 0.2, 0.2),
                 (-1.0, 0.2, 0.2),
                 (-1.0, -0.2, -0.2),
                 (1.0, -0.2, -0.2),
                 (1.0, 0.2, -0.2),
                 (-1.0, 0.2, -0.2) ]
 
    normals = [ (0.0, 0.0, +1.0),  # front
                (0.0, 0.0, -1.0),  # back
                (+1.0, 0.0, 0.0),  # right
                (-1.0, 0.0, 0.0),  # left
                (0.0, +1.0, 0.0),  # top
                (0.0, -1.0, 0.0) ]  # bottom
 
    vertex_indices = [ (0, 1, 2, 3),  # front
                       (4, 5, 6, 7),  # back
                       (1, 5, 6, 2),  # right
                       (0, 4, 7, 3),  # left
                       (3, 2, 6, 7),  # top
                       (0, 1, 5, 4) ]  # bottom

    colors = [ (0.6, 0.3, 0.3), #front
               (0.6, 0.3, 0.3), #back
               (0.3, 0.6, 0.3), #right
               (0.3, 0.6, 0.3), #left
               (0.3, 0.3, 0.6), #top
               (0.3, 0.3, 0.6)] #bottom

    def render(self):
        # Draw all 6 faces of the cube
        glBegin(GL_QUADS)
        for face_no in xrange(self.num_faces):
            glNormal3dv(self.normals[face_no])
            v1, v2, v3, v4 = self.vertex_indices[face_no]
            glColor3fv(self.colors[face_no])
            glVertex3fv(self.vertices[v1])
            glVertex3fv(self.vertices[v2])
            glVertex3fv(self.vertices[v3])
            glVertex3fv(self.vertices[v4])
        glEnd()
 
if __name__ == "__main__":
    run()

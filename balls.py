import SimpleGraphics
import random
import math
import numpy
from math import sqrt
sqrt = math.sqrt

MAX_LENGTH = 100
RESTITUTION = 0.85
RESOLUTION = 0.1

particles = []
blocks = []
mouseX = 0
mouseY = 0
gravity = 0.0
pivotX = 0
pivotY = 0
launchX = 0
launchY = 0
isPivoted = False

class Particle:
    x = 0
    y = 0 
    v_x = 0
    v_y = 0
    radius = 0
    mass = 0
    def __init__(self, x, y, radius, v_x = 0, v_y = 0, mass=1):
        self.radius = radius
        self.x = x 
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.mass = mass

def DoCirclesOverlap(x1, y1, r1, x2, y2, r2):
    return (abs((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))) <= (r1+r2)*(r1+r2)

def Create():
    SimpleGraphics.SetCaption("Balls Demo")
    return

def Update(elapsed):
    global particles
    # Collisions
    colliding_pairs = []
    for particle in particles:
        for colliding_particle in particles:
            if particle != colliding_particle:
                if(DoCirclesOverlap(particle.x, particle.y, particle.radius, colliding_particle.x, colliding_particle.y, colliding_particle.radius)):
                    distance = sqrt((particle.x - colliding_particle.x) * (particle.x - colliding_particle.x) + (particle.y - colliding_particle.y) * (particle.y - colliding_particle.y))
                    intersection_distance = particle.radius + colliding_particle.radius - distance
                    collision_x = (particle.x - colliding_particle.x) / distance
                    collision_y = (particle.y - colliding_particle.y) / distance

                    particle.x += collision_x * intersection_distance
                    particle.y += collision_y * intersection_distance

                    colliding_particle.x -= collision_x * intersection_distance
                    colliding_particle.y -= collision_y * intersection_distance

                    # Dyanmic Collision
                    tangent_x = -collision_y
                    tangent_y = collision_x

                    dptan1 = tangent_x * particle.v_x + tangent_y * particle.v_y
                    dptan2 = tangent_x * colliding_particle.v_x + tangent_y * colliding_particle.v_y

                    dpnorm1 = collision_x * particle.v_x + collision_y * particle.v_y
                    dpnorm2 = collision_x * colliding_particle.v_x + collision_y * colliding_particle.v_y 
                     
                    m1 = (dpnorm1 * (particle.mass - colliding_particle.mass) + 2.0 * colliding_particle.mass * dpnorm2) / (particle.mass + colliding_particle.mass)
                    m2 = (dpnorm2 * (colliding_particle.mass - particle.mass) + 2.0 * particle.mass * dpnorm1) / (particle.mass + colliding_particle.mass)

                    particle.v_x = dptan1 * tangent_x + collision_x * m1
                    particle.v_y = dptan1 * tangent_y + collision_y * m1
                    colliding_particle.v_x = dptan2 * tangent_x + collision_x * m2
                    colliding_particle.v_y = dptan2 * tangent_y + collision_y * m2

                
    for particle in particles:
        particle.v_y += gravity * (elapsed/10)
        particle.x += particle.v_x * (elapsed/10)
        particle.y += particle.v_y * (elapsed/10)
        if(particle.x >= SimpleGraphics.GetWidth() - particle.radius or particle.x <= particle.radius):
            particle.v_x = -particle.v_x * RESTITUTION
        if(particle.y >= SimpleGraphics.GetHeight() - particle.radius or particle.y <= particle.radius):
            particle.v_y = -particle.v_y * RESTITUTION

        if(particle.x < particle.radius): particle.x = particle.radius
        if(particle.y < particle.radius): particle.y = particle.radius
        if(particle.x >= SimpleGraphics.GetWidth() - particle.radius): particle.x = SimpleGraphics.GetWidth()-particle.radius
        if(particle.y >= SimpleGraphics.GetHeight() - particle.radius): particle.y = SimpleGraphics.GetHeight()-particle.radius 

        if(abs(particle.v_x*particle.v_x + particle.v_y*particle.v_y) < 0.0001): particle.v_x = 0; particle.v_y = 0


    return

def OnKeyPress(elapsed, key):
    global particles, isPivoted, pivotX, pivotY, mouseX, mouse
    if(key == SimpleGraphics.BTN_MOUSE1):
        isPivoted = True
        pivotX = mouseX
        pivotY = mouseY
    return

def OnKeyRelease(elapsed, key):
    global isPivoted
    if(key == SimpleGraphics.BTN_MOUSE1):
        isPivoted = False
        length_X = abs(pivotX - launchX)/5
        length_Y = abs(pivotY - launchY)/5
        particles.append(Particle(launchX, launchY, 10, length_X * numpy.sign((pivotX - launchX)), length_Y*numpy.sign((pivotY-launchY))))

def OnKeyPressed(elapsed, key):
    return
    
def Draw(elapsed):
    global particles, mouseX, mouseY, launchX, launchY
    SimpleGraphics.Clear(0,0,0)

    for particle in particles:
        SimpleGraphics.DrawCircle(particle.x, particle.y, particle.radius, 255, 0, 0, False)
    
    if(isPivoted):
        launchX = mouseX
        launchY = mouseY
        SimpleGraphics.DrawCircle(pivotX, pivotY, 5, 255, 255, 0)
        if(pivotX - launchX) ** 2 + (pivotY - launchY) ** 2 > MAX_LENGTH*MAX_LENGTH:
            sin_theta = 0
            cos_theta = 0
            tan_theta = 0
            sign_x = numpy.sign(launchX - pivotX)
            sign_y = numpy.sign(launchY - pivotY)
            if(pivotX - launchX == 0):
                if(pivotY > launchY):
                    sin_theta = -1
                    cos_theta = 0
                else:
                    sin_theta = 1
                    cos_theta = 0
            else:
                tan_theta = (launchY - pivotY) / (launchX - pivotX)
                hypotenuse = sqrt (1 + tan_theta * tan_theta) 
                sin_theta = tan_theta / hypotenuse
                cos_theta = sign_x * 1 / hypotenuse
                if(cos_theta < 0):
                    sin_theta = -sin_theta
            SimpleGraphics.DrawString("SIN: " + str(sin_theta) + " COS: " + str(cos_theta) + "TAN: " + str(tan_theta), 0, 16, 255, 255, 255)
            launchX = pivotX + MAX_LENGTH * cos_theta
            launchY = pivotY + MAX_LENGTH * sin_theta
        SimpleGraphics.DrawLine(pivotX, pivotY, launchX, launchY, 255, 30, 30)
        SimpleGraphics.DrawCircle(launchX, launchY, 3, 255, 255, 0)
    SimpleGraphics.DrawString("BALLS: " + str(len(particles) ), 0,0, 255, 255, 255)
    SimpleGraphics.DrawString("CLICK AND PULL TO THROW BALLS!", 0, SimpleGraphics.GetHeight()-16, 255, 255, 255)
    SimpleGraphics.FrameCap(60)
    return

def OnMouseMove(elapsed, x, y):
    global mouseX, mouseY
    mouseX = x
    mouseY = y
    return

SimpleGraphics.Run(800, 600, 800, 600, Create, Update, Draw, OnKeyPress, OnKeyPressed, OnKeyRelease, OnMouseMove, 0)
SimpleGraphics.Quit()
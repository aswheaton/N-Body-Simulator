"""
    Class for a gravitational body in an n-body simulator.
    Author: Alexander S. Wheaton
    Date: 29 January 2018
    Updated: 5 April 2018
"""

from Vector import Vector

class Body(object):
    
    G = float(6.674e-11)
    
    def __init__(self, name, mass, radius, colour, initialPosition, initialVelocity, initialAcceleration):
        
        self.name = name
        self.mass = mass
        self.radius = radius
        self.colour = colour

        self.posLast = Vector(initialPosition)
        self.velLast = Vector(initialVelocity)
        self.accLast = Vector(initialAcceleration)

        self.pos = Vector(initialPosition)
        self.vel = Vector(initialVelocity)
        self.acc = Vector(initialAcceleration)

        self.posNext = Vector(initialPosition)
        self.velNext = Vector(initialVelocity)
        self.accNext = Vector(initialAcceleration)
        
    def beemanPosition(self, timestep):
        
        posNext = self.pos + self.vel * timestep + (1.0/6.0) * ( 4.0 * self.acc - self.accLast ) * timestep ** 2
        
    def beemanAcceleration(self, system):
    
        netForce = Vector([0.0, 0.0, 0.0])
        
        for n in range(len(system)):
            if system[n].name != self.name:
                radius = system[n].posNext - self.posNext
                force = Body.G * system[n].mass * self.mass * radius / radius.mag() ** 3
                netForce = netForce + force

        self.accNext = netForce / self.mass
        
    def beemanVelocity(self, timestep):
        
        self.velNext = self.vel + (1.0/6.0) * (2.0 * self.accNext + 5.0 * self.acc - self.accLast) * timestep

    def stepForward(self):
        
        self.posLast = self.pos
        self.velLast = self.vel
        self.accLast = self.acc
        
        self.pos = self.posNext
        self.vel = self.velNext
        self.acc = self.accNext

"""
    Class for a gravitational body in an n-body simulator.
    Author: Alexander S. Wheaton
    Date: 29 January 2018
    Updated: 2 April 2018
"""

from Vector import Vector

class Body(object):
    
    G = float(6.674e-11)
    
    def __init__(self, name, mass, radius, colour, initialPosition, initialVelocity):
        
        self.name = name
        self.mass = mass
        self.radius = radius
        self.colour = colour

        self.position = Vector(initialPosition)
        self.velocity = Vector(initialVelocity)
        self.acceleration = Vector(initialAcceleration)

    def getForce(self, system):
    
        netForce = Vector([0.0, 0.0, 0.0])
        
        for n in range(len(system)):
            if system[n].name != self.name:
                radius = system[n].position - self.position
                force = G * system[n].mass * self.mass * radius / radius.mag() ** 3
                netForce = netForce + force
        return(netForce)
    
    def getPosition(self):
        return(self.position)

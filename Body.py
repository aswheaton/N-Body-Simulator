"""
    Class for a gravitational body in an n-body simulator.
    Author: Alexander S. Wheaton
    Date: 29 January 2018
    Updated: 29 January 2018
"""

def class Body(object):

    def __init__(self, name, mass, radius, position, velocity):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.position = position
        self.velocity = velocity

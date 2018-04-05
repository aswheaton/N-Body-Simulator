"""
    N-dimensional vector class object.
    Author: Alexander S. Wheaton
    Date: 1 April 2018
    Updated: 5 April 2018
"""

import math

class Vector(object):

    def __init__(self, components):

        self.dimension = len(components)
        self.vector = components
        self.index = 0
    
    def __getitem__(self, key):
        
        return(self.vector[key])
        
    def __add__(self, other):

        components = []

        for i in range(self.dimension):
            components.append(self.vector[i] + other.vector[i])
        return(Vector(components))

    def __sub__(self, other):

        components = []

        for i in range(self.dimension):
            components.append(self.vector[i] - other.vector[i])
        return(Vector(components))

    def __mul__(self, other):

        components = []

        for i in range(self.dimension):
            components.append(other * self.vector[i])
        return(Vector(components))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self, other):

        components = []

        for i in range(self.dimension):
            components.append(self.vector[i] / other)
        return(Vector(components))

    def __truediv__(self, other):

        components = []

        for i in range(self.dimension):
            components.append(self.vector[i] / other)
        return(Vector(components))

    def mag(self):
        
        sumsqares = 0.0

        for i in range(self.dimension):
            sumsqares = sumsqares + self.vector[i]**2
        return(math.sqrt(sumsqares))

    def norm(self):
        return(self / self.mag())

    def dot(self, other):

        scalarSum = 0.0

        for i in range(self.dimension):
            scalarSum = scalarSum + self.vector[i] * other.vector[i]
        return(scalarSum)

    def cross(self, other):
        
        components = []
        
        components.append(self.vector[1]*other.vector[2]-self.vector[2]*other.vector[1])
        components.append(-(self.vector[0]*other.vector[2]-self.vector[2]*other.vector[0]))
        components.append(self.vector[0]*other.vector[1]-self.vector[1]*other.vector[0])
        
        return(Vector(components))
    
    # Returns the components of the vector as a list.
    def __str__(self):
        return(str(self.vector))

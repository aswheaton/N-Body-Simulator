"""
    N-dimensional vector class object.
    Author: Alexander S. Wheaton
    Date: 1 April 2018
    Updated: 7 April 2018
"""

import math

class Vector(object):

    def __init__(self, components):

        self.dimension = len(components)
        self.vector = components
    
    def __getitem__(self, key):
        
        # Syntax for accessing components of the vector with a key.
        
        return(self.vector[key])
        
    def __add__(self, other):
        
        # Addition for vectors.
        
        components = []

        for i in range(self.dimension):
            components.append(self.vector[i] + other.vector[i])
        return(Vector(components))

    def __sub__(self, other):
        
        # Subtraction for vectors.
        
        components = []

        for i in range(self.dimension):
            components.append(self.vector[i] - other.vector[i])
        return(Vector(components))

    def __mul__(self, other):
        
        # Scalar multiplication for vectors.
        
        components = []

        for i in range(self.dimension):
            components.append(other * self.vector[i])
        return(Vector(components))

    def __rmul__(self, other):
        
        # Commutative scalar multiplication for vectors.
        
        return self.__mul__(other)

    def __div__(self, other):
        
        # Scalar division for vectors.
        
        components = []
        
        for i in range(self.dimension):
            components.append(self.vector[i] / other)
        return(Vector(components))
        
    def __truediv__(self, other):
        
        # Scalar division for vectors.
        
        components = []

        for i in range(self.dimension):
            components.append(self.vector[i] / other)
        return(Vector(components))

    def mag(self):
        
        # Calculates and returns the magnitude of the vector.
        
        sumsqares = 0.0

        for i in range(self.dimension):
            sumsqares = sumsqares + self.vector[i]**2
        return(math.sqrt(sumsqares))

    def norm(self):
        
        # Calculates and returns a normalised unit vector parallel to the vector.
        
        return(self / self.mag())

    def dot(self, other):
        
        # Scalar product of two vectors.
        
        scalarSum = 0.0

        for i in range(self.dimension):
            scalarSum = scalarSum + self.vector[i] * other.vector[i]
        return(scalarSum)

    def cross(self, other):
        
        # Vector product of two vectors.
        
        components = []
        
        components.append(self.vector[1]*other.vector[2]-self.vector[2]*other.vector[1])
        components.append(-(self.vector[0]*other.vector[2]-self.vector[2]*other.vector[0]))
        components.append(self.vector[0]*other.vector[1]-self.vector[1]*other.vector[0])
        
        return(Vector(components))
    
    def __str__(self):
        
        # Returns the components of the vector as a list.
        
        return(str(self.vector))

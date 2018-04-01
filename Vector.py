"""
    N-dimensional vector class object.
    Author: Alexander S. Wheaton
    Date: 1 April 2018
    Updated: 1 April 2018
"""

import math

class Vector(object):

    def __init__(self, components):

        self.dimension = len(components)
        self.vector = components

    def __add__(self, other):

        components = []

        for i in range(self.dimension):
            components.append(self.vector[i] + other.vector[i])
        return(Vector(components))

    def __subtract__(self, other):

        components = []

        for i in range(self.dimension):
            components.append(self.vector[i] - other.vector[i])
        return(Vector(components))

    def __multiply__(self, other):

        components = []

        for i in range(self.dimension):
            components.append(other * self.vector[i])
        return(Vector(components))

    def norm(self):
        
        norm = 0

        for i in range(self.dimension):
            norm = norm + self.vector[i]**2
        return(math.sqrt(norm))

    def dot(self, other):

        scalarSum = 0

        for i in range(self.dimension):
            scalarSum = scalarSum + self.vector[i] * other.vector[i]
        return(scalarSum)

    def cross(self, other):
        
        components = []
        
        components.append(self.vector[1]*other.vector[2]-self.vector[2]*other.vector[1])
        components.append(-(self.vector[0]*other.vector[2]-self.vector[2]*other.vector[0]))
        components.append(self.vector[0]*other.vector[1]-self.vector[1]*other.vector[0])
        
        return(Vector(components))
        
        # Code for an n-dimensional cross product. Work in progress. Code above works for three dimensional vectors only.
        # 
        # for i in range(self.dimension):
        #     components.append(0)
        #     for j in range(self.dimension):
        #         if j != i:
        #             for k in range(self.dimension):
        #                 if k != i:
        #                     if k > j:
        #                         components[i] += self.vector[j]*other.vector[k]
        #                     elif k < j:
        #                         components[i] -= self.vector[j]*other.vector[k]

    def list(self):
        return(self.vector)

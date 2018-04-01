"""
    Three dimensional vector class object.
    Author: Alexander S. Wheaton
    Date: 1 April 2018
    Updated: 1 April January 2018
"""

def class Vector(object):

    def __init__(self, components):

        self.dimension = len(components)
        self.vector = components

    def __add__(self, other):

        components = []

        for i in len(self.dimension):
            components.append(self.vector[i] + other.vector[i])
        return(Vector(components))

    def __subtract__(self, other):

        components = []

        for i in len(self.dimension):
            components.append(self.vector[i] - other.vector[i])
        return(Vector(components))

    def dot(self, other):

        scalarSum = 0

        for i in len(self.dimension):
            scalarSum = scalarSum + self.vector[i] * other.vector[i]
        return(scalarSum)

    def cross(self, other):
        components = []
        for i in range(self.dimension):
            components.append(0)
            for j in range(self.dimension):
                if j != i:
                    for k in range(self.dimension):
                        if k != i:
                            if k > j:
                                components[i] += self.vector[j]*other.vector[k]
                            elif k < j:
                                components[i] -= self.vector[j]*other.vector[k]
        return(Vector(components))

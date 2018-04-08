"""
    Class for a gravitational body in an n-body simulator.
    Author: Alexander S. Wheaton
    Date: 29 January 2018
    Updated: 7 April 2018
"""

from Vector import Vector

class Body(object):
    
    G = float(6.674e-11)
    
    def __init__(self, name, mass, radius, colour, initialPosition, initialVelocity, initialAcceleration):
        
        # Set some attributes to be accessed by a plotting function and for use in force calculation.
        
        self.name = name
        self.mass = mass
        self.radius = radius
        self.colour = colour
        
        # Last, current, and next position are all set to an initial condition (the first step forward is just a linear velocity * time).
        
        self.posLast = Vector(initialPosition)
        self.velLast = Vector(initialVelocity)
        self.accLast = Vector(initialAcceleration)

        self.pos = Vector(initialPosition)
        self.vel = Vector(initialVelocity)
        self.acc = Vector(initialAcceleration)

        self.posNext = Vector(initialPosition)
        self.velNext = Vector(initialVelocity)
        self.accNext = Vector(initialAcceleration)
        
        # Used to calculate the period.
        
        self.hasOrbited = False
        
    def beemanPosition(self, timestep):
        
        # Calculates and sets the next position vector using the Beeman numerical integration algorithm.
        
        self.posNext = self.pos + self.vel * timestep + (1.0/6.0) * ( 4.0 * self.acc - self.accLast ) * timestep ** 2
        
    def beemanAcceleration(self, system):
        
        # Calculates a net force vector object at the next position using Newton's Law of Gravitation and sets the acceleration vector at that position.
        
        netForce = Vector([0.0, 0.0, 0.0])
        
        for n in range(len(system)):
            if system[n].name != self.name:
                radius = system[n].posNext - self.posNext
                force = Body.G * system[n].mass * self.mass * radius / radius.mag() ** 3
                netForce = netForce + force

        self.accNext = netForce / self.mass
        
    def beemanVelocity(self, timestep):
        
        # Calculates and sets the velocity at the next position vector using the Beeman numerical integration algorithm.
        
        self.velNext = self.vel + (1.0/6.0) * (2.0 * self.accNext + 5.0 * self.acc - self.accLast) * timestep

    def stepForward(self, timestep, timeElapsed):
        
        # Checks if the body has completed an orbit and, if so, records the period.
        
        if ((self.posLast[1] < 0.0) and (self.posNext[1] > 0.0) and (self.hasOrbited == False)):
            self.period = timeElapsed
            self.hasOrbited = True
            print("The period of " + str(self.name) + " is " + str(self.period) + " seconds.")
        
        # Increments the body to the next position and discards the last position. 
        
        self.posLast = self.pos
        self.velLast = self.vel
        self.accLast = self.acc
        
        self.pos = self.posNext
        self.vel = self.velNext
        self.acc = self.accNext
        
    def getKineticEnergy(self):
        
        # Calculates and returns the kinetic energy.
        
        return(0.5 * self.mass * self.vel.mag() ** 2)
    
    def getGravitationalEnergy(self, system):
        
        # Calculates and returns the gravitational potential energy due to other bodies in the system.
        
        potentialEnergy = 0.0
        
        for n in range(len(system)):
            if system[n].name != self.name:
                radius = system[n].posNext - self.posNext
                potentialEnergy = Body.G * system[n].mass * self.mass / radius.mag()
        
        return(potentialEnergy)
        
    def closestApproach(self, system):
        
        # Records the distance to Mars for a probe called "Pan".
           
        if self.name == "Pan":
            try:
                self.distanceToMars.append((system[4].pos - self.pos).mag())    
            except AttributeError:
                self.distanceToMars = []
        
    def getPeriod(self):
        
        # Returns the period. Should not be called while the simulation is running.
        
        return(self.period)

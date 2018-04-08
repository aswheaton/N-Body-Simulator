"""
    N-body simulation class object.
    Author: Alexander S. Wheaton
    Date: 29 March 2018
    Updated: 7 April 2018
"""

import matplotlib.pyplot

from matplotlib.animation import FuncAnimation

from Body import Body

class Simulation(object):
    
    def __init__(self, filename, timestep, maxIterations, probeExists):
        
        # Recieves a datafile and generates a list of Body type objects.
                
        self.system = []
        
        datafile = open(filename, "r")

        for line in datafile.readlines():
            tokens = line.split(", ")
            self.system.append(Body(str(tokens[0]), float(tokens[1]), float(tokens[2]), str(tokens[3]), [float(i) for i in tokens[4].split(",")], [float(i) for i in tokens[5].split(",")], [float(i) for i in tokens[6].split(",")]))
        
        datafile.close()
        
        # Sets some initial parameters for the simulation and constants energy and animation methods.
        
        self.elapsedTime = 0.0
        self.timestep = timestep
        self.maxIterations = maxIterations
        
        self.probeExists = probeExists
        self.hasLaunched = False
        
    def stepForward(self):
        
        # Calculates the next position, acceleration, and velocity of each body in the system using the Beeman numerical integration algorithms.
        
        for n in range(len(self.system)):
            self.system[n].beemanPosition(self.timestep)
        for n in range(len(self.system)):
            self.system[n].beemanAcceleration(self.system)
        for n in range(len(self.system)):
            self.system[n].beemanVelocity(self.timestep)

        # Moves every body in the system to its next calculated position.
        
        for n in range(len(self.system)):
            self.system[n].stepForward(self.timestep, self.elapsedTime)
        
    def exportEnergy(self):
        
        # Opens the file in write mode on first call, append mode afterwards.
        
        if hasattr(self, "energyFile"):
            self.energyFile = open("energy.txt", "a")
        else:
            self.energyFile = open("energy.txt", "w")
        
        # Writes the current time, kinetic, potential, and total energies to a file.
        
        totalKineticEnergy = 0.0
        totalPotentialEnergy = 0.0
        
        for n in range(len(self.system)):
            totalKineticEnergy = totalKineticEnergy + self.system[n].getKineticEnergy()
            totalPotentialEnergy = totalPotentialEnergy + self.system[n].getGravitationalEnergy(self.system)
            
        totalPotentialEnergy = totalPotentialEnergy / 2.0
        
        self.energyFile.write(str(self.elapsedTime) + ", " + str(totalKineticEnergy) + ", " + str(totalPotentialEnergy) + ", " + str(totalKineticEnergy + totalPotentialEnergy) + "\n")
        
        self.energyFile.close()
    
    def launchProbe(self):
        
        # Checks that there is a probe to be launched and that more than two Earth years have transpired.
        
        if ((self.probeExists == True) and (self.hasLaunched == False) and (self.elapsedTime > float(6.31152e7))):
            
            print("Launching probe..."),
            
            # Imports a probe file with a name, mass, size, colour, and initial velocity.
            
            datafile = open("probe.txt", "r")
            tokens = datafile.read().split(", ")
            
            # Adds a new body, the probe, to the system at the position of the Earth with initial velocity from the datafile.
            
            self.system.append(Body(str(tokens[0]), float(tokens[1]), float(tokens[2]), str(tokens[3]), [float(i) for i in self.system[3].pos], [float(i) for i in tokens[4].split(",")], [0.0,0.0,0.0]))
            
            # Adds the new body to the patches and updates the axes. 
            
            self.patches.append(matplotlib.pyplot.Circle((self.system[-1].pos[0], self.system[-1].pos[1]), 20000000.0 * self.system[-1].radius, color = self.system[-1].colour, animated = True))
            self.axes.add_patch(self.patches[-1])
            
            datafile.close()
            
            # Flag so the launch only happens once.
            
            self.hasLaunched = True
            
            print("Probe launched successfully!")
            
    def getClosestApproach(self):
        
        # Finds and returns the closest approach of a probe called "Pan" to Mars.
        
        if self.system[-1].name == "Pan":
            print("The closest approach of " + str(self.system[-1].name) + " to Mars is " + str(min(self.system[-1].distanceToMars)) + " meters.")
        else:
            print("No probe was launched.")
    
    # This block updates and animates the simulation by calling the stepForward() method and using FuncAnimation.
    
    def animate(self, i):
        
        # Launches a probe, if certain conditions are met.
        
        self.launchProbe()
        
        # Steps the simulation forward, increments the time, and exports the energy of the system to a file.
        
        self.stepForward()
        
        self.elapsedTime = self.elapsedTime + self.timestep
        
        self.exportEnergy()
        
        # Calculates the closest approach of any probes to their targets.
        
        for n in range(len(self.system)):
            self.system[n].closestApproach(self.system)
        
        # Updates the position of each patch with the new simulation data.
        
        for n in range(len(self.system)):
            self.patches[n].center = (self.system[n].pos[0], self.system[n].pos[1])
        
        return(self.patches)

    def display(self):
        
        # Creates figure and axes elements. Scales and labels them appropriately.
        
        self.figure = matplotlib.pyplot.figure()
        self.axes = matplotlib.pyplot.axes()
        self.axes.axis('scaled')
        self.axes.set_xlim(-float(3e11), float(3e11))
        self.axes.set_ylim(-float(3e11), float(3e11))
        self.axes.set_xlabel('x-coordinate (m)')
        self.axes.set_ylabel('y-coordinate (m)')

        # Creates a list of circles to be plotted by pyplot and adds them to the axes.
        
        self.patches = []

        for n in range(len(self.system)):
            if self.system[n].name == "Sol":
                self.patches.append(matplotlib.pyplot.Circle((self.system[n].pos[0], self.system[n].pos[1]), 10.0 * self.system[n].radius, color = self.system[n].colour, animated = True))
            else:
                self.patches.append(matplotlib.pyplot.Circle((self.system[n].pos[0], self.system[n].pos[1]), 1000.0 * self.system[n].radius, color = self.system[n].colour, animated = True))
        
        for n in range(0, len(self.patches)):
            self.axes.add_patch(self.patches[n])
        
        # Animates the plot.
        
        self.animation = FuncAnimation(self.figure, self.animate, frames = self.maxIterations, repeat = False, interval = 20, blit = True)
        
        # Show the plot.
        
        matplotlib.pyplot.show()
        
    def exportAnimation(self, filename, dotsPerInch):
        
        # Exports the animation to a .gif file without compression. (Linux distributions with package "imagemagick" only. Files can be large!)
        
        self.animation.save(filename, dpi=dotsPerInch, writer="imagemagick")

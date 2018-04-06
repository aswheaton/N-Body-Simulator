"""
    N-body simulation class object.
    Author: Alexander S. Wheaton
    Date: 29 March 2018
    Updated: 5 April 2018
"""

import matplotlib.pyplot

from matplotlib.animation import FuncAnimation

from Body import Body

class Simulation(object):
    
    # Recieves a datafile and generates a list of Body type objects.
    def __init__(self, filename, timestep):
                
        self.system = []
        
        datafile = open(filename, "r")

        for line in datafile.readlines():
            tokens = line.split(", ")
            self.system.append(Body(str(tokens[0]), float(tokens[1]), float(tokens[2]), str(tokens[3]), [float(i) for i in tokens[4].split(",")], [float(i) for i in tokens[5].split(",")], [float(i) for i in tokens[6].split(",")]))
        
        self.timestep = timestep
        
        datafile.close()

    def stepForward(self):
        
        for n in range(len(self.system)):
            self.system[n].beemanPosition(self.timestep)
        for n in range(len(self.system)):
            self.system[n].beemanAcceleration(self.system)
        for n in range(len(self.system)):
            self.system[n].beemanVelocity(self.timestep)

        # Updates the position of every body in the system.
        for n in range(len(self.system)):
            self.system[n].stepForward(self.timestep)
        
    def exportEnergy(self):
        
        datafile = open("energy.txt", "w")
        
        totalKineticEnergy = 0.0
        totalPotentialEnergy = 0.0
        
        for n in range(len(system)):
            totalKineticEnergy = totalKineticEnergy + self.system[n].getKineticEnergy()
            totalPotentialEnergy = totalPotentialEnergy + self.system[n].getGravitationalEnergy(self.system)
            
        totalPotentialEnergy = totalPotentialEnergy / 2.0
        
        datafile.write(str(elapsedTime) + ", " + str(totalKineticEnergy) + ", " + str(totalPotentialEnergy) + ", " + str(totalKineticEnergy + totalPotentialEnergy) + "\n")
        
        datafile.close()
    
    # This block updates and animates the simulation by calling the stepForward() method and using FuncAnimation.      
    # Updates the position of each patch with the new simulation data by calling Beeman algorithm functions and stepping the simulation forward.
    def animate(self, i):
        
        self.stepForward()
        
        for n in range(len(self.system)):
            self.patches[n].center = (self.system[n].pos[0], self.system[n].pos[1])
        return(self.patches)
        
        self.exportEnergy(self.timestep * i)

    def display(self):
        
        # Creates figure and axes elements. Scales and labels them appropriately.
        figure = matplotlib.pyplot.figure()
        axes = matplotlib.pyplot.axes()
        axes.axis('scaled')
        axes.set_xlim(-float(3e11), float(3e11))
        axes.set_ylim(-float(3e11), float(3e11))
        axes.set_xlabel('x-coordinate (m)')
        axes.set_ylabel('y-coordinate (m)')

        # Creates a list of circles to be plotted by pyplot.
        self.patches = []

        for n in range(len(self.system)):
            if self.system[n].name == "Sol":
                self.patches.append(matplotlib.pyplot.Circle((self.system[n].pos[0], self.system[n].pos[1]), 10.0 * self.system[n].radius, color = self.system[n].colour, animated = True))
            else:
                self.patches.append(matplotlib.pyplot.Circle((self.system[n].pos[0], self.system[n].pos[1]), 1000.0 * self.system[n].radius, color = self.system[n].colour, animated = True))
        for n in range(0, len(self.patches)):
            axes.add_patch(self.patches[n])
        
        # Animates the plot.
        animation = FuncAnimation(figure, self.animate, frames = 1, repeat = True, interval = 10, blit = True)
        
        # Show the plot.
        matplotlib.pyplot.show()

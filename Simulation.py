"""
    N-body simulation class object.
    Author: Alexander S. Wheaton
    Date: 29 March 2018
    Updated: 2 April 2018
"""

import matplotlib.pyplot

from matplotlib.animation import FuncAnimation

from Vector import Vector
from Body import Body

class Simulation(object):
    
    # Recieves a datafile and generates a list of Body type objects.
    def __init__(self, filename, timestep):
                
        self.system = []
        
        datafile = open(filename, "r")

        for line in datafile.readlines():
            tokens = line.split(", ")
            self.system.append(Body(tokens[0], tokens[1], tokens[2], tokens[3], tokens[4], tokens[5], tokens[6]))
        
        self.timestep = timestep
    
    def stepForward(self):
        
        # Updates the position of every body in the system.
        for n in range(len(self.system)):
            self.system[n].stepForward()
    
    # This block updates and animates the simulation by calling the stepForward() method and using FuncAnimation.    
    
    # Initialiser for the animator.
    def init(self):
        return(self.patches)
    
    # Updates the position of each patch with the new simulation data by calling Beeman algorithm functions and stepping the simulation forward.
    def animate(self, i):
        
        for n in range(len(self.system)):
            self.system[n].beemanPosition(self.timestep)
        for n in range(len(self.system)):
            self.system[n].beemanAcceleration()
        for n in range(len(self.system)):
            self.system[n].beemanVelocity(self.timestep)
        
        self.stepForward()
        
        for n in range(len(self.system)):
            self.patches[n].center = self.system[n].pos
        return(self.patches)

    def display(self):
        
        # Creates figure and axes elements. Scales and labels them appropriately.
        figure = matplotlib.pyplot.figure()
        axes = matplotlib.pyplot.axes()
        axes.axis('scaled')

        # Creates a list of circles to be plotted by pyplot.
        self.patches = []

        for n in range(len(self.system)):
            self.patches.append(matplotlib.pyplot.Circle(self.system[n].pos.list(), self.system[n].radius, color = self.system[n].colour, animated = True))
        
        for n in range(0, len(self.patches)):
            axes.add_patch(self.patches[n])
        
        # Animates the plot.
        animation = FuncAnimation(figure, self.animate, init_func = self.init, frames = 1, repeat = True, interval = 0.1, blit = True)
        
        # Show the plot.
        matplotlib.pyplot.show()

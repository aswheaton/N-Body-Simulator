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
    def __init__(self, filename):
                
        self.system = []
        
        datafile = open(filename, "r")

        for line in datafile.readlines():
            tokens = line.split(", ")
            self.system.append(Body(tokens[0], tokens[1], tokens[2], tokens[3], tokens[4], tokens[5], tokens[6])
    
    def stepForward(self):
        
        # Updates the position of every body in the system.
        for i in range(len(self.system)):
            self.system[i].stepForward()
    
    # This block updates and animates the simulation by calling the stepForward() method and using FuncAnimation.    
    
    # Initialiser for the animator.
    def init(self):
        return(self.patches)
    
    # Updates the position of each patch with the new simulation data.
    def animate(self, i):
        
        self.stepForward()
        
        for i in range(len(self.system))
            self.patches[i].center = (self.system[i].getPosition())
        return self.patches

    def display(self):
        
        # Creates figure and axes elements. Scales and labels them appropriately.
        figure = matplotlib.pyplot.figure()
        axes = matplotlib.pyplot.axes()
        axes.axis('scaled')

        # Creates a list of circles to be plotted by pyplot.
        patches = []

        for i in range(len(self.system))
            patches.append(plt.Circle((self.system[i].getPostion(), self.system[i].radius, color = self.system[i].colour, animated = True)))
        
        for i in range(0, len(self.patches)):
            axes.add_patch(self.patches[i])
        
        # Animates the plot.
        animation = FuncAnimation(figure, self.animate, init_func = self.init, frames = 1, repeat = True, interval = 0.1, blit = True)
        
        # Show the plot.
        matplotlib.pyplot.show()

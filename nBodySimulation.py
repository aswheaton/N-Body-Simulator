"""
    Test code for n-body simulation class object.
    Author: Alexander S. Wheaton
    Date: 29 March 2018
    Updated: 1 April 2018
"""

from Simulation import Simulation

simulation = Simulation("sol.txt", 1000) #input("Specify a datafile or use a preset: "))

simulation.display()

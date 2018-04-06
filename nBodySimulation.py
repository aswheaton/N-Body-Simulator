"""
    Test code for n-body simulation class object.
    Author: Alexander S. Wheaton
    Date: 29 March 2018
    Updated: 7 April 2018
"""

from Simulation import Simulation

def main():

    while raw_input("Run a simulation (r) or quit (q): ") != "q":
    
        filename = "sol.txt" # input("Specify a preset n-body system file: ")
        timestep = 24 * 3600 # input("specify a timestep (s): ")
        maxIterations = 100000 # int(input("To how many iterations should the simulation be run: "))
        simulation = Simulation(filename, timestep, maxIterations)

        simulation.display()
        
main()

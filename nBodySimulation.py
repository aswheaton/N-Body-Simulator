# Test comment for pushing to get.

"""
    Test code for n-body simulation class object.
    Author: Alexander S. Wheaton
    Date: 29 March 2018
    Updated: 7 April 2018
"""

from Simulation import Simulation

def main():

    while raw_input("Run a simulation (r) or quit (q): ") != "q":
    
        systemFilename = raw_input("Specify a preset n-body system file (i.e. sol.txt): ")
        timestep = int(input("Specify a timestep (i.e. 43200) in seconds: "))
        maxIterations = int(input("To how many iterations (2500 to 5000 work well) should the simulation be run: "))
        
        # Permits the user to run the simulation without a probe.
        
        if raw_input("Launch a probe (y/n): ") == "y":
            probeFilename = raw_input("Specify a preset probe file (i.e. probe.txt): ")
            simulation = Simulation(systemFilename, timestep, maxIterations, True)
        else:
            simulation = Simulation(systemFilename, timestep, maxIterations, False)
        
        # Run the simulation and animates it.
        
        simulation.display()
        simulation.getClosestApproach()
        
        # Permits the user to export the animation. (Linux distributions with package "imagemagick" only. Files can be large!)
        
        if raw_input("Export the animation (not recommended for more than 2500 iterations) (y/n): ") == "y":
        
            filename = raw_input("Specify a filename (i.e. sol.gif): ")
            dotsPerInch = int(input("At what resolution (20-80 dpi works well) should the animation be exported: "))
            
            print("Exporting animation..."),
            simulation.exportAnimation(filename, dotsPerInch)
            print("Done!")
        
main()

# Calculations for Galvo placement and angles
#
# Input: Various heights of galvo
# Output: Corresponding galvo angles

import numpy as np

d = 30                 # Diamter of mirror array
hs = 40                # Height of sample (this is variable)
hg = np.arange(30,150)   # Various possible heights for galvo (cm)
phi = np.arctan(d/2/hg)           # POV Galvo mirror: Angle between vertical and ray to center of mirror array 
phi_p = np.arctan(2*np.tan(d/hg)) # POV Galvo mirror: Angle between vertical and ray to opposite extremum of mirror array
psi = np.arctan(d/2/hs)           # POV Sample: Angle between vertical and extremums of mirror array
# convert to degrees
phi,phi_p,psi = phi*180/np.pi, phi_p*180/np.pi, psi*180/np.pi

print(phi_p)

# Calculations for mirror angles
#
# Computational Imaging Lab
# University of California, Berkeley
# Copyright 2020 Grant J. Kirchhoff
# gkirchhoff32@berkeley.edu
#
# Input: Galvo height, sample height, mirror positions from 'mirror_array_diameter.py'
# Output: Corresponding mirror angles

import numpy as np
import math
from mirror_array_diameter import mirror_array_dims
import matplotlib.pyplot as plt

### PARAMETERS ###
mr_dia = 9e-3           # (m) Diameter of each mirror.
length_space = 4*mr_dia # (m) Length of space between mirrors. I assume space between mirrors is same dimension.
#num_dia = 21           # Desired number of mirrors in array diameter (make sure it's ODD).
hs = 0.11               # (m) Height of sample (variable)
hg = 0.1                # (m) Height of galvo (variable) (m)

#num_rad = math.floor(num_dia/2)
#d = 2*(num_rad)*(length_space+mr_dia)+mr_dia # Diameter of mirror array
#print('Diameter of Array:','{0:.4f}'.format(d), 'm')

dia = 0.5 # Input diameter
dia_avail = dia - mr_dia # Subtract out middle mirror
poss_ring_num = np.round(dia_avail/2/(mr_dia+length_space)) # Number of rings to get as close as possible\
                                                          # to input diameter (excluding center mirror)
num_dia = 2*poss_ring_num+1 # Add one to include center mirror
num_rad = math.floor(num_dia/2)
d = 2*(num_rad)*(length_space+mr_dia)+mr_dia # Diameter of mirror array
print('Diameter of Array:','{0:.4f}'.format(d), 'm')


### CALCULATIONS ###
phi = np.arctan(d/2/hg)           # POV Galvo mirror: Angle between vertical and ray to center of mirror array 
phi_p = np.arctan(d/hg)
psi = np.arctan(d/2/hs)           # POV Sample: Angle between vertical and extremums of mirror array
phi,phi_p,psi = phi*180/np.pi, phi_p*180/np.pi, psi*180/np.pi # Convert to degrees

# X and Y are mirror coords
x,y = mirror_array_dims(mr_dia,length_space,num_dia)
X,Y = np.array(x),np.array(y)

# Extrema of mirror coords
x_ext = [np.max(X),np.min(X)]
y_ext = [np.max(Y),np.min(Y)]

# Check Notebook for geometry in x and y
# OUTPUT: mirror declinations and sample angles of incidence in DEGREES
def theta_x(A,d,hg,hs):
    phi_prime = np.arctan((d-(2*A))/(2*hg))
    chi_prime = -1*np.arctan(A/hs) # Chi prime is x-angle of incidence to mirror!
    theta_prime = 0.5*(phi_prime + chi_prime)
    theta_prime*=(180/np.pi) # Convert to degrees
    chi_prime*=(180/np.pi) # Convert to degrees
    return (theta_prime, chi_prime) 

# OUTPUT: mirror declinations and sample angles of incidence in DEGREES
def theta_y(A,d,hg,hs):
    psi_prime = np.arctan(A/hg) # Psi prime is y-angle of incidence to mirror!
    upsilon_prime = np.arctan(A/hs)
    omega_prime = 0.5*(psi_prime+upsilon_prime)
    omega_prime*=(180/np.pi)
    upsilon_prime*=(180/np.pi) # Convert to degrees
    return (omega_prime, upsilon_prime)

x_out,y_out = theta_x(X,d,hg,hs), theta_y(Y,d,hg,hs) # Run 'theta_x' and 'theta_y' functions
x_ang,y_ang = np.around(x_out[0],decimals=3),np.around(y_out[0],decimals=3)
x_ang_sort,y_ang_sort = np.sort(x_ang),np.sort(y_ang)
NA_x,NA_y = np.sin(x_out[1]*np.pi/180),np.sin(y_out[1]*np.pi/180) # Convert back to radians and take sine
#print(np.sort(np.around(NA_y,decimals=3)))
print(x_ang_sort,y_ang_sort)
#for i in range(len(x_ang)):
#   print(x_ang[i],y_ang[i])
#    print(NA_x[i],NA_y[i])

# Show mirror array
array=True
if array:
    fig = plt.figure(figsize=[5,5],dpi=100)
    ax1 = fig.add_subplot(111)
    ax1.plot(X,Y,'og')
    ax1.set_xlabel('X position (m)')
    ax1.set_ylabel('Y position (m)')
    ax1.set_title('Mirror Array')
    plt.show()
    plt.close()



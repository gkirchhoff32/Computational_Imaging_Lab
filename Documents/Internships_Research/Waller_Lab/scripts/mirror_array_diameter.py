# Calculate maximum diameter given mirror dimensions
#
# Output: Estimates of number of mirrors for array

import numpy as np
# Calculate mirror coordinates and plot mirror array.
#
# Computational Imaging Lab
# University of California, Berkeley
# Copyright 2019 Grant J. Kirchhoff
# gkirchhoff32@berkeley.edu
#
# Input: mirror diameters, spaces between mirros, number of rings
# Output: mirror positions, plot mirror array

import math
import matplotlib.pyplot as plt
import time

if __name__ == '__main__':
    print('\n','THESE ARE ESTIMATES','\n')

def mirror_array_dims(mr_dia,length_space,num_dia):
    
    ### Calculations for dimensions ###
    if num_dia%2 == 0:
        print('Requires odd number of mirrors on diamter')
    elif num_dia%2 != 0: # Odd number on diameter
        
        num_rad = math.floor(num_dia/2)                # Number in radius of array.
        num_rings = num_rad # Number of rings in array is equal to the number in the radius.
                                           # (Not including center mirror).

        ### IMPORTANT: Circumferences of rings are calculated to midpoints of rings ###
        rings_nums = np.zeros(num_rings)
        rings_circs = np.zeros(num_rings)
        for i in range(num_rings):
            iter_dia = 2*(i+1)*(length_space+mr_dia)+mr_dia # Find diameter of each ring (remember, there's a 'space ring'
                                                     # between rings).
            ### For calculation of 'iter_dia', refer to STARRED page in notebook ###
            iter_circ = np.pi*iter_dia # Find circumference of each ring.
            iter_num_circ = iter_circ/mr_dia # Find number of spaces plus mirrors on the circumference.
            iter_num_mr_circ = math.ceil(iter_num_circ/2) # Find number of mirrors on circumference.
            iter_num_spaces_circ = math.floor(iter_num_circ - iter_num_mr_circ) # Find number of spaces on circumference.
            rings_nums[i] = iter_num_mr_circ
            rings_circs[i] = iter_circ

        total_mrs = np.sum(rings_nums)
        for i in range(len(rings_nums)):
            if __name__ == '__main__':
                print('Ring',i+1,':',int(rings_nums[i]),'mirrors')

        if __name__ == '__main__':
            print('Total mirrors:',total_mrs)

        array_circum = np.pi*iter_dia # Total array circumference
        array_area = np.pi*(iter_dia/2)**2 # Total array area

        if __name__ == '__main__':
            print('\n','Array diameter:',iter_dia*100,'cm','\n',\
              'Array area:',array_area*100*100,'cm^2','\n',\
              'Array circumference:',array_circum*100,'cm')

    ### Display sample mirror array ###
    space_inbetween = np.zeros(num_rings)
    x,y = [],[] # Generate x and y positions of mirrors
    for i in range(len(rings_nums)):
        space_inbetween[i] = rings_circs[i]/(rings_nums[i]) # Divide circumference by number of mirrors to give space inbetween\
                                                            # centers of mirros per ring.
        s = space_inbetween[i]
        r = rings_circs[i]/(2*np.pi)
        theta = s/r
        
        for j in range(int(rings_nums[i])):
            X = r*np.cos(j*theta) # Calculate x positions of mirrors
            Y = r*np.sin(j*theta) # Calculate y positions of mirrors
            x.append(X)
            y.append(Y)

    return x,y

if __name__ == '__main__':
    ### PARAMETERS ###
    mr_dia = 9e-3           # (m) Diameter of each mirror.
    length_space = 4*mr_dia   # (m) Length of space between mirrors. I assume space between mirrors is same dimension.
    #num_dia = 15            # Desired number of mirrors in array diameter (make sure it's ODD).
    dia = 0.5 # Input diameter
    dia_avail = dia - mr_dia # Subtract out middle mirror
    poss_ring_num = np.round(dia_avail/2/(mr_dia+length_space)) # Number of rings to get as close as possible\
                                                          # to input diameter (excluding center mirror)
    num_dia = 2*poss_ring_num+1 # Add one to include center mirror

    x,y = mirror_array_dims(mr_dia,length_space,num_dia)

    fig = plt.figure(figsize=[5,5],dpi=100)
    ax1 = fig.add_subplot(111)
    ax1.plot(x,y,'og')
    ax1.set_xlabel('X position (m)')
    ax1.set_ylabel('Y position (m)')
    ax1.set_title('Mirror Array')
    plt.show()
    plt.close()





























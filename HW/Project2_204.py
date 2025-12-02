#Author: Shishir Tumma
#Assignment: AAE 204 Project 2 
#Date: 12/1/25

import numpy as np
import math as ma
from sympy import *

#Define functions that I will be using
def calc_diagonal_dist(x, y):
    '''
    Calculate the diagonal distance between two points (x, y)
    
    Parameters
    ----------
    x : float
        The x-coordinate of the point
    y : float
        The y-coordinate of the point
    
    Returns
    -------
    float
        The diagonal distance between the two points
    '''
    return np.sqrt(x**2 + y**2)


if __name__ == '__main__':

    #Degree to radian

    dr = ma.pi/180
    #Intialize applied forces in kN
    F1 = 75
    F2 = 90
    F3 = 60

    alpha = 21.9
    #Intialize all internal forces calculated without angle alpha involved
    
    #Node C
    Fcd = F3/ma.sin(12*dr)
    Fde = F3/ma.sin(12*dr)
    Fbc = -Fcd*ma.cos(12*dr)
    # print(Fcd, Fbc, Fde)

    #Node D
    Fbd = 0

    #Node B
    Fbe = F2/ma.sin(26.54*dr)
    Fab = Fbc - Fbe*ma.cos(26.54*dr)
    # print(Fab, Fbe)

    # Node A
    Fae = F1
    Fga = Fab
    # print(Fae, Fga)

    #Node E
    Feh, Fge = symbols("Feh Fge", real = True)

    Fx_E = Eq(Fde*ma.cos(12*dr) + Fbe*ma.cos(26.54*dr) - Feh*ma.cos(12*dr) - Fge *ma.cos(alpha), 0) 
    Fy_E = Eq(Fae+Fde*ma.sin(12*dr) + Fbe*ma.sin(25.64*dr) - Feh*ma.sin(12*dr) + Fge*ma.sin(alpha), 0)

    solution = solve([Fx_E, Fy_E], [Feh, Fge])
    print(solution)
    L_total = 18
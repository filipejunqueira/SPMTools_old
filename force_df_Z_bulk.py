'''
This reads a csv file with ON and OFF spectroscopy.
For each entry it reads the files and
0) Reads on the first line f0 and K. If it does not find it uses the default f = 25000 and K = 1000
1) Determines if ON and OFF are the same Z size.
2) If they are NOT it proceeds to calculate the new Z and new df of the OFF curve by aproximating the OFF curve by a fitting curve
3) Calculates the curve difference and saves it into a dataframe with name Z_# and df_#. # being the number of the ON CURVE!
4) If they are the same size it just takes the difference.
5) Calculates the forces curve using Sader-Jarvis method.
6) Saves the graph for each ON curve along with the global maxima, global minima, local maximas e local minimas (if more than one).
7) Saves a pdf with all the graphs and global maxima and global minima.
'''


import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import datetime
import time
import glob
from scipy.optimize import curve_fit
import cmath

def read_firstline(filename):
    f = open(filename)
    lines = f.readlines()
    return lines[0]


#curve_table_cvs=input()
curve_table_cvs ="spec_table.cvs"

# 0) Reads on the first line f0 and K. If it does not find it uses the default f = 25000 and K = 1000
read_firstline(curve_table_cvs)




df = pd.read_csv(full_path, header=None, names=[variable, "Energy", "Time", "Memory"])

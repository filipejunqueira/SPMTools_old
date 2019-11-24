# I only do tests here
import numpy as np
import matplotlib.pyplot as plt
from spmFunctions import get_one_line, get_path_gui

file_path = get_path_gui()
data = np.genfromtxt(file_path,skip_header=3)



# Script for opening .txt and saving traces exported from Gwideon.
import numpy as np
import matplotlib.pyplot as plt
from spmFunctions import get_one_line, get_path_gui


# First step is to locate file. One method is to manually select the spectroscopy txt .file.
# To do this one must use the following code:

file_path = get_path_gui()
trace = np.loadtxt(file_path, skiprows=3)
units = get_one_line(file_path, 3).decode("utf-8").strip().split("    ")

plt.plot(trace[:, 0], trace[:, 1], "#fd9696")
plt.ylabel(units[1])
plt.xlabel(units[0])
plt.show()

# Script for opening .txt and saving traces exported from Gwideon.
import numpy as np
import matplotlib.pyplot as plt
from subprocess import check_output

# First step is to locate file. One method is to manually select the spectroscopy txt .file.
# To do this one must use the following code:
import tkinter as tk
from tkinter.filedialog import askopenfilename

root = tk.Tk()
root.withdraw()  # prevents the default window  to open.
file_path = (
    askopenfilename()
)  # show an "Open" dialog box and return the path to the selected file

trace = np.loadtxt(file_path, skiprows=3)

def get_one_line(filepath, line_number):
    return check_output(["sed", "-n", "%sp" % line_number, filepath])

units = get_one_line(file_path, 3).decode("utf-8").strip().split("    ")

plt.plot(trace[:,0],trace[:,1])

plt.show()
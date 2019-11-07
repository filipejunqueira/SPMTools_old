# Script for opening .txt and saving traces exported from Gwideon.
import numpy as np
import matplotlib.pyplot as plt

# First step is to locate file. One method is to manually select the spectroscopy txt .file.
# To do this one must use the following code:
import tkinter as tk
from tkinter.filedialog import askopenfilename

root = tk.Tk()
root.withdraw()  # prevents the default window  to open.
file_path = (
    askopenfilename()
)  # show an "Open" dialog box and return the path to the selected file

data = np.loadtxt(file_path)



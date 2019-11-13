# Script for opening .txt and saving spec files exported from vernisage.
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

# Second method is to just add the address to file_path variable.
# file_path = "D:/LTData/2019-07-11/specs/default_2019Jul11-160426_AFM_NonContact_QPlus-AFM_NonContact_QPlus_AtomManipulation--204_1-Df(Z)_1.txt"
data = np.loadtxt(file_path)

# grab spec position:

stringToMatch = "# Sample position                 "
spec_position = ""

# get line
with open(file_path, "r") as file:
    for line in file:
        if stringToMatch in line:
            spec_position = line
            break

spec_position = spec_position.strip().split("# Sample position                 ")[1]

# size of my data, might need to set this manually to 1024 if the retrace data is incomplete
data_size = len(data) // 2

# spits original data into forward data and backwards data
data_forward = data[:data_size]
data_retrace = data[data_size:]

# data_forward_smooth = savgol_filter(data_forward[:, 1], 51, 3)


# Plotting the graph! '#06D6A0 and #FFD166 are hex color codes'
# Plotting scale is done in nm so it is divided by 10-9
# Plot title comes from the end of the string file_path (it looks for the --). Will only work for files generated
# from matrix 4.0 onwards.

temp_title = file_path.split("--")
plot_title = temp_title[1].replace(".txt", "")
fig = plt.figure()
plt.plot(data_forward[:, 0] / 10 ** (-9), data_forward[:, 1], "#06D6A0")
plt.plot(data_retrace[:, 0] / 10 ** (-9), data_retrace[:, 1], "#FFD166")
plt.ylabel("Frequency shift | df(Z)[Hz]")
plt.title(plot_title)
plt.xlabel("Z[nm]")

# setting up x ticks and y ticks - This is important so the last and first ticks are visible
xticks_array = np.around(
    np.linspace(
        min(data_forward[:, 0] / 10 ** (-9)),
        max(data_forward[:, 0] / 10 ** (-9)),
        num=5,
    ),
    2,
)

y_max = max(np.append(data_forward[:, 1], data_retrace[:, 1]))
y_min = min(np.append(data_forward[:, 1], data_retrace[:, 1]))

yticks_array = np.around(np.linspace(y_min, y_max, num=5), 3)
plt.xticks(xticks_array)
plt.yticks(yticks_array)

# Text showing the positions of the spec. It just copy that from the positions from the .txt
# It puts this text in the lower right coner of the the figure.

textposx = (
    min(data_forward[:, 0] / 10 ** (-9)) + max(data_forward[:, 0] / 10 ** (-9))
) / 2
textposy = (y_max + y_min) / 2

plt.text(
    textposx * (1.1),
    textposy * (1.5),
    "Spec pos: " + spec_position,
    fontsize=7,
    family="serif",
)

# TODO need to make the code to be not folder specific here.

plt.savefig(
    "D:/LTData/2019-07-11/specs/" + plot_title + ".png",
    bbox_inches="tight",
    transparent=True,
)
plt.show()

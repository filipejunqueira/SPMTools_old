# Script for opening .txt and saving traces exported from Gwideon.
import numpy as np
import matplotlib.pyplot as plt
from spmFunctions import get_one_line, get_path_gui


# First step is to locate file. One method is to manually select the spectroscopy txt .file.
# To do this one must use the following code:
# Depending how it is exported from gwideon;

file_path = get_path_gui()
trace = np.genfromtxt(file_path, skip_header=3)
units = get_one_line(file_path, 3).decode("utf-8").strip().split("    ")
legend = get_one_line(file_path,1).decode("utf-8").strip().split("             ")
number_traces = int(len(trace[0, :]) / 2)

plot_title = file_path.split("/traces/")[1].strip(".txt")
colours = ["#FF6B6C", "#DD6E42", "#FFC145", "#56E39F", "#5B6C5D"]

plt.title(plot_title)

index = 0
while index < number_traces:
    plt.plot(trace[:, 2 * index], trace[:, 2 * index + 1], colours[index], label=legend[index])
    index += 1

plt.ylabel(units[1])
plt.xlabel(units[0])
plt.legend()

# Todo make this not path depedent?

plt.savefig("D:/LTData/2019-07-11/traces/" + plot_title + ".png", bbox_inches="tight")

plt.show()

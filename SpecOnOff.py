# Script for opening .txt and saving spec files exported from vernisage.
import numpy as np
import matplotlib.pyplot as plt
from spmFunctions import load_spec, get_path_gui

print("Select the ON curve")
data_on_path = get_path_gui()
print("Select the OFF curve")
data_off_path = get_path_gui()

data_on_tuple = load_spec(data_on_path)
data_off_tuple = load_spec(data_off_path)

# TODO rewrite this so it only uses the object now. Makes it simpler to read.
data_forward_diff = np.asarray(
    [x - y for x, y in zip(data_on_tuple[0][:, 1], data_off_tuple[0][:, 1])]
)
data_retrace_diff = np.asarray(
    [x - y for x, y in zip(data_on_tuple[1][:, 1], data_off_tuple[1][:, 1])]
)

#TODO add the tick positions in this graph as I did in loadspecsript.py.

plot_title_on = data_on_path.split("--")[1].replace(".txt", "")
plot_title_off = data_off_path.split("--")[1].replace(".txt", "")
plot_title = f"Df difference = {plot_title_on} (ON) - {plot_title_off} (OFF)"
plt.plot(data_on_tuple[0][:, 0], data_forward_diff, "#2A9D8F")
plt.plot(data_on_tuple[1][:, 0], data_retrace_diff, "#E9C46A")
plt.title(plot_title)
plt.xlabel("Z[nm]")
plt.ylabel("Df[Hz]")

plt.savefig("D:/LTData/2019-07-11/specs/" + plot_title + ".png",bbox_inches="tight",)
plt.show()

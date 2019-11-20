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

data_forward_diff = np.asarray(
    [x - y for x, y in zip(data_on_tuple[0][:, 1], data_off_tuple[0][:, 1])]
)
data_retrace_diff = np.asarray(
    [x - y for x, y in zip(data_on_tuple[1][:, 1], data_off_tuple[1][:, 1])]
)

plt.plot(data_on_tuple[0][:, 0], data_forward_diff, "#163A37")
plt.plot(data_on_tuple[1][:, 0], data_retrace_diff, "#E3B23C")
plt.show()

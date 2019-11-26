# Script for opening .txt and saving spec files exported from vernisage.
import numpy as np
import matplotlib.pyplot as plt
from spmFunctions import get_path_gui


file_path = get_path_gui()
root_path = file_path.split("/specs/")[0]
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
# fig = plt.figure()
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

plt.savefig(
    f"{root_path}/specs/{plot_title}.png", bbox_inches="tight", transparent=True,
)
plt.show()

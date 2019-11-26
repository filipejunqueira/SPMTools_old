import numpy as np
from spmFunctions import import_matrix_file, get_path_gui
import matplotlib.pyplot as plt

file_path = get_path_gui()
root_path = file_path.split("/default")


# TODO include input somehow in the function calling. Need to think about the use cases.

print("Type 0: up forward, 1: up retrace, 2: down forward, 3: down retrace")
file_index = int(input())
image, image_raw = import_matrix_file(file_index, file_path)

# Averaging image per row
mean_array = np.mean(image, axis=1, dtype=np.float64)

# Getting image size (number of points) and image height

image_height = image_raw.height
image_size = image.shape[0]

# Creating an axis to plot the average value of Df
x_axis = np.arange(start=0.0, stop=image_height, step=image_height / image_size)
# in case you need to slice x,y to show in graph
#x_axis = x_axis[:300]
#mean_array = mean_array[:300]
temp_title = file_path.split("--")
plot_title = temp_title[1].replace("_mtrx", "")

# TODO could make this labels tecnicly file specific (like read the file_path and determine if its Z(mn) Df(Z) etc....)

plt.plot(x_axis / 10 ** (-9), mean_array, "#6699CC")
plt.ylabel("Frequency shift | df [Hz]")
plt.title(f"{plot_title} Line average_{file_index}")
plt.xlabel("Z[nm]")

plt.savefig(f"{root_path[0]}/traces/{plot_title}_{file_index}_Line_average.png",
    bbox_inches="tight",
    transparent=True,
)

plt.show()

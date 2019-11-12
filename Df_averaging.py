import numpy as np
from ImportMatrixFile import import_matrix_file
import tkinter as tk
from tkinter.filedialog import askopenfilename
import matplotlib as plt

root = tk.Tk()
root.withdraw()  # prevents the default window  to open.
file_path = (
    askopenfilename()
)  # show an "Open" dialog box and return the path to the selected file

image, image_raw = import_matrix_file(1, file_path)

# Averaging image per row
mean_array = np.mean(image, axis=1, dtype=np.float64)


fig = plt.figure()
temp_title = file_path.split("--")
plot_title = temp_title[1].replace(".txt", "")
plt.plot(mean_array)
plt.show()
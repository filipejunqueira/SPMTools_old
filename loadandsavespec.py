import matplotlib.pyplot as plt
from spmFunctions import get_one_line, get_path_gui, plot_spec

file_path = get_path_gui()
plot_spec(file_path)
plt.show()
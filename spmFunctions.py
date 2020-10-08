import access2thematrix
import numpy as np
from subprocess import check_output
import tkinter as tk
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
from pathlib import Path

# Function that imports matrix file
def import_matrix_file(series_number, file_path):

    mtrx_data = access2thematrix.MtrxData()
    traces, message = mtrx_data.open(file_path)
    im, _ = mtrx_data.select_image(traces[series_number])
    image = im.data

    # dict = {0: "up forward", 1: "up retrace", 2: "down forward", 3: "down retrace"}
    # print("Image has been uploaded to variables image and im")

    return image, im


# Function that loads a spec file (exported from Vernisage in .txt)


def load_spec(file_path):

    data = np.loadtxt(file_path)

    # grab spec position:

    stringToMatch = "# Sample position                 "
    position_temp = " "

    # get line
    with open(file_path, "r") as file:
        for line in file:
            if stringToMatch in line:
                position_temp = line
                break

    position_temp = position_temp.strip().split("# Sample position                 ")[1]
    position_temp = position_temp.strip("[nm]").split(",")
    spec_position = np.asfarray(position_temp, dtype="float64")

    # size of my data, might need to set this manually to 1024 if the retrace data is incomplete
    data_size = len(data) // 2

    # spits original data into forward data and backwards data
    data_forward = data[:data_size]
    data_retrace = data[data_size:]

    class Spec:
        def __init__(self, forward, retrace, size, position):
            self.forward = forward
            self.retrace = retrace
            self.size = size
            self.position = position

    spec_object = Spec(data_forward, data_retrace, data_size, spec_position)
    return data_forward, data_retrace, data_size, spec_position, data, spec_object


# grabs one specific line of a .txt file
# I copied this from stackoverflow, I have no idea what check_output really does... But it works! :-)
def get_one_line(filepath, line_number):
    return check_output(["sed", "-n", "%sp" % line_number, filepath])

# Todo - add initialdir=initialdirectory atribute ti get_path_gui

def get_path_gui():
    root = tk.Tk()
    root.withdraw()  # prevents the default window  to open.
    root.attributes(
        "-topmost", True
    )  # makes the window go on top of other applications
    file_path = (
        askopenfilename()
    )  # show an "Open" dialog box and return the path to the selected file, function path makes / -> \ for windows
    return file_path


def plot_spec(file_path):
    spec = load_spec(file_path)[5]
    root_path = file_path.split("/specs/")[0]
    temp_title = file_path.split("--")
    plot_title = temp_title[1].replace(".txt", "")
    fig = plt.figure()
    plt.plot(spec.forward[:, 0] / 10 ** (-9), spec.forward[:, 1], "#06D6A0")
    plt.plot(spec.retrace[:, 0] / 10 ** (-9), spec.retrace[:, 1], "#FFD166")
    plt.ylabel("Frequency shift | df(Z)[Hz]")
]    plt.title(plot_title)
    plt.xlabel("Z[nm]")

    # setting up x ticks and y ticks - This is important so the last and first ticks are visible
    xticks_array = np.around(
        np.linspace(
            min(spec.forward[:, 0] / 10 ** (-9)),
            max(spec.forward[:, 0] / 10 ** (-9)),
            num=5,
        ),
        2,
    )

    y_max = max(np.append(spec.forward[:, 1], spec.retrace[:, 1]))
    y_min = min(np.append(spec.forward[:, 1], spec.retrace[:, 1]))

    yticks_array = np.around(np.linspace(y_min, y_max, num=5), 3)
    plt.xticks(xticks_array)
    plt.yticks(yticks_array)

    # Text showing the positions of the spec. It just copy that from the positions from the .txt
    # It puts this text in the lower right coner of the the figure.

    textposx = (
        min(spec.forward[:, 0] / 10 ** (-9)) + max(spec.forward[:, 0] / 10 ** (-9))
    ) / 2
    textposy = (y_max + y_min) / 2

    plt.text(
        textposx * (1.1),
        textposy * (1.5),
        f"Spec pos: {spec.position}",
        fontsize=7,
        family="serif",
    )

    plt.savefig(
        f"{root_path}/specs/{plot_title}.png", bbox_inches="tight", transparent=True,
    )
    return True

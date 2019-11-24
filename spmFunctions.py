import access2thematrix
import numpy as np
from subprocess import check_output
import tkinter as tk
from tkinter.filedialog import askopenfilename

# Function that imports matrix file

def import_matrix_file(series_number, file_path):

    mtrx_data = access2thematrix.MtrxData()
    traces, message = mtrx_data.open(file_path)
    im, _ = mtrx_data.select_image(traces[series_number])
    image = im.data

    # dict = {0: "up forward", 1: "up retrace", 2: "down forward", 3: "down retrace"}
    #print("Image has been uploaded to variables image and im")

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
    spec_position = np.asfarray(position_temp, float)

    # size of my data, might need to set this manually to 1024 if the retrace data is incomplete
    data_size = len(data) // 2

    # spits original data into forward data and backwards data
    data_forward = data[:data_size]
    data_retrace = data[data_size:]

    return data_forward, data_retrace, data_size, spec_position, data


# grabs one specific line of a .txt file
# I copied this from stackoverflow, I have no idea what check_output really does... But it works! :-)
def get_one_line(filepath, line_number):
    return check_output(["sed", "-n", "%sp" % line_number, filepath])


def get_path_gui():
    root = tk.Tk()
    root.withdraw()  # prevents the default window  to open.
    file_path = (
        askopenfilename()
    )  # show an "Open" dialog box and return the path to the selected file
    return file_path

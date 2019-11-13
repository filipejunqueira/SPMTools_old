import numpy as np
import matplotlib.pyplot as plt


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
    spec_position = np.asfarray(position_temp,float)

    # size of my data, might need to set this manually to 1024 if the retrace data is incomplete
    data_size = len(data) // 2

    # spits original data into forward data and backwards data
    data_forward = data[:data_size]
    data_retrace = data[data_size:]

    return data_forward, data_retrace, data_size, spec_position


a = load_spec(
    "D:\\LTData\\2019-07-11\\specs\\default_2019Jul11-160426_AFM_NonContact_QPlus-AFM_NonContact_QPlus_AtomManipulation--308_1-Df(Z)_1.txt"
)

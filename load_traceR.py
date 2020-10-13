import matplotlib.pyplot as plt
import spmFunctions

root_path = "/mnt/bigdrive/LTData/2020-08-03/"
file_path = "20200803-130406_GaAs(110)--AFM_NonContact_QPlus--17_1-Df(Z)_1.txt"
path = f"{root_path}/specs/{file_path}"

#graph = spmFunctions.plot_trace_Zr(path)
graph = spmFunctions.plot_trace_Dfr(path)
import matplotlib.pyplot as plt
import spmFunctions

root_path = "/mnt/bigdrive/LTData/2019-07-11"
file_path = "default_2019Jul11-160426_AFM_NonContact_QPlus-AFM_NonContact_QPlus_AtomManipulation--60_1-Z(r).txt"
path = f"{root_path}/specs/{file_path}"

trace = spmFunctions.load_trace_r(file_path=path)
x = spmFunctions.plot_trace_r(path)

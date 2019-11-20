import matplotlib.pyplot as plt
from spmFunctions import load_spec, import_matrix_file

file_path_spec = "D:\\LTData\\2019-07-11\\specs\\default_2019Jul11-160426_AFM_NonContact_QPlus-AFM_NonContact_QPlus_AtomManipulation--311_1-Df(Z)_1.txt"
file_path_image = "D:\\LTData\\2019-07-11\\default_2019Jul11-160426_AFM_NonContact_QPlus-AFM_NonContact_QPlus_AtomManipulation--17_1.Df_mtrx"

series_id = int(0)
file = load_spec(file_path_spec)

x = file[3][0]
y = file[3][1]

canvas, canvasim = import_matrix_file(series_id, file_path_image)

size = canvasim.height

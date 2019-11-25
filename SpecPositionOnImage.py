import matplotlib.pyplot as plt
from spmFunctions import load_spec, import_matrix_file, get_path_gui
import numpy as np

# Starts with a .txt called in a folder.
# Atributes order - #file_number,spec type (Df(Z),I(Z)),spec_files_number(234_1, 235_1, 233_1, 123 etc)
# Creates a canvas based on the height of image number. Asks in terminal
# if you want to get another image (like a .png).

# root_paths must be edited for each folder you are working on
root_image_path = "D:\\LTData\\2019-07-11\\default_2019Jul11-160426_AFM_NonContact_QPlus-AFM_NonContact_QPlus_AtomManipulation--"
root_specs_path = "D:\\LTData\\2019-07-11\\specs\\default_2019Jul11-160426_AFM_NonContact_QPlus-AFM_NonContact_QPlus_AtomManipulation--"
f = open(get_path_gui(),'r')
txt_input = (f.read()).split(" ")

# If looking at other images then Z you must change image_path string variable
image_path = f"{root_image_path}{txt_input[0]}.Z_mtrx"
specs_path_index = txt_input[2:]
specs_path =[]
for item in specs_path_index:
    specs_path.append(f"{root_specs_path}--{item}-{txt_input[1]}_1")

# Retreive size of image from image_path - and check if must keep it
print("Getting information from the image of spec - height and data.\n")
print("Select which image you want")
print("Type 0: up forward, 1: up retrace, 2: down forward, 3: down retrace")
file_index = int(input())
image, image_raw = import_matrix_file(file_index, image_path)
image_height = image_raw.height
image_size = image.shape[0]

# Now need to storage the positions for each specs




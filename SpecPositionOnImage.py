import matplotlib.pyplot as plt
from spmFunctions import load_spec, import_matrix_file, get_path_gui
import numpy as np

# -----------------------------------------------------------------------------------------
# Starts with a .txt called in a folder.
# Atributes order - #file_number,spec type (Df(Z),I(Z)),spec_files_number(234_1, 235_1, 233_1, 123 etc)
# Creates a canvas based on the height of image number. Asks in terminal
# if you want to get another image (like a .png).

# root_paths must be edited for each folder you are working on
root_image_path = "D:\\LTData\\2019-07-11\\default_2019Jul11-160426_AFM_NonContact_QPlus-AFM_NonContact_QPlus_AtomManipulation--"
root_specs_path = "D:\\LTData\\2019-07-11\\specs\\default_2019Jul11-160426_AFM_NonContact_QPlus-AFM_NonContact_QPlus_AtomManipulation--"
print("Select the input file")
f = open(get_path_gui(), "r")
txt_input = (f.read()).split(" ")

# If looking at other images then Z you must change image_path string variable
image_path = f"{root_image_path}{txt_input[0]}.Z_mtrx"

specs_list = txt_input[2:]
specs_path = []
for item in specs_list:
    specs_path.append(f"{root_specs_path}{item}-{txt_input[1]}_1.txt")

# Retreive size of image from image_path - and check if must keep it
print("Getting information from the image of spec - height and data.\n")
print("Select which image you want")
print("Type 0: up forward, 1: up retrace, 2: down forward, 3: down retrace")
file_index = int(input())
image, image_raw = import_matrix_file(file_index, image_path)
image_height = image_raw.height
image_size = image.shape[0]


# Getting the correct image height
# If you change the image size during scanning it only stores the last value! :-(

print(
    f"The image_height is {image_height*(10**9)} nm, is that correct? \n If yes press y if no n:"
)
loop_flag = True
while loop_flag == True:

    height_check = input()
    if height_check in ("y", "Y", "yes", "YES", "yes"):
        loop_flag = False
        break

    elif height_check in ("n", "N", "NO", "No", "no"):
        print("Insert the correct height in nm:\n")
        image_height = np.float64(input()) / (10 ** 9)
        loop_flag = False
    else:
        print("Try again")
        break
print(f"ok! Height is {image_height*(10**9)} nm")


spec_pos = []  # Need to storage the positions for each specs
for item in specs_path:
    spec_pos.append(load_spec(item)[5].position)

# Now need to add flat image - a png in the image folder. Image **should** be without lateral scales!
# TODO add spiepy option for flatting!

print("Select an image two plot the points")
image_gwideon_path = get_path_gui()

im = plt.imread(image_gwideon_path)
fig, ax = plt.subplots()
ax.imshow(im, extent=[0, image_height * (10 ** 9), 0, image_height * (10 ** 9)])

color_palette = ["#FFFF00", "#FFFF33", "#FFFF66", "#FFFF99", "#FFFFCC"]

index = int(0)
offset = (image_height * (10 ** 9)) / 2

while index < len(spec_pos):
    plt.scatter(
        offset + spec_pos[index][0],
        offset + spec_pos[index][1],
        c=color_palette[index % 5],
        s=10,
    )
    plt.annotate(
        specs_list[index],
        xy=(offset + spec_pos[index][0], offset + spec_pos[index][1]),
        xytext=(
            image_height * (10 ** 9) * 0.92,
            image_height * (10 ** 9) * (0.40 - index / 20),
        ),
        arrowprops=dict(
            facecolor="#ffc000",
            shrink=0.02,
            edgecolor="#ffc000",
            width=0.6,
            headwidth=4,
            headlength=4,
            # arrowstyle="->",
        ),
        c=color_palette[index % 5],
        weight="heavy",
        va="center",
        ha="right",
    )
    index += 1

# put a red dot, size 40, at 2 locations:
# plt.scatter(x=[30, 70], y=[20, 90], c="r", s=80)

plt.xlabel("Z[nm]")
plt.title(f"Image {txt_input[0]} with spec position")
plt.savefig(f"D:/LTData/2019-07-11/specs/{txt_input[0]}Z_with_{txt_input[1]}_specs.png")
plt.show()

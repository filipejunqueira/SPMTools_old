import access2thematrix
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter.filedialog import askopenfilename


# Load data
mtrx_data = access2thematrix.MtrxData()
data_file = r"D:\LTData\2019-07-11\default_2019Jul11-160426_AFM_NonContact_QPlus-AFM_NonContact_QPlus_AtomManipulation--63_1.Df_mtrx"
traces, message = mtrx_data.open(data_file)
im, _ = mtrx_data.select_image(traces[1])
image = im.data

# Plot images
plt.imshow(image)

# Take max, min of each line
im_max = np.max(image, axis=1)
im_min = np.min(image, axis=1)
im_diff = im_max - im_min

# Split im_diff to get data we actually give a toss about
im_diff_filtered = im_diff[im_diff <= 2e-9]

# Make histrogram
plt.hist(im_diff_filtered, bins=40)
plt.xlabel("Height Difference.")
plt.ylabel("Num.")
plt.show()

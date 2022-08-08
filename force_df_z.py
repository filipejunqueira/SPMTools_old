from numpy import arange
from pandas import read_csv
from scipy.optimize import curve_fit
from matplotlib import pyplot
import glob
import os
import math

def objective(x, a, b, c, d):
    return a * x ** (-6) + b * x ** (-12) + c * x ** -1 + d*x**0

def read_spec(full_path):
    df = pd.read_csv(full_path, header=None, names=["Z", "df"])
    return df

def extremes_z(file):
    #should spit out a numpy array which is 2x1 in size.
    pass

def smooth(array):
    #should smooth out with some method to remove the noise
    pass

def local_max():
    pass

def local_min():
    pass


#Loading curves.

cwd = os.getcwd()
files = glob.glob(f"{cwd}/*.cvs")
path_off = ""
path_on = ""

spec_on = read_spec(path_on)
spec_off = read_spec(path_off)
extreme_ON = extremes_z(spec_on["Z"])
extreme_OFF = extremes_z(spec_off["Z"])
# Merge spec on and spec off

if extreme_ON != extreme_OFF:
    print(f"I was not able to do a full 1 x 1 comparisson. Spec ON Z range is {extreme_ON} and Spec OFF is {extreme_OFF}")
    #replacing it OFF with function to match ON.
    popt, pcov = curve_fit(objective, path_off["Z"], path_off["df"])
    a, b, c, d = popt
    x_line = path_on["Z"]
    y_line = objective(x_line, a, b, c, d)
    delta_df = spec_on["df"] - y_line # this should subtract the on from the background.
    delta_df_smooth = smooth(spec_on["df"]) - y_line
else:
    print(f"1x1 Comparisson is possible. Z range is the same")
    delta_df = spec_on["df"] - spec_off["df"] # this should subtract the on from the background.
    delta_df_smooth = smooth(spec_on["df"]) - smooth(spec_off["df"])


#Calculating forces.
k = 1000 #spring constant
f = 20000 #resonance frequency

#Finding all local maxima and all local minimima.
maxima = local_max()
minima = local_min()
global_max = max(maxima)
global_minima = min(minima)

#Plotting curve
fig = plt.figure()
ax = fig.add_subplot(111)

# create a line plot for the mapping function
cmap = sns.light_palette("#77DD77", as_cmap=True)

sns.lineplot(delta_df, y=y_line, marker=True, color='#ff6969')
sns.scatterplot(data=df, x=f"", y="Energy", hue="Time",
                palette=sns.color_palette("dark:#77DD77", as_cmap=True), ax=ax)

# Set title
ax.title.set_text(f'Force vs Z')
# Set x-axis label
plt.xlabel(f'Z(nm)')
# Set y-axis label
plt.ylabel('Force (pN)')
#ax.text(1, e_min * 0.95, f'Emin= {round(e_min, 5)} [eV]', horizontalalignment='left', size='small', color='gray',
        weight='semibold')
# Set text with total price
# ax.text(0,0,f'Total cost = £{round(total_price,2)}', horizontalalignment='left', size='small', color='gray', weight='semibold')
plt.savefig(f'{variable}Force_curve.eps', format='eps', dpi=300)
plt.show()


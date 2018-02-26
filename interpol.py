# interpol.py
#
# Written by Matthew Stevenson
#
# Program to approximate input data and plot approximating functions
# for CS517
#
# Any questions please email: mstev019@odu.edu
#

from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np

# initialization of variables
scale_x = 0
scale_data = 0
x = []
yb = []
yf = []

# parse input file for x scale and y scale
file = open("afm.data", "r")
for line in file:
    line = line.strip()
    columns = line.split()
    if (unicode(columns[0], 'utf-8') == 'Scale') & (unicode(columns[1], 'utf-8') == 'X'):
        scale_x = float(columns[3])
    if (unicode(columns[0], 'utf-8') == 'Scale') & (unicode(columns[1], 'utf-8') == 'Data'):
        scale_data = float(columns[3])

# parse for input data for x, yb, and yf
with open("afm.data", "r") as file:
    for i in xrange(18):
        file.next()
    for line in file:
        data_col = line.split()
        x.append((float(data_col[0])*scale_x)/1000)
        yb.append((float(data_col[1])*scale_data)/1000)
        yf.append((float(data_col[2])*scale_data)/1000)
        #print ((float(data_col[0])*scale_x)/1000, (float(data_col[1])*scale_data)/1000, (float(data_col[2])*scale_data)/1000)
file.close()

# print values to console
print("Scale X: ", scale_x, "Scale Data: ", scale_data)
print("X:", x)
print("YB:", yb)
print("YF:", yf)

# edit yb below if you would like to use yf y values
adj_close = np.array(yb)
adj_piece = adj_close[:]
end = np.shape(adj_close)[0]
adj_x = np.linspace(0, end, end, endpoint=True)
inter_cub = interp1d(adj_x, adj_close, kind='cubic')
plt.figure()
plt.plot(x, adj_piece, 'ro', label='data')
plt.plot(x, inter_cub(adj_x), label='approximation')
plt.title("CS517 - Approximation of Input Data")
plt.legend()
plt.grid()
plt.show()

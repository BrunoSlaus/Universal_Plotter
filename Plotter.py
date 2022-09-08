import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
######################################################
Array_Name = 'Histogram_Data_Final.fits'
Colors     = ['black', 'blue', 'red']
Styles     = ['-', '--', '-.']

x_min      = 10
x_max      = 24
y_min      = -10
y_max      = 500

######################################################

Array   = fits.open(Array_Name)[1].data
Columns = fits.open(Array_Name)[1].columns

N_Columns = len(Columns.names)

x_Plot = Array.field(0)
print('Plotting column ',0 ,'.')

fig = plt.figure()
ax = fig.add_axes([0.15,0.15,0.8,0.75])
for i in range(1, N_Columns):
    print('Plotting column ',i ,'.')
    y_Plot = Array.field(i)
    plt.step(x_Plot, y_Plot, where='post', color=Colors[i-1], linestyle=Styles[i-1], label=Columns.names[i])
    #plt.text(0.60, 0.95-0.05*i, Colors[i-1] + ' = ' + Columns.names[i], transform=ax.transAxes, fontsize=15)
plt.xlabel('z_DECam_magnitude', fontsize=15)
plt.ylabel('N', fontsize=15)    
plt.title('Final Distribution', fontsize=15)
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.legend(loc='upper left', bbox_to_anchor=(0.01, 0.99), fontsize=13)
plt.axhline(0, color='black')
plt.savefig('Magnitude_Distribution_'+ Array_Name +'.png', dpi = 300)
plt.close()










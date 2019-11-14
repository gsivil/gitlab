# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:23:16 2019

@author: DELL
"""
#Error bars
#Aspect ratio equal for camera images
#Colorbar
#Scale if needed
#Angle view
#Lightning and shading
#Give example for 2D surface plot
#Give example for 2D surface plot at an angle
#Give example for 3D isosurface plot
#
import matplotlib.pyplot as plt
import numpy as np
#plt.plot([1, 2, 3, 4],'r.')


font = {'family' : 'helvetica',
        'weight' : 'normal',
        'size'   : 22}

plt.rc('font', **font)

axeswidth = 2.5
plt.rc('axes', linewidth=axeswidth)

ticksizemajor = 4
tickwidthmajor = axeswidth

ticksizeminor = 4
tickwidthminor = axeswidth

plt.rcParams['xtick.major.size'] = ticksizemajor
plt.rcParams['xtick.major.width'] = tickwidthmajor
plt.rcParams['xtick.minor.size'] = ticksizeminor
plt.rcParams['xtick.minor.width'] = tickwidthmajor

plt.rcParams['ytick.major.size'] = ticksizemajor
plt.rcParams['ytick.major.width'] = tickwidthmajor
plt.rcParams['ytick.minor.size'] = ticksizeminor
plt.rcParams['ytick.minor.width'] = tickwidthminor

plt. rcParams.update({'figure.autolayout': True})


# libraries

# create data
#x  = np.exp()
xpoints = 201
ypoints = 201
x = np.linspace(-12,12,xpoints)
y = np.linspace(-12,12,ypoints)

 
xi, yi = np.mgrid[x.min():x.max():1j*xpoints, y.min():y.max():1j*ypoints]

waist = 5
zi = np.exp(-(xi**2+yi**2)/waist**2)
 
# Make the plot

plt.pcolormesh(xi, yi, zi, cmap= plt.cm.jet)

plt.xlabel(r'X position ($\mu m$)')
plt.ylabel(r'Y position ($\mu m$)')


cbar = plt.colorbar(ticks=[0, 0.5, 1.0])
cbar.ax.set_yticklabels(['0', '0.5','1'])  # vertically oriented colorbar

plt.axes().set_aspect('equal')

plt.text(-11, 9, r'(iv)', weight = 'normal', size = 24, color = 'w')
#plt.axis([40, 160, 0, 0.03])

fname = "PaperFigureMultiplotsurface_lowrestest.tiff" 
plt.savefig(fname, dpi=300, figsize= (6.4, 4.8), facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format='tiff',
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None, metadata=None)
plt.show()



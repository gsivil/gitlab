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
#from mpl_toolkits.mplot3d import axes3d

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LightSource

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

# create data

xpoints = 251; ypoints = 251
x = np.linspace(-12,12,xpoints); y = np.linspace(-12,12,ypoints)
fig = plt.figure(figsize=(6.4,6.4*4.8/6.4))
ax = fig.add_subplot(111, projection='3d')
xi, yi = np.mgrid[x.min():x.max():1j*xpoints, y.min():y.max():1j*ypoints]
waist1 = 4; waist2 = 2
zi = np.exp(-(xi**2+yi**2)/waist1**2)+0.5*np.exp(-((xi-4)**2+(yi-4)**2)/waist2**2)
 # Make the plot
rgb = np.ones((zi.shape[0], zi.shape[1], 3))
ls = LightSource(azdeg=120, altdeg=50)
red = np.array([1.0,0.00,0.00])
red_surface = ls.shade_rgb(rgb * red, zi, vert_exag=0.01)
surf1 = ax.plot_surface(xi, yi, zi, rstride=1, cstride=1, linewidth=0,
                antialiased=False, facecolors = red_surface, alpha =1.0, shade = True)
ax.set_xlabel(r'X ($\mu m$)',labelpad=15)
ax.set_ylabel(r'Y ($\mu m$)',labelpad=15)
ax.set_zlabel(r'Intensity ($W/m^2$)',labelpad=12, rotation=0)
altitude, azimuth = (30, 120)
ax.view_init(altitude, azimuth)
ax.set_xlim(np.array([-11,11]))
ax.set_ylim(np.array([-11,11]))
ax.set_zlim(np.array([0,1.0]))
ax.grid(False)
ax.set_axis_off()
#plt.tight_layout()

fname = "PaperFigureMultiplotsurface_Rgb_RGtest.tiff" 
plt.savefig(fname, dpi=600, figsize= (6.4, 4.8), facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format='tiff',
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None, metadata=None)
plt.show()



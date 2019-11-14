# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:23:16 2019

@author: DELL
"""
#Data points
#Lines
#Add two or three plots
#Legends
#Figure caption
#Figure title
#Ticks
#Size
#Font
#Format
#Resolution
#Vector graphics
#Axes thickness
#Linewidths
#Markers
#Can we make a template
#Error bars
#Give example for 2D surface plot
#Give example for 3D isosurface plot

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


x = np.linspace(0,10,11)

y1data = x
y1fitting = x
y2data = 1.25*x+1
y2fitting = 1.25*x+1
y3data = 1.5*x+2
y3fitting = 1.5*x+2

myfigure = plt.figure()

plot1data = plt.plot(x,y1data)
plot1theory = plt.plot(x,y1fitting)

plt.setp(plot1data, color='blue',marker = 'o', markersize=10,  fillstyle='full'
         , markeredgewidth=2, label =  'tall data', linestyle= '')
plt.setp(plot1theory, color='blue',  linewidth = 2.5, label=None)

plot2data = plt.plot(x,y2data)
plot2theory = plt.plot(x,y2fitting)

#plt.plot(x,y2data,'black', marker='o', markersize=10,  fillstyle='none', markeredgewidth=2, label =  'data')
#plt.plot(x,y2fitting,'black', linewidth = 2.5, label='simulation')

plt.setp(plot2data, color='blue',marker = 'd', markersize=10,  fillstyle='none'
         , markeredgewidth=2, label =  'grande data', linestyle= '')
plt.setp(plot2theory, color='blue',  linewidth = 2.5, label=None)

plot3data = plt.plot(x,y3data)
plot3theory = plt.plot(x,y3fitting)

plt.setp(plot3data, color='blue',marker = 'o', markersize=10,  fillstyle='none'
         , markeredgewidth=2, label =  'venti data', linestyle= '')
plt.setp(plot3theory, color='blue',  linewidth = 2.5, label=None)

plt.ylabel(r'Temperature ($^\degree C$)')
plt.xlabel(r'Time ($\mu s$)')
plt.text(0, 14, r'(ii)', weight = 'normal', size = 24)
plt.grid(False)
plt.legend()
plt.legend(loc='lower right', prop={'size': 12}, frameon = False)




fname = "PaperFigureMultiplot.tiff" 
plt.savefig(fname, dpi=600, figsize= (6.4, 4.8), facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format='tiff',
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None, metadata=None)

plt.xticks(np.arange(0, 10.1, 2)) 
plt.yticks(np.arange(0, 15.1, 5)) 

#plt.tight_layout()

plt.show()

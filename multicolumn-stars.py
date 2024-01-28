# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 08:30:39 2024

@author: JMCasado
"""

#General import
import os
import argparse
import glob
import numpy as np
import datetime
import matplotlib.pyplot as plt
import math
import pandas as pd

#Local import
from data_transform import smooth
from data_export.data_export import DataExport
from data_import.data_import import DataImport
from sound_module.simple_sound import simpleSound
from data_transform.predef_math_functions import PredefMathFunctions

# Instanciate the sonoUno clases needed
_dataexport = DataExport(False)
_dataimport = DataImport()
_simplesound = simpleSound()
_math = PredefMathFunctions()
# Sound configurations, predefined at the moment
_simplesound.reproductor.set_continuous()
_simplesound.reproductor.set_waveform('celesta')
_simplesound.reproductor.set_time_base(0.05)
_simplesound.reproductor.set_min_freq(300)
_simplesound.reproductor.set_max_freq(1500)
# The argparse library is used to pass the path and extension where the data
# files are located
parser = argparse.ArgumentParser()
# Receive the extension from the arguments
parser.add_argument("-t", "--file-type", type=str,
                    help="Select file type.",
                    choices=['csv', 'txt'])
# Receive the directory path from the arguments
parser.add_argument("-d1", "--directory1", type=str,
                    help="Indicate a directory to process as batch.")
parser.add_argument("-d2", "--directory2", type=str,
                    help="Indicate a directory to process as batch.")
parser.add_argument("-d3", "--directory3", type=str,
                    help="Indicate a directory to process as batch.")
# Indicate to save or not the plot
parser.add_argument("-p", "--save-plot", type=bool,
                    help="Indicate if you want to save the plot (False as default)",
                    choices=[False,True])
# Alocate the arguments in variables, if extension is empty, select txt as
# default
args = parser.parse_args()
ext = args.file_type or 'txt'
#path = args.directory
path1 = args.directory1
path2 = args.directory2
path3 = args.directory3
plot_flag = args.save_plot or True
# Print a messege if path is not indicated by the user
if not path1:
    print('1At least on intput must be stated.\nUse -h if you need help.')
    exit()
if not path2:
    print('2At least on intput must be stated.\nUse -h if you need help.')
    exit()
if not path3:
    print('3At least on intput must be stated.\nUse -h if you need help.')
    exit()
# Format the extension to use it with glob
extension = '*.' + ext

# Initialize a counter to show a message during each loop
i = 1
if plot_flag:
    # Create an empty figure or plot to save it
    cm = 1/2.54  # centimeters in inches
    #fig = plt.figure(figsize=(15*cm, 10*cm), dpi=300)
    fig = plt.figure()
    # Defining the axes so that we can plot data into it.
    #ax = plt.axes()
#Inits to generalize

# Loop to walk the directory and sonify each data file
now = datetime.datetime.now()
print(now.strftime('%Y-%m-%d_%H-%M-%S'))

#for filename in glob.glob(os.path.join(path, extension)):
print("Converting data file number "+str(i)+" to sound.")
# Open each file
data1, status, msg = _dataimport.set_arrayfromfile(path1, ext)
data2, status, msg = _dataimport.set_arrayfromfile(path2, ext)
data3, status, msg = _dataimport.set_arrayfromfile(path3, ext)
# Convert into numpy, split in x and y and normalyze
if data1.shape[1]<2:
    print("Error reading file 1, only detect one column.")
    exit()
if data2.shape[1]<2:
    print("Error reading file 2, only detect one column.")
    exit()
if data3.shape[1]<2:
    print("Error reading file 3, only detect one column.")
    exit()
# Extract the names and turn to float
data_float1 = data1.iloc[1:, 1:].astype(float)
data_float2 = data2.iloc[1:, 1:].astype(float)
data_float3 = data3.iloc[1:, 1:].astype(float)

# Cut first data set
abs_val_array = np.abs(data_float1.loc[:,1] - 3700)
x_pos_min = abs_val_array.idxmin()
abs_val_array = np.abs(data_float1.loc[:,1] - 4700)
x_pos_max = abs_val_array.idxmin()
data_float1 = data1.iloc[x_pos_min:x_pos_max, :].astype(float)
# Cut second data set
data_float2 = data2.iloc[x_pos_min:x_pos_max, :].astype(float)
# Cut third data set
data_float3 = data3.iloc[x_pos_min:x_pos_max, :].astype(float)

# Generate the plot if needed
if plot_flag:
    # Configure axis, plot the data and save it
    # Erase the plot
    #ax.cla()
    # First file of the column is setted as axis name
    #x_name = str(data1.iloc[0,0])
    #ax.set_xlabel(x_name)
    # Separate the name file from the path to set the plot title
    #head, tail = os.path.split(filename)
    #ax.plot(data_float1.loc[:,0], data_float1.loc[:,1], label='Flux-Barred spiral')
    #ax.plot(data_float1.loc[:,0], data_float1.loc[:,2], label='Best Fit')
    #ax.plot(data_float1.loc[:,0], data_float1.loc[:,3], label='Sky Flux')
    #ax.plot(data_float2.loc[:,0], data_float2.loc[:,1], label='Flux-Double nucleus')
    
    ax1 = plt.subplot(311)
    ax1.plot(data_float1.loc[:,1], data_float1.loc[:,2], label='O5 V')
    #plt.tick_params('x', labelsize=6)
    ax1.tick_params('x', labelbottom=False)

    # share x only
    ax2 = plt.subplot(312, sharex=ax1)
    ax2.plot(data_float2.loc[:,1], data_float2.loc[:,2], label='A5 V')
    # make these tick labels invisible
    ax2.tick_params('x', labelbottom=False)

    # share x and y
    ax3 = plt.subplot(313, sharex=ax1, sharey=ax1)
    ax3.plot(data_float3.loc[:,1], data_float3.loc[:,2], label='G0 V')
    #plt.xlim(0.01, 5.0)
    #plt.show()
    
    ax1.legend()
    ax2.legend()
    ax3.legend()
    # Set the path to save the plot and save it
    plot_path = path1[:-4] + '_plot.png'
    fig.savefig(plot_path)
    
# Reproduction
# Normalize the data to sonify
x1, y1, status = _math.normalize(data_float1.loc[:,1], data_float1.loc[:,2], init=x_pos_min)
x2, y2, status = _math.normalize(data_float2.loc[:,1], data_float2.loc[:,2], init=x_pos_min)
x3, y3, status = _math.normalize(data_float3.loc[:,1], data_float3.loc[:,2], init=x_pos_min)

# Reproduction
minval1 = float(data_float1.loc[:,2].min())
maxval1 = float(data_float1.loc[:,2].max())
minval2 = float(data_float2.loc[:,2].min())
maxval2 = float(data_float2.loc[:,2].max())
minval3 = float(data_float3.loc[:,2].min())
maxval3 = float(data_float3.loc[:,2].max())

ordenada1 = np.array([minval1, maxval1])
ordenada2 = np.array([minval2, maxval2])
ordenada3 = np.array([minval3, maxval3])

for x in range (x_pos_min, x_pos_max):
    # Plot the position line
    if not x == x_pos_min:
        line1 = red_line1.pop(0)
        line1.remove()
        line2 = red_line2.pop(0)
        line2.remove()
        line3 = red_line3.pop(0)
        line3.remove()
    abscisa = np.array([float(data_float1.loc[x,1]), float(data_float1.loc[x,1])])
    red_line1 = ax1.plot(abscisa, ordenada1, 'r')
    red_line2 = ax2.plot(abscisa, ordenada2, 'r')
    red_line3 = ax3.plot(abscisa, ordenada3, 'r')
    plt.pause(0.05)
    # Make the sound
    _simplesound.reproductor.set_waveform('sine')
    _simplesound.make_sound(y1[x], 1)
    _simplesound.reproductor.set_waveform('flute')
    _simplesound.make_sound(y2[x], 1)
    _simplesound.reproductor.set_waveform('pipe organ')
    _simplesound.make_sound(y3[x], 1)
    
# Save sound
#x1, y1, status = _math.normalize(data_float1.loc[:,1], data_float1.loc[:,2], init=x_pos_min)
#x, y2, status = _math.normalize(data_float1.loc[:,0], data_float1.loc[:,2], init=1)
#x, y3, status = _math.normalize(data_float1.loc[:,0], data_float1.loc[:,3], init=1)
#x2, y2, status = _math.normalize(data_float2.loc[:,1], data_float2.loc[:,2], init=x_pos_min)
#x3, y3, status = _math.normalize(data_float3.loc[:,1], data_float3.loc[:,2], init=x_pos_min)
wav_name = path1[:-4] + '_sound.wav'
#_simplesound.save_sound_multicol_stars(wav_name, data_float1.loc[:,1], y1, y2, y3, init=x_pos_min)
# Print time
now = datetime.datetime.now()
print(now.strftime('%Y-%m-%d_%H-%M-%S'))
# Counter
i = i + 1

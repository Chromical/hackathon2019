#!/usr/bin/python
import sys
import numpy as np

# File names passed as command line arguments
filename_input = sys.argv[1]
filename_output = sys.argv[2]

# Load arrays from files
data_input = np.loadtxt(filename_input)

# Loop over photosynthetic rates, calculating growth
data_output = []
for prate in data_input:
    grate = 0.5 * prate
    print('growth: photosynthesis rate = %f ---> growth rate = %f' % (
        prate, grate))
    data_output.append(grate)

# Save data to output file
np.savetxt(filename_output, data_output)

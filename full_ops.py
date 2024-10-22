#!/usr/bin/env python
#  full_ops.py
#
# Calculates the output shape and operation count of a fully connected layer
#
# Usage: python3 full_ops.py c_in n_wv
#
# Written by Blake Batchelor, batchelorbh@vt.edu
# Other contributors: none
#
# Parameters:
#    c_in                input channel count
#    n_wv                number of weight vectors
#
# Output:
#    Print output values to screen, including the output channel count,
#    height count, width count, number of additions performed, number of
#    multiplications performed, and number of divisions performed
#
# Revision history:
#    10/22/2024          Script created
#
###############################################################################

#Import relevant modules
import sys

#Define constants
const1 = 0

#User-defined functions
def user_function(param1, param2):
   return param1 + param2

#Pre-initialize input parameters
c_in = float('nan') #Input channel count
n_wv = float('nan') #Number of weight vectors

#Arguments are strings by default
if len(sys.argv) == 3:
   c_in = float(sys.argv[1])
   n_wv = float(sys.argv[2])
else:
   print('Usage: python3 full_ops.py c_in n_wv')
   sys.exit()

#Main body of script

#Calculate the number of output channels
c_out = n_wv

#Calculate the output height and width
h_out = 1
w_out = 1

#Calculate the total number of addition and multiplication operations
adds = n_wv * (c_in - 1)
muls = n_wv * c_in
divs = 0 #Zero for fully-connected layer operations

#Print output variables to the screen
print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed

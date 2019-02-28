# Program: monteCarlo.py
# Author: Soran Dizay-Loftkaer
# Last Date Modified: 2-27-19
# Purpose is to find an approximation for the average number of times to find pi

import math
import random   # Imports math and random functions as needed.

a = 0
b = 0           # Variables for the program.
c = 0
for d in range(10):
  while abs(a - math.pi) < 3.20001:     # Set to try and get 5 decimal points. 
    b += 1
    x = random.random()         # Creates random numbers to test to find pi
    y = random.random()
    if math.sqrt(x**2 + y**2) <= 1.0:      # Equation to find inside pi.
      a += 1

    c = (a / b) * 4

print(c)
                # Made to give outputs on the programs data.
print(a, b)
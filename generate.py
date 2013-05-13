"""
This module creates a shuffled list of slow, medium, and fast days.

Usage: Run with 3 command line inputs, the number of slow, medium, and fast days in that order.  Redirect output to a text file.  Total number of days is printed out first

"""  
import random 
import sys
import string

slow = int(sys.argv[1]);
medium = int(sys.argv[2]);
fast = int(sys.argv[3]);

x = [];
print (slow + medium + fast);
for i in range (0,slow):
    x.extend([0]);
for i in range (0,medium):
    x.extend([1]);
for i in range (0,fast):
    x.extend([2]);
random.shuffle(x);
for i in range(0,(slow + medium + fast)):
    print (x[i]);

# Program to pull data from Nanoplot run and populate csv file
# (which can then be concat to a master .csv file

# Import pandas
from itertools import islice

# Read length
with open('NanoStats.txt') as file:
    for read_length in islice(file,1,2):
        print(float(read_length[31:39].replace(",","")))

with open('NanoStats.txt') as file:
    for y in islice(file,2,3):
        print(y[35:39])

x = read_length[31:39] + " " + y[35:39]
x = print(x)
#with open('NanoStats.txt') as file:
    #for y in islice(file, 3, 4):
        #print(y[35:39])
# Program to pull data from Nanoplot run and populate csv file
# (which can then be concat to a master .csv file

# Import itertools
from itertools import islice

# Mean read length
with open('NanoStats.txt') as file:
    for mean_length in islice(file,1,2):
        print(float(mean_length[31:39].replace(",","")))

# Mean read quality
with open('NanoStats.txt') as file:
    for mean_quality in islice(file,2,3):
        print(float(mean_quality[35:39]))

# Median read length
with open('NanoStats.txt') as file:
    for med_length in islice(file,3,4):
        print(float(med_length[31:39].replace(",","")))

# Median read quality
with open('NanoStats.txt') as file:
    for med_quality in islice(file,4,5):
        print(med_quality[35:39])


x = mean_length[31:39] + " " + mean_quality[35:39] 


x = print(x)
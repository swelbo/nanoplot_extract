# Program to pull data from Nanoplot run and populate csv file
# (which can then be concat to a master .csv file

# Import pandas
#import pandas as pd
# read txt file
#df = pd.read_fwf('NanoStats.txt')
# write file to csv
#df.to_csv('log.csv')

#with open('test.txt') as file:
	#first_line = file.readlines()[2:4]
#print(first_line)

from itertools import islice
with open('NanoStats.txt') as file:
    for read_length in islice(file, 1, 2):
        print(read_length[31:39])

print(read_length[31:39])

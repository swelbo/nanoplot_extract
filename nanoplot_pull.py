# Program to pull data from Nanoplot run and populate csv file
# (which can then be concat to a master .csv file

# Import itertools
from itertools import islice

# Mean read length
with open('NanoStats.txt') as file:
    for mean_length in islice(file,1,2):
        a = (float(mean_length[25:39].replace(",","")))

# Mean read quality
with open('NanoStats.txt') as file:
    for mean_quality in islice(file,2,3):
        b = (float(mean_quality[34:39]))

# Median read length
with open('NanoStats.txt') as file:
    for med_length in islice(file,3,4):
        c = (float(med_length[30:39].replace(",","")))

# Median read quality
with open('NanoStats.txt') as file:
    for med_quality in islice(file,4,5):
        d = (float(med_quality[30:39].replace(",","")))

# Number of reads:
with open('NanoStats.txt') as file:
    for no_reads in islice(file,5,6):
        e = (float(no_reads[29:39].replace(",","")))

# Read length N50:
with open('NanoStats.txt') as file:
    for STDEV in islice(file,6,7):
        f = (float(STDEV[29:39].replace(",","")))

# Number of reads:
with open('NanoStats.txt') as file:
    for no_reads in islice(file,7,8):
        g = (float(no_reads[29:39].replace(",","")))

# Number of bases
with open('NanoStats.txt') as file:
    for total_bases in islice(file,8,9):
         h = (float(total_bases[25:39].replace(",","")))

#x = mean_length[31:39] + " " + mean_quality[35:39] 
print(type(a))#,b,c,d,e,f,g,h)
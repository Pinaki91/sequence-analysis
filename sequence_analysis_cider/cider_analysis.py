#importing libraries
import os
from localcider.sequenceParameters import SequenceParameters
from natsort import natsorted
import matplotlib.pyplot as plt

#Assigning path and fasta files to be analyzed
path = "RNAP/"
filelist = os.listdir(path)
#Sorting them in an order
filelist=natsorted(filelist)

#create an empty lists for sequences to be processed
list_of_SeqObjs = []
#First cider command to load the fasta files into the list of sequences
for file in filelist:
   file= path + file
   list_of_SeqObjs.append(SequenceParameters(sequenceFile=file))
#output file
f = open("cider_rnap.dat", "w")

#Cider commands to get the parameters of interest
for obj in list_of_SeqObjs:
   f_pos=obj.get_fraction_positive()
   f_neg=obj.get_fraction_negative()
   mhyd=obj.get_uversky_hydropathy()
   mnc=obj.get_mean_net_charge(pH=7)
   kappa=obj.get_kappa()
   f.write("%s %f %f %f %f %f\n"%(filelist[list_of_SeqObjs.index(obj)],f_pos,f_neg,mhyd,mnc,kappa))
#closing the output file
f.close()

#For plotting mean net charge vs mean hydropathy
with open('cider_rnap.dat') as f:
    lines = f.readlines()
    x = [line.split()[3] for line in lines]
    y = [line.split()[4] for line in lines]

#replacing strings to floats
for i in range(0, len(x)): 
    x[i] = float(x[i])
    y[i] = float(y[i])

#plotting and saving figure 
plt.scatter(x,y)
plt.xlabel('Mean Hydropathy')
plt.ylabel('Mean net charge')
plt.xlim(0, 0.8)
plt.ylim(0, 0.4)
fig1=plt.gcf() 
plt.show()
plt.draw()
fig1.savefig('RNAP_table1.png')

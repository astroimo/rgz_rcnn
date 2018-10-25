import os,glob
import numpy as np


flist = glob.glob(os.path.join('*.out'))
flist.sort()


data = []
for i,afil in enumerate(flist):
	with open(afil) as fil:
		lines = fil.readlines()
	for i,line in enumerate(lines):
		if line[0] == '0':
			line = line[:5]
			line = float(line)
			data.append(line)

data = np.array(data)
print (len(data))

np.save('3c_acc.npy',data)
print ('3c_acc.npy has saved ;) ')


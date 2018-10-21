import glob, os, re
import numpy as np

files = glob.glob(os.path.join('s*'))
files.sort()
image_num = 922
file_num = 3 * 6
save_file = 'learning_curve_val_loss.npy'
idx = 0
data = []
for nfil in files:
	idx += image_num 
	print ('loading: ',nfil)

	with open(nfil) as fil:
		lines = fil.readlines()
	iter_num_idx = 0
	for i,line in enumerate(lines):
		if line[:4] == 'iter':
			iter_num = line[6:8]
			iter_num_idx += 10 
			#print ('iter_num is ',iter_num, 'iter_num_idx is',str(iter_num_idx)[:2])
			if not iter_num == str(iter_num_idx)[:2]:
				print ('ouch!! line number is ',i)
				break
			value = re.search('\d.\d\d\d\d',line).group()
			value = float(value)
			data.append(value)
	#print ('data length is',len(data))
	#print ('idx = ',idx)
data_ary_ori = np.array(data).reshape(file_num, image_num)
average = []
for row in data_ary_ori:
	ave = np.average(row)
	average.append(ave)
data_ary = np.array(average).reshape(3,6)
print ('data_ary=\n',data_ary)
np.save(save_file,data_ary)



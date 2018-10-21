import glob, os, re
import numpy as np

files = glob.glob(os.path.join('*.out'))
files.sort()
print ('file list is ',files)
file_num = len(files)
# iter = 80000 -> iters =8000
iters = 8000
save_file = 'learning_curve_tra_loss.npy'
data_num = 12280
data_type_num = 3
points_num = 6
# processing txt data
data = []
for nfil in files:
	with open(nfil) as fil:
		lines = fil.readlines()
	for idx,line in enumerate(lines):
		if line[:4] == 'iter':
			value = re.search('\d.\d\d\d\d',line).group()
			value = float(value)
			if value > 1:
				print ('file: ',nfil,'line: ',str(idx), 'value: ',value)
			data.append(value)
data_ary_ori = np.array(data).reshape(file_num,iters)
index = [ num*1000 for num in range(1,9)]
data_ary = []


for i, row in enumerate(data_ary_ori):
	average = np.average(row[-data_num:])
	data_ary.append(average)

#	if i == 0:
		#D1_264 has 6141 data, other has 6140 data.
#		data_num = data_num + 1*2
# calculation of loss
#	for p in index:
#		start_point = p - data_num
#		if start_point < 0: #get loss for 10000 iter
#			start_point = 0 #get loss for all data (12280) at the point of 20k,30k....80k
#		average = np.average(row[start_point:p])
#		data_ary.append(average)

data_ary = np.array(data_ary).reshape(data_type_num,points_num)
np.save(save_file,data_ary)
print (save_file, ' was saved\n',data_ary)


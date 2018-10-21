
sbj = 'example_train_slurm_pleiades.sh'
ldata = [
'lc_D1_1023',
'lc_D1_2046',
'lc_D1_3069',
'lc_D1_4092',
'lc_D1_5115',
'lc_D1_6138',
'lc_D3_1023',
'lc_D3_2046',
'lc_D3_3069',
'lc_D3_4092',
'lc_D3_5115',
'lc_D3_6138',
'lc_D4_1023',
'lc_D4_2046',
'lc_D4_3069',
'lc_D4_4092',
'lc_D4_5115',
'lc_D4_6138']
print (ldata)

for idx,fil in enumerate(ldata):
	new_file_name = fil + '.sh'
	with open(sbj) as data:
		lines = data.readlines()
	new_file = open(new_file_name,'w')
	for i, line in enumerate(lines):
		new_line = line
		if i ==5:
			new_line = '#SBATCH --job-name=lea_cur'
		if i == 17:
			new_line = '                    --imdb rgz_2017_' + fil  + ' \\\n'
		if i == 19:
			if fil[3:5] == 'D1':
				new_line = '                    --cfg $RGZ_RCNN/experiments/cfgs/faster_rcnn_end2end_264.yml \\\n'
		new_file.write(new_line)
	new_file.close()
	print (new_file_name, 'was saved ')



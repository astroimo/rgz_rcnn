data_type_unit = 1023
weight = ['50000','60000','50000'] #D1,D3,D4


with open('lc_D1_1023_val.sh') as afile:
	lines = afile.readlines()
for i,dtype in enumerate(['D1','D3','D4']):
	for j in range(6):
		new_file_name = 'lc_' + dtype + '_' + str(data_type_unit * (1+j)) + '_val.sh'
		new_file = open(new_file_name, 'w')
		for k, line in enumerate(lines):
			new_line = line
			if k == 16:
				new_line = '                    --imdb rgz_2017_' + new_file_name[:-3] + ' \\\n'
			if k == 17:
				if dtype == 'D1':
					new_line = '                    --cfg $RGZ_RCNN/experiments/cfgs/faster_rcnn_end2end_264.yml \\\n'
				else:
					new_line = '                    --cfg $RGZ_RCNN/experiments/cfgs/faster_rcnn_end2end.yml \\\n'
			if k == 19:
					new_line = '                    --weights $RGZ_RCNN/output/faster_rcnn_end2end/rgz_2017_'+ new_file_name[:-7] +  '/VGGnet_fast_rcnn-80000 \\\n'#				if dtype == 'D3':
#					new_line = '                    --weights $RGZ_RCNN/output/faster_rcnn_end2end/rgz_2017_'+ new_file_name[:-7] +  '/VGGnet_fast_rcnn-60000 \\\n'
#				else:
#					new_line = '                    --weights $RGZ_RCNN/output/faster_rcnn_end2end/rgz_2017_' + new_file_name[:-7]  + '/VGGnet_fast_rcnn-50000 \\\n'
			new_file.write(new_line)
		new_file.close()
		


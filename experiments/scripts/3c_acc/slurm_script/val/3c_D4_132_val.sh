#!/bin/bash

#SBATCH --partition=mlgpu
#SBATCH --time=00:30:00
#SBATCH --gres=gpu:1
#SBATCH --job-name=3c_val \

# if cuda driver is not in the system path, customise and add the following paths
# export PATH=/usr/local/cuda-8.0/bin${PATH:+:${PATH}}
# export LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}

export PYTHONPATH=$PYTHONPATH:/home/chen/software/lib/python2.7/site-packages
time RGZ_RCNN=/home/yuno/intern/rgz_rcnn
/usr/bin/python $RGZ_RCNN/tools/test_net.py \
                    --device gpu \
                    --device_id 0 \
                    --imdb rgz_2017_3c_D4_132_val \
                    --cfg $RGZ_RCNN/experiments/cfgs/faster_rcnn_end2end_132.yml \
                    --network rgz_test \
                    --weights $RGZ_RCNN/output/faster_rcnn_end2end/rgz_2017_3c_D4_132/VGGnet_fast_rcnn-80000 \
                    --comp

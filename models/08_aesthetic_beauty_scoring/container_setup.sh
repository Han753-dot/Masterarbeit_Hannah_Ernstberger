#!/bin/bash

pip install --upgrade pip
pip install opencv-contrib-python

cd /opt/caffe/build
cmake .. -DUSE_CUDNN=OFF
make -j"$(nproc)"
make install
make pycaffe
pip install --upgrade "pip<21"
pip install --ignore-installed --force-reinstall "numpy==1.16.6" "scipy==1.2.3" "scikit-image==0.14.5"

python2.7 -c "import caffe; print('Caffe (no cuDNN) OK')"
cd

exec bash

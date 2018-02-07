"""
scipy显示图像
creat by swm
2018/02/07
"""
import numpy as np
from scipy.misc import imread, imresize
import matplotlib.pyplot as plt

# better path
from pathlib import Path
dataset_path = 'scipylearn'
dataset_root = Path('E:\githubcode\CS231learnresult')

imgpath = dataset_root/dataset_path/'source.jpg'
img = imread(imgpath)
img_tinted = img * [1, 0.9, 0.9]
plt.subplot(1, 2, 1)
plt.imshow(img)

plt.subplot(1, 2, 2)
plt.imshow(np.uint8(img_tinted))

plt.show()


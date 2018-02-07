"""
scipy的基本操作
create by swm
2017/02/07
"""
import numpy as np
from scipy.misc import imread, imsave, imresize
from scipy.spatial.distance import pdist, squareform


# 读取图片和resize图片
def scipyread(imgpath):
    img = imread(imgpath)
    print(img.dtype, img.shape)
    # 改变三原色的色彩
    img_tinted = img * [1, 0.95, 0.95]
    # resize改变色彩后的图片
    img_tinted = imresize(img_tinted, (300, 300))
    imsave('result.jpg', img_tinted)


# 计算一个矩阵中点其他所有点之间的距离
def cacultdistance(x):
    d = squareform(pdist(x, 'euclidean'))
    print(d)
    # scipy.spatial.distance.cdist计算不同集合中点的距离


if __name__ == '__main__':
    # imgpath = 'source.jpg'
    # scipyread(imgpath)
    x = np.array([[0, 1], [1, 0], [2, 0]], dtype=int)
    cacultdistance(x)
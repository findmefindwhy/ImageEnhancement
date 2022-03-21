#tf.image.psnr(tf_img1, tf_img2, max_val=255)
from PIL import Image
import numpy as np
import cv2
import math

image1 = cv2.imread('standardprostate.jpg',0)
img1 = np.array(image1)
image2 = cv2.imread('mix0.1.jpg',0)
img2 = np.array(image2)


def psnr(img1, img2):
    #img1 = np.array(image1).astype(np.float64)
    #img2 = np.array(image2).astype(np.float64)
    mse = np.mean((img1-img2)**2)
    if mse == 0:
        return float('inf')
    else:
        return 20*np.log10(255/np.sqrt(mse))

def mse(img1,img2):
    mse = np.mean((img1-img2)**2)
    return mse

def entropy(img):
    tmp = []
    for i in range(256):
        tmp.append(0)
    val = 0
    k = 0
    res = 0
    for i in range(len(img)):
        for j in range(len(img[i])):
            val = img[i][j]
            tmp[val] = float(tmp[val] + 1)
            k =  float(k + 1)
    for i in range(len(tmp)):
        tmp[i] = float(tmp[i] / k)
    for i in range(len(tmp)):
        if(tmp[i] == 0):
            res = res
        else:
            res = float(res - tmp[i] * (math.log(tmp[i]) / math.log(2.0)))
    return res

if __name__ == "__main__":
    print("峰值信噪比为:",psnr(img1,img2))
    print("均方差为:",mse(img1,img2))
    print("信息熵为:",entropy(img2))


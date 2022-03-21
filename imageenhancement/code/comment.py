from cv2 import cv2
import numpy as np
import math
#计算信息熵
tmp = []
for i in range(256):
    tmp.append(0)
val = 0
k = 0
res = 0
image = cv2.imread('standardprostate.jpg',0)#0代表读入灰度图片
img = np.array(image)
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
print("信息熵为：",res)

#计算对比度
def contrast(img0):   
        img1 = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY) #彩色转为灰度图片
        m, n = img1.shape
        #图片矩阵向外扩展一个像素
        img1_ext = cv2.copyMakeBorder(img1,1,1,1,1,cv2.BORDER_REPLICATE) 
        rows_ext,cols_ext = img1_ext.shape
        
        b = 0.0
        for i in range(1,rows_ext-1):
            for j in range(1,cols_ext-1):
                b += (( int(img1_ext[i,j]) -int(img1_ext[i,j+1])**2) + (int(img1_ext[i,j])-int(img1_ext[i,j-1]))**2 + 
                        (int(img1_ext[i,j])-int(img1_ext[i+1,j]))**2 + (int(img1_ext[i,j])-int(img1_ext[i-1,j]))**2)
    
        cg = b/(4*(m-2)*(n-2)+3*(2*(m-2)+2*(n-2))+2*4) #对应上面48的计算公式
        img1=img1/1.0
        print("对比度为：",cg)
       
img= cv2.imread('standardprostate.jpg')
contrast(img)

#计算方差
import cv2 as cv

img = cv.imread('standardprostate.jpg', 0)
height, width = img.shape
size = img.size

p = [0]*256

for i in range(height):
    for j in range(width):
        p[img[i][j]] += 1

m = 0
for i in range(256):
    p[i] /= 256
    m += i*p[i]

s = 0
for i in range(256):
    s += (i-m)*(i-m)*p[i]

print("方差为：",s)
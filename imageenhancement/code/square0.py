#encoding:utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread('mix0.1.jpg')
cv2.imshow("src", src)

plt.hist(src.ravel(), 256)
plt.rcParams['font.sans-serif']=['SimHei']#正常显示中文汉字
plt.xlabel("灰度级",fontsize=14)
plt.ylabel("像素/个数",fontsize=14)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
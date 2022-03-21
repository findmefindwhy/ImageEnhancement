import cv2
import matplotlib.pyplot as plt
import numpy as np

def img_show(name,img):
    """matplotlib图像显示函数
    name：字符串，图像标题
    img：numpy.ndarray，图像
    """
    plt.imshow(img,'gray')
    #plt.xticks([])
    #plt.yticks([])
    plt.xlabel(name,fontproperties='FangSong',fontsize=12)
    

if __name__=="__main__":

    img1 = cv2.imread("standardprostate")
    #别忘了中括号[img1],[0],None,[256],[0,256]，只有mask没有中括号
    hist = cv2.calcHist([img1],None,[256],[0,256])
    
    plt.figure(figsize=(12,8),dpi=80)
    plt.subplot(121)
    #img_show('原图',img1)
    plt.subplot(122)
    plt.plot(hist)
    plt.xlim([0,256])
    plt.ylim([0,800000])
    plt.xlabel('直方图',fontproperties='FangSong',fontsize=12)
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
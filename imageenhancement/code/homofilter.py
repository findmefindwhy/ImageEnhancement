import cv2
import numpy as np
import evo

#网上没找到现成的同态滤波器的包，所以自定义实现同态滤波器

#####################################################################
#############        自定义同态滤波器函数      ################r1-亮度
#####################################################################
def homomorphic_filter(src,d0=70,c=0.1,rh=2.2,h=2.2,r1=0.7,l=0.7):
    #d0 截止频率，越大图像越亮
    #r1 低频增益,取值在0和1之间
    #rh 高频增益,需要大于1
    #c 锐化系数
    #图像灰度化处理

    gray = src.copy()

    if len(src.shape) > 2:#维度>2
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    #图像格式处理
    gray = np.float64(gray)

    #设置数据维度n
    rows, cols = gray.shape

    #傅里叶变换
    gray_fft = np.fft.fft2(gray)

    #将零频点移到频谱的中间，就是中间化处理
    gray_fftshift = np.fft.fftshift(gray_fft)

    #生成一个和gray_fftshift一样的全零数据结构
    dst_fftshift = np.zeros_like(gray_fftshift)

    #arange函数用于创建等差数组，分解f(x,y)=i(x,y)r(x,y)
    M, N = np.meshgrid(np.arange(-cols // 2, cols // 2), np.arange(-rows//2, rows//2))#注意，//就是除法

    #使用频率增强函数处理原函数（也就是处理原图像dst_fftshift）
    D = np.sqrt(M ** 2 + N ** 2)#**2是平方
    Z = (rh - r1) * (1 - np.exp(-c * (D ** 2 / d0 ** 2))) + r1#
    dst_fftshift = Z * gray_fftshift
    dst_fftshift = (h - l) * dst_fftshift + l

    #傅里叶反变换（之前是正变换，现在该反变换变回去了）
    dst_ifftshift = np.fft.ifftshift(dst_fftshift)
    dst_ifft = np.fft.ifft2(dst_ifftshift)

    #选取元素的实部
    dst = np.real(dst_ifft)

    #dst中，比0小的都会变成0，比255大的都变成255
    #uint8是专门用于存储各种图像的（包括RGB，灰度图像等），范围是从0–255
    dst = np.uint8(np.clip(dst, 0, 255))
    return dst
#自定义函数完毕

#########################################################
################       主函数开始         ################
#########################################################

img = cv2.imread('standardprostate.jpg',0)
#将图片执行同态滤波器
img_new = homomorphic_filter(img)
cv2.imwrite("sptongtai.jpg", img_new)
def excel(n):
    n=200
    re=[[0]*3 for i in range(n) ]#创建一个二维列表
    for i in range(n):
        img_new = homomorphic_filter(img,i)
        re[i][0]=evo.psnr(img,img_new)
        re[i][1]=evo.mse(img,img_new)
        re[i][2]=evo.entropy(img_new)

    output=open('evostrengthen.xls','w',encoding='gbk')  #不需要事先创建一个excel表格，会自动生成，gbk为编码方式，支持中文，w代表write
    output.write('psnr\tmse\tentropy\n')
    for i in range(len(re)):
        for j in range(len(re[i])):
            output.write(str(re[i][j]))    #write函数不能写int类型的参数，所以使用str()转化
            output.write('\t')   #相当于Tab一下，换一个单元格
        output.write('\n')       #写完一行立马换行
    output.close()

#输入和输出合并在一起输出
result = np.hstack((img,img_new))
#打印
cv2.imshow('outputPicName',result)
cv2.waitKey()
cv2.destroyAllWindows()




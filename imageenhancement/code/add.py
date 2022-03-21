import matplotlib.pyplot as plt

#Import required packages
import cv2

#Read image 1
img1=cv2.imread("speqlzd.jpg")
#Read image 2
img2=cv2.imread("sptongtai.jpg")

#Define alpha and beta
alpha=0.10
beta=0.90

#Blend images
final_image=cv2.addWeighted(img1,alpha,img2,beta,0.0)

#show image
cv2.imshow("mix0.1",final_image)
cv2.imwrite("mix0.1.jpg",final_image)
cv2.waitKey(0)
import cv2
import matplotlib.pyplot as plt
img1 = cv2.imread("lena.jpg" , 0)
img2 = cv2.bilateralFilter(img1,1,100,50)# 1:直徑區域直徑，100:色彩值，50:空間值
plt.imshow(img1,"gray")
plt.show()
plt.imshow(img2 ,"gray")
plt.show()
import cv2
import matplotlib.pyplot as plt
img1 = cv2.imread("lena.jpg" , 0 )#讀入圖片
#平均濾波
img2 = cv2.blur(img1,(21 , 21))
#高斯濾波用法
#img2 = cv2.GaussianBlur(img1,(21 , 21),10)
plt.imshow(img1 , cmap="gray")
plt.show()
plt.imshow(img2 , cmap="gray")
plt.show()
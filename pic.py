import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("lena.jpg", 0)#讀取圖片檔名
img2 = cv2.resize(img , (1024,1024), interpolation = cv2.INTER_LINEAR)#使用雙線性內插縮放圖片
def re(img , theta):
  (h , w) = img.shape[:2]
  (cX , cY) = (w/2 , h/2)
  M = cv2.getRotationMatrix2D((cX, cY), theta, 1)
  cos = np.abs(M[0, 0])
  sin = np.abs(M[0, 1])
  nW = int((h * sin) + (w * cos))
  nH = int((h * cos) + (w * sin))
  M[0, 2] += (nW / 2) - cX
  M[1, 2] += (nH / 2) - cY
  img2 = cv2.warpAffine(img, M, (nW, nH))
  return img2
img3 = re(img ,80)#設定圖片旋轉角度
plt.imshow(img3 , cmap= "gray")#以灰階顯示圖片
plt.show()

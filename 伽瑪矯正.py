import cv2
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as special
def gamma(f , gam):
  g = f.copy()
  nr,nc = f.shape[:2]
  x = 255.0/(255.0**gam)
  table = np.zeros(256)#計算
  for i in range(256):
    table[i] = round(i**gam*x,0)
  if f.ndim !=3:
    for x in range(nr):
      for y in range(nc):
        g[x, y] = table[f[x,y]]
  else:
    for x in range(nr):
      for y in range(nc):
        for k in range(3):
          g[x,y,k] = table[f[x,y,k]]
  return g
img = cv2.imread("lena.jpg" , 0)#讀入圖片
img1 = gamma(img , 0.1)
img2 = gamma(img , 3)#變數>1變暗
img3 = gamma(img , 0.5)#變數<1變亮
plt.imshow(img,"gray")
plt.show()
plt.imshow(img1,"gray")
plt.show()
plt.imshow(img2,"gray")
plt.show()
plt.imshow(img3,"gray")
plt.show()
import cv2
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as special
def beta(f , a=2.0 , b=2.0):
  g = f.copy()
  nr,nc = f.shape[:2]
  x = np.linspace(0,1,256)
  table = np.round(special.betainc(a,b,x)*256,0)#不完整Beta函數計算
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
img = cv2.imread("lena.jpg" , 0)
img1 = beta(img , a = 0.5, b = 0.5)
img2 = beta(img , a = 2.0, b = 2.0)
plt.imshow(img,"gray")
plt.show()
plt.imshow(img1,"gray")
plt.show()
plt.imshow(img2,"gray")
plt.show()
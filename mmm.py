import random
from random import seed
import cv2

seed(1)
img_name = input("Enter image name (with extension): ")
img = cv2.imread(img_name)
img2 = cv2.resize(img, (300, 300))
cv2.imshow("original image", img2)

img3 = img2.copy()
l1 = []
for i in range(0, 256, 1):
    l1.append(i)

list1 = []
for i in range(0, 256, 1):
    inp = random.random()
    list1.append(inp)
list1.sort()


def my_function(x):
    return (random.random())


list2 = []
for i in list1:
    list2.append(my_function(i))
list3 = list2.copy()
list3.sort()

list4 = []
for i in list2:
    opt = list3.index(i)
    list4.append(opt)

m, n, p = img2.shape
for i in range(0, m, 1):
    for j in range(0, n, 1):
        for k in range(0, p, 1):
            o = img3[i][j][k]
            img3[i][j][k] = list4[o]

cv2.imshow("substituted image", img3)

""" REVERSE """
img4 = img3.copy()
for x in range(0, m, 1):
    for y in range(0, n, 1):
        for z in range(0, p, 1):
            w = img4[x][y][z]
            img4[x][y][z] = list4.index(w)

cv2.imshow("new original img", img4)

cv2.waitKey()

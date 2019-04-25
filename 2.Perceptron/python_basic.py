import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

x = np.array([1.0, 2.0, 3.0])
print(x)
type(x)
y = np.array([2.0, 4.0, 6.0])
x + y
x - y
x * y
x / y
x = np.array([1.0, 2.0, 3.0])
x / 2.0
A = np.array([[1, 2], [3, 4]])
print(A)
A.shape
A.dtype
B = np.array([[3, 0], [0, 6]])
A + B
A * B
print(A)
A * 10
A = np.array([[1, 2], [3, 4]])
B = np.array([10, 20])
A * B
X = np.array([[51, 55], [14, 19], [0, 4]])
print(X)
X[0]
X[0][1]
for row in X:
    print(row)
X = X.flatten()
print(X)
X[np.array([0, 2, 4])]
X > 15
X[X > 15]

#그래프 그리기
x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label = "sin")
plt.plot(x, y2, linestyle="--", label = "cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title('sin&cos')
plt.legend()
plt.show()
#이미지 표시하기
img = imread('LENA256.png')
plt.imshow(img)
plt.show()
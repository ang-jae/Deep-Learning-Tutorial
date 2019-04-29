import numpy as np

A = np.array([[1,2],[3,4]])
print(A.shape)

B = np.array([[5,6], [7,8]])
print(B.shape)

print(np.dot(A, B))

A = np.array([[1,2,3], [4,5,6]])
print(A.shape)

B = np.array([[1,2], [3,4], [5, 6]])
print(B.shape)

print(np.dot(A, B))

C = np.array([[1,2], [3,4]])
print(C.shape)
print(A.shape)
# print(np.dot(A, C))#결과 : 오류 출력

#다차원 배열을 곱하려면 두 행렬의 대응하는 차원의 원소 수를 일치시켜야 한다.
#이러한 원칙을 적용하여 코드를 수정하면 다음과 같다.
A = np.array([[1, 2], [3, 4], [5, 6]])
print(A.shape)
B = np.array([7, 8])
print(B.shape)
print(np.dot(A, B))#더 이상 오류가 나오지 않음을 알 수 있다.
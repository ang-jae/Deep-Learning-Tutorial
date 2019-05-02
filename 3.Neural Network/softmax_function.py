import numpy as np

a = np.array([0.3, 2.9, 4.0])

exp_a = np.exp(a)
print(exp_a)

sum_exp_a = np.sum(exp_a)
print(sum_exp_a)

y = exp_a / sum_exp_a
print(y)
# 앞으로 사용하기 위해 함수화
#def softmax(a):
#    exp_a = np.exp(a)
#    sum_exp_a = np.sum(exp_a)
#    y = exp_a / sum_exp_a
#    return y
#문제점 : overflow
a = np.array([1010, 1000, 990])
np.exp(a) / np.sum(np.exp(a)) # error 발생.
#문제 해결
c = np.max(a) # c = 1010 (최댓값)
print(a - c)
print(np.exp(a - c) / np.sum(np.exp(a - c)))
#softmax 재정의
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c) # overflow 대책
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

a = np.array([0.3, 2.9, 4.0])
y = softmax(a)
print(y)
print(np.sum(y))
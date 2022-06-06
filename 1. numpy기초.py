import numpy as np

#column vector
c = np.array([1,2,3])
print(c.shape)
print (c[0])

#row vector
r = np.array([[1,2,3]])
print(r.shape)
print(r[0,1])



#전부 0으로 행렬 만들기
a = np.zeros((2,2))
print(a)

#전부 1로 행렬 만들기
b=np.ones((2,2))

#한 원소로 행렬 채우기
c = np.full((2,2),7)

#랜덤 행렬
d = np.random.random((2,2))

#행렬 생성
A = np.array([1,2],[3,4],[5,6])
B= np.array([11,12,13,14],[15,16,17,18])
#뒤집기
A.T

#행렬 곱
np.dot(A,B)
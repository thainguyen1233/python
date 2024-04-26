#bài tập python
#bài tập 2: xây dựng module
#nhân 2 ma trận
#ma traajn chuyển vị
#cộng 2 ma trận

import numpy as np
def cong():
    A=np.array([[1,2,3],[4,5,6],[7,8,9]])
    B=np.array([[1,2,3],[4,5,6],[7,8,9]])
    result = np.dot(A, B)
    return result
def chuyen_vi():
    A=np.array([[1,2,3],[4,5,6],[7,8,9]])
    B=np.transpose(A)
    return B
def nhan():
    A=np.array([[1,2,3],[4,5,6],[7,8,9]])
    B=np.array([[1,2,3],[4,5,6],[7,8,9]])
    result = np.add(A,B)
    return result


#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:janvn
# datetime:18-7-29 下午2:30
# software:PyCharm

import numpy as np

# test1
matrix = np.array([[1,2,3],[20,30,40]])
#print(matrix[0,1])

# test2
matrix1 = np.array([[1,2,3],[4,5,6],[7,8,9],[4,1,1]])
#print(matrix1[1:3,:])
#print(matrix1[1:3,0:2])

# test3
m = (matrix1 == 6)
#print(m)

# test4
first_column_4 = (matrix1[:,0] == 4)
#print(first_column_4)
#print(matrix1[first_column_4,:])

#test5
matrix2 = np.array([1,2,3,4,5])
equal_to_1_and_2 = (matrix2 == 1) & (matrix2 == 2)
#print(equal_to_1_and_2)
equal_to_1_or_2 = (matrix2 == 1) | (matrix2 == 2)
#print(equal_to_1_or_2)

# test6: 2.3.8
matrix2[equal_to_1_or_2] = 100
#print(matrix2)

# test7: 2.3.9
vector = np.array(["1","2","3"])
vector = vector.astype(float)
#print(vector)

#test8: 2.3.10
matrix3 = np.array([[1,2,3],[1,2,3],[1,2,3]])
print(matrix3.sum(axis=1))   # sum of row
print(matrix3.sum(axis=0))   # sum of column
import numpy as np

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

print(array[0:4:2])

print(array[:, 1::2])

#Selecting the 4 quadrants
print(array[0:2, 0:2])
print(array[0:2, 2:4])
print(array[2:4, 0:2])
print(array[2:4, 2:4])
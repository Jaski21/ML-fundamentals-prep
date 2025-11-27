import numpy as np

array = np.array([1.14,2.25,3.74])

# Scalar operations
print(array + 1)
print(array - 2)
print(array * 3)
print(array / 4)
print(array ** 5)

# Vectorized funcs
print(np.sqrt(array))
print(np.round(array))
print(np.floor(array))
print(np.ceil(array))
print(np.pi)

radii = np.array([1,2,3])
print(f"Areas: {np.pi * (radii ** 2)}")

# Element wise

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
print(arr1+arr2) # +, -, *, /, ** all work element wise


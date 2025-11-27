import numpy as np

arr = np.array([[1,2,3,4,5],
                [6,7,8,9,10]])

print(np.sum(arr))
print(np.mean(arr))
print(np.std(arr)) # Standard deviation
print(np.var(arr)) # Variance
print(np.min(arr)) # Max works too
print(np.argmax(arr)) # Returns position
print(np.sum(arr, axis=0)) # Sums columns. axis=1 sums rows
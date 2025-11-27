import numpy as np

rng = np.random.default_rng()

print(rng.integers(low=1, high=11, size=(2, 3)))
print(rng.integers(low=1, high=101, size=(10, 10)))

print(np.random.uniform(low=-1, high=1, size=5))
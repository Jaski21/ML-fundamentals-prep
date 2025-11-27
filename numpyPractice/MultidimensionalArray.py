import numpy as np

letters = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                    [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                    [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]])
print(letters)

# Print dimensions and shape
print(letters.ndim, letters.shape)

# Create a word using chain indexing
word = letters[1,0,0] + letters[0,0,0] + letters[2,0,0] + letters[1,0,1] + letters[0,2,2]
print(word)
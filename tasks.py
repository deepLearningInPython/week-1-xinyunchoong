import numpy as np

# Follow the tasks below to practice basic Python concepts.
# Write your code in between the dashed lines.
# Don't import additional packages. Numpy suffices.

# Task 1: 
# Instructions:
#Write a function that takes one numeric argument as input. 
#If the number is larger than zero, the function should return 1, otherwise is should return -1.
#The name of the function should be step

# Your code here:
# -----------------------------------------------
def step(x):
    if x > 0:
        return 1
    else:
        return -1

print(step(1))
print(step(-1))
# -----------------------------------------------


# Task 2:
# Instructions:
#Write a function that takes in two arguments: a numpy array, and an integer (call argument "cutoff" and set default to 0).
#The function should return a numpy array of the same length, with all elements smaller than the cutoff being set to cutoff).
#The name of the function should be ReLu


# Your code here:
# -----------------------------------------------
def ReLu(x, cutoff = 0):
    x = np.array(x)
    return np.maximum(x, cutoff)

1 == np.array([-2, -1, 0, 1, 2])
print(ReLu(1))
# -----------------------------------------------


# Task 3:
# Instructions:
#Write a function that takes in a two-dimensional numpy array of size (n, p) and a one-dimensional numpy array of size p.
#The function should start by multiplying the two numpy arrays (matrix multiplication).
#Next, apply the ReLu function from above to the resulting matrix and return the result.
#Name the function neural_net_layer

# Your code here:
# -----------------------------------------------
def neural_net_layer(matrix, weight):
    matrix = np.array(matrix)
    weight = np.array(weight)
    result = matrix @ weight  # matrix multiplication
    return ReLu(result)

X = np.array([[1, -2, 3],
              [0, 4, -1]])
w = np.array([0.5, -0.25, 0.1])

print(neural_net_layer(X, w))
# ------------------------------------------
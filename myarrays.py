import numpy as np

"""
integers = np.array([1, 2, 3])

# print(type(integers))

# One dimensional array
list_num = np.array([x for x in range(2, 21) if x % 2 == 0])

# print(list_num)

# two dimensional array
integers = np.array([[1, 2, 3], [4, 5, 6]])
print(integers)

floats = np.array([0.0, 0.1, 0.2, 0.3, 0.4])
print(floats)

a = integers.dtype
b = integers.ndim
c = integers.shape
d = integers.size

print()

for row in integers:
    print(row)
    for col in row:
        print(col, end=" ")

for i in integers.flat:
    print(i)


import random


a = np.array(
    [
        [random.randint(1, 10) for x in range(5)],
        [random.randint(1, 10) for x in range(5)],
    ]
)

# Using np random module
b = np.array(np.random.randint(1, 10, size=(2, 5)))




c = np.zeros(5)
d = np.ones(5)
e = np.ones((2, 4), dtype=int)
f = np.full((3, 5), 13)
g = np.arange(5)
h = np.arange(5, 10)
i = np.arange(10, 1, -2)


print()

# Create even spaced float range
print(np.linspace(0.0, 1.0, num=5))

# reshape method to change dimension
array1 = np.arange(1, 21)

array2 = array1.reshape(4, 5)

print(array1)

print(array2)



array3 = np.arange(1, 100001).reshape(4, 25000)

print(array3)

array4 = np.arange(1, 100001).reshape(100, 1000)
print(array4)
"""
# Argumented operations
numbers = np.arange(1, 6)
numbers += 10

print(numbers)

print(numbers * 2)

print(numbers ** 3)

print(numbers)


# multiplying integer arrays with floating point arrays
# result is floating point
numbers2 = np.linspace(1.1, 5.5, 5)

print(numbers * numbers2)

# Compare arrays
print(numbers >= 13)

print(numbers2 < numbers)

print(numbers2 == numbers2)
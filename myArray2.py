import numpy as np

"""
grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])
print(grades)
# each row represents a student
# each col represents a Test

a = grades.sum()
b = grades.min()
c = grades.max()
d = grades.mean()
e = grades.std()
f = grades.var()

# Processes by column
g = grades.mean(axis=0)

print("Average of each test", g)

# Processes by row
h = grades.mean(axis=1)
print("Average of each student", h)



# Universal Functions
numbers = np.array([1, 4, 9, 16, 25, 36])

sqrt = np.sqrt(numbers)

print(sqrt)

numbers2 = np.arange(1, 7) * 10
print(numbers2)

np_add = np.add(numbers, numbers2)

print(np_add)

np_multiply = np.multiply(numbers2, 5)
print(np_multiply)

numbers3 = numbers2.reshape(2, 3)
numbers4 = np.array([2, 4, 6])
np_multiply2 = np.multiply(numbers3, numbers4)

print(np_multiply2)



# Indexing and Slicing
grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])
# Select a single element (row and column given)
a = grades[0, 1]
print(a)

# select a single row
b = grades[1]
print(b)

# To select multiple sequential rows, use slice notation
# (upper limit is not included)
c = grades[0:2]
print(c)

# To select multiple non-sequential rows, use a list of row indices
d = grades[[1, 3]]
print(d)

# to get test1 for all students
e = grades[:, 0]
print(e)

# to get test1 and test3 for all students
f = grades[:, [0, 2]]
print(f)



#######################
num_rand = np.array(np.random.randint(60, 101, size=(1, 12)))
reshape_num = num_rand.reshape(3, 4)

print(num_rand)
print(reshape_num)

# average grades
avg_grades = reshape_num.mean()
print("Average of all test:", avg_grades)

# avergge each test
avg_test = reshape_num.mean(axis=0)
print("average of each test:", avg_test)

# avergge each student
avg_student = reshape_num.mean(axis=1)
print("averageg of each student:", avg_student)



# Shallow copies (view)
numbers = np.arange(1, 6)
print(numbers)
numbers2 = numbers.view()

numbers[1] *= 10
print(numbers2)

# Slice Views
numbers2 = numbers2[0:3]

numbers[1] *= 20
print(numbers2)

# Deep Copies
# The array method copy returns a new array object with a deep copy of the original array
numbers = np.arange(1, 6)
numbers2 = numbers.copy()

numbers[1] *= 10

print(numbers)
print(numbers2)


# Reshape and resize methods
# They both enable you to change an array's dimension.
# Reshape -- shallow copy
# Reszie -- deep copy

grades = np.array([[87, 96, 70], [100, 87, 90]])

a = grades.reshape(1, 6)
print(grades)
print(a)

b = grades.resize(1, 6)
print(grades)
print(b)

# flattened Method --- makes it into a one dimension -- creates a deep copy
flattened = grades.flatten()

# Ravel method -- creates a shallow copy
raveled = grades.ravel()

raveled[0] = 100
print(grades)

raveled[5] = 99
print(grades)

# Transpose the cols and rows
t = grades.T
print(t)

print(grades)

"""
# Horizontal Stacking
grades = np.array([[87, 96, 70], [100, 87, 90]])
grades2 = np.array([[94, 77, 90], [100, 81, 82]])

h_grades = np.hstack((grades, grades2)) -- Adds more cols
print(h_grades)

v_grades = np.vstack((grades, grades2)) --- adds more rows
print(v_grades)
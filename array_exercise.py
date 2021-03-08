## Numpy Exercise
import numpy as np

## Step 1: Create a 4x3 array of all 2s
print(
    "-----------------------------------------------   STEP ONE   -----------------------------------------------"
)

step1 = np.full((4, 3), 2)
print(step1)

print()

## Step 2: Create a 3x4 array with a range from 0 to 110 where each number increases by 10
print(
    "-----------------------------------------------   STEP TWO   -----------------------------------------------"
)
array1 = np.arange(0, 111, 10).reshape(3, 4)
print(array1)

print()

## Step 3: Change the layout of the above array to be 4x3, store it in a new array
print(
    "-----------------------------------------------   STEP THREE   -----------------------------------------------"
)

array2 = array1.reshape(4, 3)
print(array2)

print()

## Step 4: Multiply every elemnt of the above array by 3 and store the new values in a different array
print(
    "-----------------------------------------------   STEP FOUR   -----------------------------------------------"
)
array3 = array2 * 3

print(array3)

print()

## Step 5: Multiply your array from step one by your array from step 2
print(
    "-----------------------------------------------   STEP FIVE   -----------------------------------------------"
)

# array4 = step1 * array1.reshape(4, 3)
# print(array4)

## This errored out... why?
print()

## Step 6: Comment out your code from Step 5 and then multiply your array from step 1 by your array from step 3
print(
    "-----------------------------------------------   STEP SIX   -----------------------------------------------"
)

array6 = step1 * array2
print(array6)
## this worked! why?
print()

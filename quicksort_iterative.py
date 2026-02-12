'''

Name: Spriha Pokharel
Course: CS360 (Programming Languages)
Purpose: HW-01, Iterative implementation of the Quick Sort Algorithm.
Sources used: GeeksforGeeks (https://www.geeksforgeeks.org/python/python-program-for-iterative-quick-sort/),
W3 Schools (https://www.w3schools.com/python/python_arrays.asp), Pseudocode provided in assignment instructions.

'''

import random

# Partition Function
def partition(A, p, r):
    pivot = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    q = i + 1

    # Print result after each partition
    print(f"   After Partition, p, q, r, A: {p} {q} {r} {A}")
    return q


# Iterative implementation of Quicksort
def quicksort_iterative(A, p, r):

    # Create a stack
    size = r - p + 1
    stack = [0] * size
    top = -1

    # Push initial values of p and r to stack
    top += 1
    stack[top] = p
    top += 1
    stack[top] = r

    # Continue sorting until the stack is empty
    while top >= 0:

        # Pop r and p
        r = stack[top]
        top -= 1
        p = stack[top]
        top -= 1

        # Partition the array
        q = partition(A, p, r)

        # If there are numbers on the left, add that part to the stack
        if q - 1 > p:
            top += 1
            stack[top] = p
            top += 1
            stack[top] = q - 1

        # If there are numbers on the right, add that part to the stack
        if q + 1 < r:
            top += 1
            stack[top] = q + 1
            top += 1
            stack[top] = r


# Prompting user to enter the problem size
n = int(input("Enter problem size n: "))

# Generating a random array of numbers (based on problem size)
A = [random.randint(0, 9) for _ in range(n)]

# Print the final output
print("Initial array:", A)
quicksort_iterative(A, 0, len(A) - 1)
print("Sorted array: ", A)

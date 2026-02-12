'''

Name: Spriha Pokharel
Course: CS360 (Programming Languages)
Purpose: HW-01, Recursive implementation of the Quick Sort Algorithm.
Sources used: GeeksforGeeks (https://www.geeksforgeeks.org/dsa/python-program-for-quicksort/),
W3Schools (https://www.w3schools.com/python/python_dsa_quicksort.asp), W3 Schools (https://www.w3schools.com/python/python_arrays.asp),
Pseudocode provided in assignment instructions.

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

# Recursive implementation of Quicksort
def quicksort_recursive(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort_recursive(A, p, q - 1)
        quicksort_recursive(A, q + 1, r)

# Prompting user to enter the problem size
n = int(input("Enter problem size n: "))

# Generating a random array of numbers (based on problem size)
A = [random.randint(0, 9) for _ in range(n)]

# Print the final output
print("Initial array:", A)
quicksort_recursive(A, 0, len(A) - 1)
print("Sorted array: ", A)




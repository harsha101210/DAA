# code of binary search

import time
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# User Input
n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements in sorted order:")
for i in range(n):
    arr.append(int(input()))

target = int(input("Enter the element to search: "))

# Measure Execution Time
start_time = time.perf_counter()

result = binary_search(arr, target)

end_time = time.perf_counter()

# Output
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")

print("Execution Time:", end_time - start_time, "seconds")
print("Time Complexity: O(log n)")







# code of linear search
import time

# Linear Search Function
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# User Input
n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

target = int(input("Enter the element to search: "))

# Measure Execution Time
start_time = time.perf_counter()

result = linear_search(arr, target)

end_time = time.perf_counter()

# Output
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")

print("Execution Time:", end_time - start_time, "seconds")
print("Time Complexity: O(n)")

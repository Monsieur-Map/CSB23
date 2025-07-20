import random
import time

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Tạo mảng ngẫu nhiên
arr = random.sample(range(10000), 5000)  # Thay đổi kích thước để nhận xét
x = arr[random.randint(0, len(arr)-1)]   # Chọn phần tử có tồn tại

# Linear Search
start = time.time()
result_linear = linear_search(arr, x)
end = time.time()
print("Linear Search:", result_linear, "Time:", end - start)

# Binary Search
arr.sort()  # Sắp xếp mảng trước khi dùng binary search
start = time.time()
result_binary = binary_search(arr, x)
end = time.time()
print("Binary Search:", result_binary, "Time:", end - start)

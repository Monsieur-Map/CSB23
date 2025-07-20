import random
import time

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Tạo mảng ngẫu nhiên
arr = random.sample(range(10000), 500)  # Thử nghiệm với mảng lớn hơn để so sánh

# Insertion Sort
arr1 = arr.copy()
start = time.time()
insertion_sort(arr1)
end = time.time()
print("Insertion Sort Time:", end - start)

# Bubble Sort
arr2 = arr.copy()
start = time.time()
bubble_sort(arr2)
end = time.time()
print("Bubble Sort Time:", end - start)

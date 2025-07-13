# Toạ nguyên liệu ngẫu nhiên
import random
arr1 = random.sample(range(100), 10)
arr2 = random.sample(range(100), 10)

# Đếm số lần swap trong thuật toán Bubble sort
def bubble_sort(arr):
    #Biến count
    swapped_count = 0
    print(arr) #print thì không cần return nữa
    for i in range(len(arr)):
        swapped = False # Biến kiểm tra có thay đổ chỗ hay không
        for j in range(0, len(arr)-i -1):
            if arr[j] > arr[j+1]: # So sánh hai số liền kề
                #Swap
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped_count +=1
                print(f"Lần swap thứ {swapped_count:02} : {arr1}")
                swapped = True
        if not swapped:
            break
    # return arr, swapped_count  -> do print thì không cần return nx

#Test
bubble_sort(arr1)

#--------------------------------------------------------------------------------------------
#Đếm số lần chèn trong thuật toán Insertion
def insertion_sort(arr):
    # Duyệt quả từng phần tử -> tìm vị trí nhỏ nhất
    for index in range(1, len(arr)):
        insert_index = index
        current_value = arr.pop(index) #Không chỉ lấy giá trị cuối cùng mà còn lấy các giá trị dựa trên index (xoá phần tử tại index)
        print(arr, f"Cắt phần tử {current_value}")
        for j in range(index -1,-1, -1): # start, stop , step
            if arr[j] > current_value:
                insert_index = j
        arr.insert(insert_index, current_value) #Thêm phần tử vào vị trí mới
        print(f"Lần chèn {index:02}:{arr}")

#Test 2
arr2, = insertion_sort(arr2)
print("Arr đã sort: ", arr2)



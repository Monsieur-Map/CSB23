def binary_search_loop(arr, target): #Vòng lặp
    #Danh sách rỗng
    if not arr: return -1
    # Khởi tạo mid, start, end
    start, end = 0, len(arr) -1
    mid = (end - start) // 2 + start
    
    # Lặp từ start đến end
    while start <= end:
        # = 
        if arr[mid] == target:
            return mid
            # <
        if arr[mid] < target:
            start = mid +1
            # >
        else:
            end = mid -1
        # Cập nhật mid
        mid = (end - start) // 2 + start
    # Kết thức vòng while -> không tìm thấy
    return  -1
        

# input
try:
    n = int(input())
    if n <=0:
        raise ValueError("n must be a positive integer")
    arr = input().split(" ")
    if len(arr) != n:
        raise ValueError("The number of elements does not match n")
    #Yêu cầu danh sách số int
    arr = [int(x) for x in arr]
    target = int(input())
    
    # Thực thi thuật toán
    arr.sort()
    result = binary_search_loop(arr, target)
    print(result)
        
except Exception as e:
    print("Error: ", e)

finally:
    print("End")
    
# O(n^2)
# def sort_colors(colors):
    # do, move, xanh = 0, 0, len(nums) -1 #Move để di chuyển, biến gì đó...
    # while do <= xanh:
    #     if nums[move] == "r": #Đỏ
    #         # swapped
    #         nums[do], nums[move] = nums[move], nums[do]
    #         do +=1
    #         move +=1
            
    #     elif nums[move] == "w": #Trắng
    #         move +=1 #Thấy màu trắng thì skip vì trắng chắc chắn sau đỏ ròi:p
    #     else: # Đánh giá bạn xanh
    #         # Swapped lần nx X_X
    #         nums[move], nums[xanh] = nums[xanh], nums[move]
    #         xanh -= 1
    # return nums
# print(sort_colors(colors))
    
                 
def insertion_sort(arr):
    # Duyệt quả từng phần tử -> tìm vị trí nhỏ nhất
    for index in range(1, len(arr)):
        insert_index = index
        current_value = arr.pop(index) #Không chỉ lấy giá trị cuối cùng mà còn lấy các giá trị dựa trên index (xoá phần tử tại index)
        for j in range(index -1,-1, -1): # start, stop , step
            if arr[j] > current_value:
                insert_index = j
        arr.insert(insert_index, current_value) #Thêm phần tử vào vị trí mới
    return arr

#----------------------------------------------------------------------------
colors_code = {'r':1, 'w': 2, "b": 3} #Biến toàn cục -> ở dạng dictionary   |
#----------------------------------------------------------------------------

def convert_color_code(colors_arr): 
    global colors_code
    #Chuyển danh sách màu sắc -> sang dạng chữ 
    result = []
    for check in colors_arr:
        num = colors_code[check]
        result.append(num)
    # Check ngoại lệ -> danh sách ghi không dùng tên màu
    
    if len(result) != len(colors_arr):
        raise ValueError("Danh sách chứa tên màu không đúng quy định (r,w,b)")
    return result


def convert_color_char(color_num):
    global colors_code
    result = []
    for num in color_num:
        for key, value in colors_code.items():
            if value == num:
                result.append(key)
    
    #Ngoại lệ
    if len(result) != len(color_num):
        raise ValueError("Danh sách mã màu không đúng quy định (1,2,3)")
    
    return result


def test_drive():
    print("Start ---------------------------------------------------")
    # Tự nhập hàm vào (nhập một chuỗi string và cắt chuỗi string ra, thay vì hỏi độ dài)
    color_arr = input("Nhập danh sách (r,w,b), mỗi phần tử cách nhau một space :\n ")
    try:
        #Cắt chuỗi bởi mỗi space
        color_arr = color_arr.split(" ")
        #Convert color code
        color_code_list = convert_color_code(color_arr)
        # Sắp xếp
        sorted_color_code_list = insertion_sort(color_code_list)
        #Convert color code
        sorted_color_char_list = convert_color_char(sorted_color_code_list)
        #Print
        print(sorted_color_char_list)
    except Exception as e: #Ngoại lệ thì báo lỗi
        print("Error: ",e)
    finally:
        print("End---------------------------------------")
        
    

test_drive()
        
    
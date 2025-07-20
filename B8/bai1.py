

        

def giao_hop(nums1,nums2):
    if not nums1 or not nums2: return [] # Kiếm tra ngoại lệ
    
    ket_qua = [] #Danh sách chứa phần tử có ở cả 2 mảng
    diem_khong_giao = []
    
    if len(nums1) < len(nums2):
        for i in nums1:
            #Phần tử có trong nums2
            if i in nums2:
                # Phần tử chưa được cho vào danh sách
                if i not in ket_qua:
                    ket_qua.append(i)
    else:
        for i in nums2:
            if i in nums1 and i not in ket_qua:
                ket_qua.append(i)
    return ket_qua
    
    
    
    # for nums in nums1:
    #     if nums not in diem_khong_giao:
    #         diem_khong_giao.append(nums)
    #         for i in nums2_no_repeat:
    #             if i == nums:
    #                 ket_qua.append(nums)
    #     return ket_qua, diem_khong_giao

len_nums1 = int(input("Độ dài mảng 1: "))
nums1 = []
if len_nums1 > 0:
    for i in range(len_nums1):
       item = input(f"Phần tử thứ {i+1}:") 
       if item: nums1.append(item)
print(f"Mang 1 là: {set(nums1)}")        


len_nums2 = int(input("Độ dài mảng 2: "))
nums2 = []
if len_nums1 > 0:
    for i in range(len_nums1):
       item = input(f"Phần tử thứ {i+1}:") 
       if item: nums1.append(item)
print(f"Mang 1 là: {nums1}" )        

#So sánh -> in kết quả
if nums1 and nums2:
    dup = giao_hop(nums1=nums1,nums2=nums2)
    print(f"Danh sách phần tử có ở cả 2 mảng: {dup}") 
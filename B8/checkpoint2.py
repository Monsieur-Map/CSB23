len_nums1 = int(input("Độ dài mảng 1: "))
nums1 = []
if len_nums1 > 0:
    for i in range(len_nums1):
       item = input(f"Phần tử thứ {i+1}:") 
       if item: nums1.append(item)
print(f"Mang 1 là: {set(nums1)}")        


len_nums2 = int(input("Độ dài mảng 2: "))
nums2 = []
if len_nums2 > 0:
    for i in range(len_nums2):
       item = input(f"Phần tử thứ {i+1}:") 
       if item: nums2.append(item)
print(f"Mang 2 là: {nums2}" )   





class Gop:
    
    
    def __init__(self, nums1, nums2):
        if not nums1 and not nums2: 
            print("Cảnh báo cả 2 mảng đều rỗng")
        self.nums1 = nums1
        self.nums2 = nums2
        self.fusion = []
        
        
    #thêm vào mảng :Đ
    def merged(self):
        for i in self.nums1:
            self.fusion.append(i)
        
        for i in self.nums2:
            self.fusion.append(i)
        
    
        
    #Sort bong bóng
    def bubble_sort(self):
        for i in range(len(self.fusion)):
            swapped = False # Biến kiểm tra có thay đổ chỗ hay không
            for j in range(0, len(self.fusion)-i -1):
                if self.fusion[j] > self.fusion[j+1]: # So sánh hai số liền kề
                    #Swap
                    self.fusion[j], self.fusion[j+1] = self.fusion[j+1], self.fusion[j]
                    swapped = True
            if not swapped:
                break
        return self.fusion
    
    def ket_qua(self): #Hàm kết quả
        return self.fusion
    
     #Theo như cô dăn:)

#Sử dụng cờ class
ket_qua_gop_mang = Gop(nums1,nums2)
ket_qua_gop_mang.merged()
ket_qua_gop_mang.bubble_sort()
  

print("Kết quả sau khi gộp và sắp xếp là: ", ket_qua_gop_mang.ket_qua())
print("Độ phức tạp của chưng trình thì ở hàm merged thì độ khó là 0(2n) do có 2 for đi song song")
print("Độ phức tạp của chưng trình thì ở hàm bubble sort thì có độ khó là 0(n^2) do có for lồng for") 
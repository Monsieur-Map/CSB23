#SỬ DỤNG DOUBLE QUEUE
from collections import deque 

### XẾP HÀNG ĐỢI LẤY BÁNH -> ĐẾM SỐ NGƯỜI RỒI ĐỢI LẤY BÁNH ###
    
def count_students_unable_to_eat(sandwiches,students):   
    # Ép kiểu -> dequeue
    students = deque(students)
    sandwiches = deque(sandwiches)
    
    count = 0
    while students and sandwiches:
        #Lấy phần tử ở đầu 2 danh sách
        if students[0] == sandwiches[0]:
            students.popleft()
            sandwiches.popleft()
            count = 0
        else:
            #Nếu không trùng khớp -> đẩy student xuống cuối
            std = students.popleft()
            students.append(std)
            count+=1
            #Nếu xoay hết hàng của students mà không còn ai lấy được bánh nữa -> SÌ TÓP
            if count == len(students):
                break
            
    return len(students)

# --- Demo ---
print(count_students_unable_to_eat(students=[1,1,0,0], sandwiches=[0,1,0,1]))  # KQ: 0
print(count_students_unable_to_eat(students=[1,1,1,0,0,1,1,1,1,1], sandwiches=[1,0,0,0,1,1]))  # KQ: 3       

import queue

class Queue:
     #Khai báo
    def __init__(self):
        self.__queue = [] #Để dưới dạng private
        
    #Thêm phần tử (thêm ở cuối)
    def enqueue(self, new_item):
        self.__queue.append(new_item)
        
    #Xoá phần tử (Xoá ở đầu)
    def dequeue(self):
        if not self.is_empty():
            return self.__queue.pop(0)
    
    def is_empty(self):
        if len(self.__queue) == 0:
            return True
        else:
            return False
    @property
    def size(self):
        return int(len(self.__queue))
    
    @property
    def front(self):
        if not self.is_empty():
            return self.__queue[0] #Lấy về vị trí đầu tiên
    
    def __str__(self):
        return str(self.__queue) # ép kiểu list về kiểu string 


def hungry_students(students, sandwiches):
    if __name__ == "__main__":
        queue_for_students = Queue()
        for j in students:
            queue_for_students.enqueue(j)
            
        samdwiches_stack = sandwiches
        
        while not queue_for_students.is_empty():
            #Học sinh lấy bánh ở đầu hàng
            current_student = queue_for_students.front
            current_sandwich = samdwiches_stack[0]
            #Kiếm tra coi học sinh có thích bánh ko
        
            if current_student == current_sandwich:
               #Em này thích -> mất hàng chơ (dequeue)
               queue_for_students.dequeue()
               samdwiches_stack.pop(0) #Chồng trên cùng của sandwich bị lấy mất
               
        
            
   

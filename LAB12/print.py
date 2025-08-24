
import queue
import time
import threading
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Dùng thư viện queue
# Class printer: enqueue print job + dequeue print job


class Printer:
    def __init__(self):
        self.__print_list = queue.Queue()
        self.__pause_flag = threading.Event()
        self.__stop_flag = threading.Event()
        self.__worker = None

    def enqueue_print_job(self, job):
        self.__print_list.put(job)  # Put an item into queue

    def dequeue_print_job(self):
        if not self.__print_list.empty:
            return self.__print_list.get()  # Return or remove an item from queue
        return None
    
    #override
    def __str__(self):
        print("----Danh sách in-----")
        for index, value in enumerate(list(self.__print_list.queue)): #Phải chuyển về kiểu list thì mới thực hiện được khối lệnh
            print(f"{index}, {value}")
            
    def process_jobs(self):
        while not self.__print_list.empty():
            job = self.dequeue_print_job()
            print(f"Đăng in tác vụ: {job}")
            time.sleep(2) #Thời gian in cách nhau 2s

    # Hàm pause
    def __print_worker(self):
        while not self.__stop_flag.is_set():
            if self.__pause_flag.is_set():
                time.sleep(0.2)
                continue
            job = self.dequeue_print_job()
            if job:
                print(f"Đăng tác vụ")
                time.sleep(2)
            else:
                time.sleep(0.5) #Cho job mới
                
    def start(self):
        self.__stop_flag.clear()
        self.__pause_flag.clear()
        self.__worker = threading.Thread(target=self.__print_worker, daemon=True) #Tạoc cửa sổ để thực hiến tác vụ
        
    def pause(self):
        self.__pause_flag.set() #Cho nó tạm dừng
        print("|| Máy tạm dừng ......")
        
    def resume(self):
        self.__pause_flag.clear() #Cho nó tiếp tục
        print("|> Máy tin tiếp tục ...")
        
    def stop(self):
        self.__stop_flag.set()
        print("Máy in đã dừng!")
        
#Demo/test drive
if __name__ == "__main__":
    printer = Printer()
    printer.enqueue_print_job("Văn bản 1")
    printer.enqueue_print_job("Văn bản 2")
    printer.enqueue_print_job("Văn bản 3")
    
    printer.__str__()
    
    printer.start()
    
    #Pause 3s -> resume
    time.sleep(3)
    printer.pause()
    time.sleep(4)
    printer.resume()
    
    #Chạy thêm 4s -> tạm dừng
    time.sleep(4)
    printer.stop()
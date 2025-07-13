import time
def running_time(func):
        print("Bắt đầu chạy hàm --------------------------------------")
        start_time = time.time() #Lấy thời gian hiện tại
        result = func()
        end_time = time.time()
        print(f"Kết quả chạy hàm: {result}")
        print(f" Thời gian thực thi: {(end_time - start_time):.6f} giây")  
        print("Kết thúc chạy hàm ---------------------------")      
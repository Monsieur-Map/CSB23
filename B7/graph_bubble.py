import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

arr1 = random.sample(range(100),10)

def bubble_sort_steps(arr):
    #Tạo danh sách arr sau mỗi lần lặp
    steps= []
    print("Arr chưa sort: ", arr)
    for i in range(len(arr)):
        swapped = False # Biến kiểm tra có thay đổ chỗ hay không
        for j in range(0, len(arr)-i -1):
            if arr[j] > arr[j+1]: # So sánh hai số liền kề
                #Swap
                arr[j], arr[j+1] = arr[j+1], arr[j]
                steps.append(arr.copy())
                swapped = True
        if not swapped:
            break
    return steps

def visualize_sort_bubble(arr):
    steps = bubble_sort_steps(arr)
    
    #Khai báo các thông số vẽ đồ thị
    fig, ax = plt.subplots()
    ax.set_title("Step by step bubble sort")
    #Vẽ cột
    bar_rects = ax.bar(range(len(arr)), arr,align="edge", color="green")
    #Kích thước của cột
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, max(arr) + 5) 
    text = ax.text(0.02,0.95, "", transform =  ax.transAxes)
    
    #hàm cập nhật đồ thị sau mỗi lần swap
    def update_bars(frame):
        for rect, val in zip(bar_rects, steps[frame]):
            #Chiều cao của cột
            rect.set_height(val)
        text.set_text(f"Step {(frame + 1):02}/ {len(steps)}")
        return bar_rects
    
    #Tạo animation
    ani = animation.FuncAnimation(fig, update_bars, frames=len(steps),  interval=1000, repeat=False)
    # Hiện thị đồ thị
    plt.show()
    
#Test
visualize_sort_bubble(arr1)
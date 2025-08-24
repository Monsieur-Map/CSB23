# MP3 player: add song, play song, skip song
class MP3Player:
    def __init__(self):
        self.music_queue = []
        self.current_song = None
        
    def add_song(self,song:str): # Ép kiểu dữ liệu cho string
        # Thêm bài mới (vào cuối danh sách)
        self.music_queue.append(song)
        print(f"Đã thêm bài hát: {song}")
        
    def play_song(self):
        if len(self.music_queue):
            # Lấy phần tử đầu danh sách
            self.current_song = self.music_queue.pop[0]
            print(f"Bài hát đang phát: {self.current_song}")
        else:
            self.current_song = None
            print("Danh sách bài hát đang trống!")
            
    def skip_song(self):
        if self.current_song:
            print(f"Bỏ qua bài hát: {self.current_song}")
            #Phát tiếp bài tiếp theo
            self.play_song
       
        else:
            print("Không có bài hát nào đang phát để bỏ qua.")
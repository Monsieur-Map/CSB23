import time
import threading


class MP3Player:
    def __init__(self):
        self.music_queue = []
        self.current_song = None
        self.is_playing = False
        self.skip_flag = False
        self.thread = None

    def add_song(self, song):
        self.music_queue.append(song)

    def _play_loop(self):
        """Luồng chạy phát nhạc tự động"""
        self.is_playing = True
        while self.music_queue and self.is_playing:
            self.current_song = self.music_queue.pop(0)
            print(f"🎵 Đang phát: {self.current_song}")
            # Mỗi bài hát "nghe" trong 3 giây
            for i in range(3):
                if self.skip_flag:
                    self.skip_flag = False
                    break
                time.sleep(1)
            if self.skip_flag:
                print(f"⏭ Đã bỏ qua: {self.current_song}")
                self.skip_flag = False
                continue
            print(f"✅ Phát xong: {self.current_song}")

        self.is_playing = False
        self.current_song = None
        print("📭 Hết nhạc trong danh sách.")

    def play_song(self):
        """Bắt đầu phát nhạc (nếu chưa phát)"""
        if not self.is_playing and self.music_queue:
            self.thread = threading.Thread(target=self._play_loop, daemon=True)
            self.thread.start()
        elif self.is_playing:
            print("⏳ Nhạc đang phát rồi...")
        else:
            print("❌ Không có bài hát nào trong danh sách.")

    def skip_song(self):
        """Đặt cờ bỏ qua bài hát hiện tại"""
        if self.is_playing and self.current_song:
            self.skip_flag = True
        else:
            print("❌ Không có bài hát nào để bỏ qua.")

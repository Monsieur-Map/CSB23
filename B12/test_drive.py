from play_song import MP3Player

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"


def test_drive():
    mp3 = MP3Player()
    print(BLUE + "----------- Trình phát nhạc -----------" + RESET)

    song_list_len = 0
    while song_list_len == 0:
        try:
            song_list_len = int(input("Số lượng bài hát: "))
        except Exception as e:
            print(RED + "Lỗi: " + str(e) + RESET)
            song_list_len = 0

    for i in range(song_list_len):
        song = ""
        while len(song) == 0:
            song = input("Nhập tên bài hát {}: ".format(i + 1)).strip()
        mp3.add_song(song)

    print(BLUE + "----------- Danh sách bài hát -----------" + RESET)
    for index, value in enumerate(mp3.music_queue):
        print("{}. {}".format(index + 1, value))

    choices = """ LỰA CHỌN:
        1. Phát nhạc
        2. Bỏ qua bài hát hiện tại
        3. exit
    """
    choose = 0
    while choose != 3:
        print(BLUE + choices + RESET)
        try:
            choose = int(input())
        except Exception as e:
            print(RED + "Lỗi: " + str(e) + RESET)
            choose = 0

        match choose:
            case 1:
                mp3.play_song()
            case 2:
                mp3.skip_song()
            case 3:
                print(
                    BLUE
                    + "----------- Cảm ơn bạn đã sử dụng chương trình! -----------"
                    + RESET
                )
                break
            case _:
                print(RED + "Lỗi: Lựa chọn không hợp lệ!" + RESET)


if __name__ == "__main__":
    test_drive()

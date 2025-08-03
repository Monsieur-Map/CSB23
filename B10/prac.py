import string
# Đếm số lần từ xuất hiện trong 1 đoạn văn bản (Word Counter)
def count_words (paragraph):
    # Thay đổi thành chữ thường
    paragraph = paragraph.lower()
    
    # Lược bỏ các dấu câu (".", ",", "!",...)  
    for char in string.punctuation:
        paragraph = paragraph.replace(char, '')
        
    # Tách từ
    words = paragraph.split()
    
    # Đếm tần suất
    word_count = {} #Dict
    for word  in words:
        if word in word_count:
            word_count[word] += 1 # Cộng một lần đếm
        else:
            word_count[word] =1 # Đếm một lần
            
    return word_count

p = """"
But what kind of cat will they become? One possibility is that the cats of the future will be larger than today’s felines. 

Continued contact with humans may also help cats grow friendlier. By nature, cats tend to be more solitary and standoffish than dogs, which have a long evolutionary history as pack animals rather than lone hunters. Ongoing contact with humans may have helped give friendlier cats a survival advantage, making them more likely to pass on more sociable genes to their offspring.

Over time, this might have helped create a more relaxed pet—without ruining one of the most endearing parts of living with a cat: that when your kitty cuddles, you know it’s for real.

When scientists compared the social behaviors and personalities of domestic cats with clouded leopards, snow leopards, African lions, and Scottish wildcats, they found that house cats weren’t exactly suited for group living. They tended to be domineering, neurotic, and impulsive—not exactly the traits you want in a friend.

However, the personalities of house cats were most like those of the more sociable African lion, which has figured out a way to live in groups. This suggests that cats have the raw material to adapt to a more sociable future. And though large cat colonies may not be the same as lion prides, lions do show that cats can live side by side when the circumstances are right.
"""
result = count_words(paragraph=p)
# Hiển thị danh sách theo thứ tự chữ cái
max = 0
word_count_max = ""

for word, counter in sorted(result.items()):
    print(f"{word}: {counter}")
    if counter > max:
        max = counter
        word_count_max =  word
    
print(f"Từ với số lần lặp nhiều nhất: {word_count_max}, lặp {max} lần")
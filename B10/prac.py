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
For starters, orange cats are not a breed, like British shorthair or Siamese. Cats of many breeds, from Maine coons and munchkins to American bobtails and Siberians, can have orange colorations. Which perhaps makes it all the weirder that orange cat aficionados claim that orange cat behaviors transcend breed.
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
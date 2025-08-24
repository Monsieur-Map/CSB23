def is_valid_parentheses(s:str):
    danhsach_ngoac = {")": "(", "}" : "{", "]" : "["} #Dạng dictionary
    mongoac = "({["
    stack_luu_mo_ngoac = []
    
    for ch in s:
        #Kiếm tra mở ngoặc
        if ch in mongoac:
            stack_luu_mo_ngoac.append(ch)
            
        else:
            # Kiểm tra ngoặc đóng
            if not stack_luu_mo_ngoac or stack_luu_mo_ngoac[-1] != danhsach_ngoac.get(ch,None):
                return False
            #Nếu có ngoặc đóng -> Xoá ngoặc mở
            stack_luu_mo_ngoac.pop()
            
        #Nếu danh sách ngoặc mở được xoá hết
    return len(stack_luu_mo_ngoac) == 0
    

if __name__ == "__main__":
    s = input("Chuỗi biểu thức: ").strip()
    print(f"Biểu thức đúng? {is_valid_parentheses(s)}")
    
import csv # Giúp xử lý dữ liệu thành dạng tuple
import sys
sys.stdout.reconfigure(encoding='utf-8')

def process_csv(file_path): #Def sử lý csv
    name_counts = {}
    unique_email = set()
    company_counts = {}
    
    
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file) 
        #Cắt từng dòng
        for row in reader:
            #Kiểm tra số lượng cột
            if len(row) != 3:
                continue #Bỏ qua nếu sai định dạng
            name, company ,email= row
            
            #Xoá khoảng trắng (whitespace removed)
            email = email.strip()
            company = company.strip()
            name = name.strip()
            
            #Kiểm tra sự tồn tại của email
            if email not in unique_email:
                unique_email.add(email)
                #Cập nhật số lượng đại biểu của công ty
                if company in company_counts:
                    company_counts[company] +=1
                else:
                    company_counts[company] =1
                    
            if email not in unique_email:
                unique_email.add(email)
                if name in name_counts:
                    name_counts[name] += 1
                else:
                    name_counts[name] =1
                    
                
                    
            
                    
        # Sắp xép công ty theo số lượng đại biểu giảm dần:
        sorted_companies = sorted( # Nêus nếu có varable.sort() không có sorted
            company_counts.items(), key=(lambda item: item[1]), reverse = True
            ) 
        
        sorted_names = sorted(
            name_counts.items(), key=(lambda item: item[0]), reverse= True
        )
        
        # In kết quả
        print(f"Số lượng đại biểu dự kiến tham dự: {len(unique_email)}")
        print("Danh sách công ty và số lượng đại biểu: ")
        for company, count in sorted_companies:
            print(f"{company}:{count}")
        print("Danh sách tên những người tham gia: ")
        for name, count in sorted_names:
            print(f"{name}: {name_counts}")
            
process_csv("LAB10/data.csv")
            
                
                        
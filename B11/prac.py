# Đề: tạo chức năng forward, backward cho web browser
# Gợi ý: sử dụng 2 stack để lưu
# Lớp Browser: visit_page, back, foward

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"  # Resets the color to default


class Browser:
    def __init__(self):
        self.current_page = "home"
        self.backward_page = []
        self.forward_page = []

    def visit_page(self, url):
        # Lưu trang hiện tại vào back
        self.backward_page.append(self.current_page)
        # Thay dổi trang hiện tại
        self.current_page = url
        # Xoá trang trong forward
        self.forward_page.clear()
        #Trở lại trang hiện tại
        
        return f"Visited: {self.current_page}"

    def back(self):
        if len(self.backward_page) == 0:
            return "No back history"

        # lưu trang hiện tại vào forward
        self.forward_page.append(self.current_page)
        # Quay lại trang trước
        self.current_page = self.backward_page.pop()
        return f"Trang hiện tại của bạn là: {self.current_page}"

    def forward(self):
        if len(self.forward_page) == 0:
            return "No forward history"

        # Lưu trang hiện tại vào back
        self.backward_page.append(self.current_page)
        # Quay lại trang sau
        self.current_page = self.forward_page.pop()
        return f"Trang hiện tại của bạn là: {self.current_page}"


def testdrive():
    # Tạo obj browser
    browser = Browser()
    function_table = """ Use number 1,2,3 for functions:
        1. Visit page -> input page name
        2. <- Back
        3. -> Forward
    """
    request = ""
    while request != "4":
        # Hiển thị agenda chức năng
        print(function_table)
        # Cho user nhập theo yêu cầu
        request = input(f"{GREEN}Enter your choice: {RESET} ").strip()
        match request:
            case "1":
                page_name = input(
                    f"{BLUE}Enter page name: {RESET} "
                ).strip()  # Xoá khoảng trắng
                # Không điền trang
                if not page_name:
                    print(f"{RED}Page name cannot be empty {RESET}")
                    # Quay lại vòng lặp
                    continue
                # page name đúng yêu cầu
                print(GREEN + browser.visit_page(page_name) + RESET)

            case "2":
                print(GREEN + browser.back() + RESET)

            case "3":
                print(GREEN + browser.forward() + RESET)
            case "4":
                print(f"{RED}Exiting program. Goodbye!{RESET}")

            case _:
                print("Please try again")
            ###### KHÔNG BREAK THÌ SẼ HIỂU NGẦM VÀ PHÁ VÒNG LẶP TRONG KHI MÌNH VẪN MUỐN Ở TRONG VÒNG LẶP ĐỂ LÀM GÌ ĐÓ

        # Xoá request cũ
        request = ""


testdrive()

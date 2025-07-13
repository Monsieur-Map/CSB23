class TaiKhoan:
    def __init__(self, stk, ten, so_du):
        self.stk = stk
        self.ten = ten
        self.so_du = so_du

    def rut_tien(self, so_tien):
        if so_tien > self.so_du:
            print(f"[{self.ten}] Không đủ số dư để rút {so_tien} VNĐ.")
        else:
            self.so_du -= so_tien
            print(f"[{self.ten}] Rút {so_tien} VNĐ. Số dư còn lại: {self.so_du} VNĐ.")

    def nap_tien(self, so_tien):
        self.so_du += so_tien
        print(f"[{self.ten}] Nạp {so_tien} VNĐ. Số dư mới: {self.so_du} VNĐ.")

    def lay_so_du(self):
        return self.so_du


class TaiKhoanTietKiem(TaiKhoan):
    def __init__(self, stk, ten, so_du, lai_suat):
        super().__init__(stk, ten, so_du)
        self.lai_suat = lai_suat

    def tinh_lai(self, thang):
        tien_lai = self.so_du * self.lai_suat * thang / 12
        print(f"[{self.ten}] Lãi sau {thang} tháng là: {tien_lai} VNĐ.")
        return tien_lai


# Hàm main thực hiện yêu cầu
def main():
    # Tài khoản chính
    tk1 = TaiKhoan("111111", "Nguyen Van A", 3000000)
    tk1.nap_tien(1000000)
    tk1.rut_tien(500000)
    print(f"[{tk1.ten}] Số dư cuối cùng: {tk1.lay_so_du()} VNĐ\n")

    # Tài khoản tiết kiệm
    tk2 = TaiKhoanTietKiem("222222", "Le Thi B", 8000000, 0.06)
    tk2.nap_tien(2000000)
    tk2.rut_tien(1000000)
    lai = tk2.tinh_lai(6)  # Lãi 6 tháng
    tk2.so_du += lai  # Cộng lãi vào số dư
    print(f"[{tk2.ten}] Số dư cuối cùng sau cộng lãi: {tk2.lay_so_du()} VNĐ")


# Gọi hàm main
main()

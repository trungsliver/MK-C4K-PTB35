# Quy tắc đặt tên file: [TenLop]_[HoTen]_CP1.py
# VD: PTB35_BuiDucTrung_CP1.py

# Trắc nghiệm
# 1B 2C 3C 4B 5A 6A 7B 8B 9D 10A

# Tự luận
# Nhập số diện bạn sử dụng
# kwh = float(input("Nhập số điện sử dụng (kWh): "))

# # Khai báo biến tiền điện
# cash = 0

# # Tính tiền điện 
# if 0 <= kwh <= 50:
#     cash = kwh * 1.7
# elif 50 < kwh <= 100:
#     cash = 50 * 1.7 + (kwh - 50) * 1.9
# elif 100 < kwh <= 200:
#     cash = 50 * 1.7 + 50 * 1.9 + (kwh - 100) * 2.1
# elif kwh > 200:
#     cash = 50 * 1.7 + 50 * 1.9 + 100 * 2.1 + (kwh - 200) * 3
# else:
#     print("Số điện không hợp lệ")

# # Hiển thị kết quả
# print(f"Số tiền điện phải trả: {cash} nghìn VND")

# Link đề bài: shorturl.at/q0TIJ

# Hạn nộp: 15h15

# ============= CHỮA BTVN ===============
# Câu 1: Nhập một số từ bàn phím và in ra số đó.
num = input("Nhập một số: ")
print("Số bạn vừa nhập là:", num)

# Câu 2: Viết chương trình kiểm tra nhập vào 1 số và kiểm tra số đó là chẵn hay lẻ.
num = int(input("Nhập một số nguyên: "))
if num % 2 == 0:
    print(f"Số {num} là số chẵn.")
else:
    print(f"Số {num} là số lẻ.")

# Câu 3: Viết chương trình tính tổng, hiệu, tích, thương của hai số nhập từ bàn phím.
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
print(f"Tổng: {a + b}")
print(f"Hiệu: {a - b}") 
print(f"Tích: {a * b}")
if b != 0:
    print(f"Thương: {a / b}")
else:
    print("Không thể chia cho 0.")

# Câu 4: Viết chương trình chuyển đổi từ USD sang VND (số tiền được nhập từ bàn phím).
usd = float(input("Nhập số tiền (USD): "))
if usd <= 0:
    print("Số tiền không hợp lệ.")
else:
    vnd = usd * 27000
    print(f"Số tiền sau khi chuyển đổi: {vnd} VND")

# Câu 5: Viết chương trình nhập số điểm của 3 bạn học sinh, in ra màn hình bạn có điểm thấp nhất và bạn có điểm cao nhất.
danh = float(input("Nhập điểm của bạn Đức Anh: "))
hoang = float(input("Nhập điểm của bạn Hoàng: "))
minh = float(input("Nhập điểm của bạn Minh: "))

if danh == hoang and hoang == minh:
    print("Ba bạn có điểm bằng nhau.")
elif danh >= hoang and danh >= minh:
    print(f"Bạn có điểm cao nhất là: Đức Anh với {danh} điểm.")
elif hoang >= minh and hoang >= danh:
    print(f"Bạn có điểm cao nhất là: Hoàng với {hoang} điểm.")
elif minh >= danh and minh >= hoang:
    print(f"Bạn có điểm cao nhất là: Minh với {minh} điểm.")
else: 
    print("Dữ liệu không hợp lệ.")    

# ============= Kết quả CP1 ===============
# Vũ Hoàng: 8
# Minh Tùng: 7.5
# Nhật Minh: 8.5
# Đức Anh: 8
# Hoàng Anh: 8
# Nguyên Vũ: 9

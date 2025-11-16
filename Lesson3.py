# Data Types - Kiểu dữ liệu
    # String: chuối ký tự - xâu ký tự
name = "Duc Anh"
    # int (integer): số nguyên
age = 100
    # float: số thực
score = 0.1
    # boolean: logic True/False - Đúng/Sai
male = True

# Toán tử số học
    # Cơ bản: + - * /
print(" 7 / 2 =", 7 / 2)      # Kết quả: 3.5
    # Chia lấy nguyên: //
print(" 7 // 2 =", 7 // 2)    # Kết quả: 3
    # Chia lấy dư: %
print(" 7 % 2 =", 7 % 2)      # Kết quả: 1
    # Lũy thừa: **
print(" 7 ** 2 =", 7 ** 2)    # Kết quả: 49

# Toán tử số học với string
    # Cộng chuỗi: +
print("hello " + "Vu Hoang")
    # Phép lặp lại: *
print('hi' * 3)
print("Hoang Anh" * 0)

# Toán tử quan hệ (phép so sánh) => True/False
    # So sánh bằng: ==
print("7 == 2 :", 7 == 2)    # Kết quả: False
    # So sánh khác: !=
print("7 != 2 :", 7 != 2)    # Kết quả: True
    # So sánh lớn/nhỏ hơn: >, <, >=, <=
print("5 >= 5 :", 5 >= 5)           # Output: True
print("5 < 3 :", 5 < 3)            # Output: False

# Toán tử logic: and, or, not
    # Ví dụ: trà sữa - gà rán

# Câu điều kiện
    # Dạng thiếu
age = 2
if age >= 18:
    print('Bạn đã đủ 18 tuổi')    

    # Dạng đủ:
number = 99
if number % 2 == 0:
    print(number, "là số chẵn")
else:
    print(number, "là số lẻ")

    # Dạng đa nhánh:
score = 9
if 8 <= score <= 10:
    print("Học lực: giỏi")
elif 6.5 <= score < 8:
    print("Học lực: khá")
elif 5 <= score < 6.5:
    print("Học lực: trung bình")
elif 0 <= score < 5:
    print("Học lực: yếu")
else:
    print("Điểm không hợp lệ")

# ============== LUYỆN TẬP ==============
# Bài 1: Viết chương trình nhập vào một số nguyên n, 
# kiểm tra số đó có chia hết cho 5 hay không và in kết quả ra màn hình
n = int(input("Nhập vào một số nguyên n: "))
if n % 5 == 0:
    print(n, "chia hết cho 5")
else:
    print(n, "không chia hết cho 5")

# Bài 2: Nhập điểm số của bạn từ bàn phím.
# Yêu cầu: Xếp loại học lực học sinh. Biết rằng:
    # [8, 10]: Giỏi, [6.5, 8): Khá, [5, 6.5): TB, [0, 5): Yếu
score = float(input("Nhập điểm số của bạn: "))
if score > 10 or score < 0:
    print("Điểm không hợp lệ")
else:
    if score >= 8:
        print("Học lực: giỏi")
    elif score >= 6.5:
        print("Học lực: khá")
    elif score >= 5:
        print("Học lực: trung bình")
    else:
        print("Học lực: yếu")
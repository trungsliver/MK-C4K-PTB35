# Vòng lặp vô han - Vòng lặp while

# Hiện ra các số nguyên từ 0 đến 5
    # Vòng lặp for
for i in range(6):
    print(i)

    # Vòng lăp while
i = 0
while i < 6:
    print(i)
    # Tăng i lên 1 đơn vị
    i = i + 1   # i += 1

# Ví dụ: Nhập số nguyên n trong khoảng [0, 100]
# Nếu nhập sai (n<0 hoặc n>100) thì yêu cầu nhập lại

n = int(input("Nhập số nguyên n trong khoảng [0, 100]: "))

while n < 0 or n > 100:
    print("Số bạn nhập không hợp lệ. Vui lòng nhập lại.")
    n = int(input("\nNhập số nguyên n trong khoảng [0, 100]: "))

print("Bạn đã nhập số hợp lệ:", n)

#  Đề bài: Tạo Mysterious Game
    # Yêu cầu: tạo ra 1 số đặc biệt để đoán (random)
    # Người chơi cần nhập đến khi nào đoán đúng số đặc biệt thì dừng game

import random
number = random.randint(1, 100)  # Tạo số đặc biệt trong khoảng [1, 100]
print('Số bí mật:', number)
# Đếm số lần đoán
count = 1
# Nhập số đoán đầu tiên
n = int(input("Nhập dự đoán của bạn [0, 100]: "))

while n != number:
    if n > number:
        print("Số bạn đoán lớn hơn số bí mật.")
    if n < number:
        print("Số bạn đoán nhỏ hơn số bí mật.")

    count += 1
    n = int(input("\nNhập dự đoán của bạn [0, 100]: "))

print(f"Bạn đã trả lời đúng sau {count} lần đoán.")
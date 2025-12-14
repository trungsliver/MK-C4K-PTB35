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
    # Tăng số lần đoán lên 1
    count += 1
    n = int(input("\nNhập dự đoán của bạn [0, 100]: "))

print(f"Bạn đã trả lời đúng sau {count} lần đoán.")

# ==================== ÔN TẬP VÒNG LẶP FOR =====================
# Dạng 1: In / Hiển thị ra màn hình
    # 1.1. In ra màn hình các số từ 0 đến n
n = int(input("Nhập số nguyên dương n: "))
for i in range(n+1):
    print(i)

    # 1.2. In ra màn hình các số nguyên trong khoảng [a, b]
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
for i in range(a, b+1):
    print(i)

    # 1.3. In ra màn hình các số chẵn trong khoảng [a, b]
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
for i in range(a, b+1):
    if i % 2 == 0:
        print(i)

    # 1.4. In ra màn hình các số lẻ trong khoảng [a, b]
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
for i in range(a, b+1):
    if i % 2 != 0:
        print(i)

# Dạng 2: Tính tổng
    # 2.1. Tính tổng các số trong khoảng [a, b]
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
total = 0
for i in range(a, b+1):
    # Cộng từng số i vào total
    total += i      # total = total + i
print(f"Tổng các số trong khoảng [{a}, {b}] là: {total}")

    # 2.2. Tính tổng các số chẵn trong khoảng [a, b]
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
total = 0
for i in range(a, b+1):
    if i % 2 == 0:
        total += i
print(f"Tổng các số chẵn trong khoảng [{a}, {b}] là: {total}")

    # 2.3. Tính tổng các số lẻ trong khoảng [a, b]
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
total = 0
for i in range(a, b+1):
    if i % 2 != 0:
        total += i
print(f"Tổng các số lẻ trong khoảng [{a}, {b}] là: {total}")

# Dạng 3: Đếm số lượng
    # 3.1. Đếm số lượng số chia hết cho 5 trong khoảng [a, b]
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
count = 0
for i in range(a, b+1):
    if i % 5 == 0:
        count += 1
print(f"Số lượng số chia hết cho 5 trong khoảng [{a}, {b}] là: {count}")

    # 3.2. Đếm số lượng số âm trong khoảng [a, b]
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
count = 0
for i in range(a, b+1):
    if i < 0:
        count += 1
print(f"Số lượng số âm trong khoảng [{a}, {b}] là: {count}")
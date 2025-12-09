# Vòng lặp hữu han- Vòng lặp for

# Cú pháp đầy đủ: range(start, stop, step)
    # start: giá trị bắt đầu, không bắt buộc, mặc định là 0
    # stop: giá trị kết thúc, bắt buộc
    # step: bước nhảy, không bắt buộc, mặc định là 1
# Lưu ý: chạy từ start đến stop-1

# TH1: range(start, stop, step)
# for i in range(1, 10, 3):
#     print(i)
#     print("Hoàng Anh")

# TH2: range(start, stop)
# for i in range(50, 60):
#     print(i, end=" ")

# TH3: range(stop)
# for i in range(5): # giống range(0, -5, 1)
#     print(i)

# Ví dụ:
# range(5,10): 5 -> 9
# range(2, 10, 2): 2,4,6,8
# range(-5): không chạy
# range(-10, -5): -10, -9, -8, -7, -6
# range(1): 0
# range(2,8,3): 2, 5
# range(2): 0, 1
# range(-5, 2): -5 , -4, -3, -2, -1, 0, 1

# ============== LUYỆN TẬP ==============
# Bài 1: Nhập 2 số nguyên a và b từ bàn phím.
# In ra các số nguyên trong khoảng [a, b]
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
print(f"Các số nguyên trong khoảng [{a}, {b}]: ")
for i in range(a, b + 1):
    print(i, end=" ")

# Bài 2: Nhập 2 số nguyên a và b từ bàn phím.
# In ra các số nguyên trong khoảng [a, b] nếu b >= a
# In ra các số nguyên trong khoảng [b, a] nếu a > b
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

if b >= a:
    print(f"Các số nguyên trong khoảng [{a}, {b}]: ")
    for i in range(a, b + 1):
        print(i, end=" ")
else:
    print(f"Các số nguyên trong khoảng [{b}, {a}]: ")
    for i in range(b, a + 1):
        print(i, end=" ")

# Bài 3: Nhập 1 số nguyên a trong khoảng [1, 10]
# In ra màn hình bảng cửu chương a
a = int(input('\nNhập a: '))
print(f'Bảng cửu chương {a}:')
for i in range(1, 11):
    print(f'{a} x {i} = {a * i}')

# Bài 4: In ra màn hình bảng cửu chương từ 2 => 9
for a in range(2, 10):
    print(f'Bảng cửu chương {a}:')
    for i in range(1, 11):
        print(f'{a} x {i} = {a * i}')
    print()  # In dòng trống giữa các bảng cửu chương
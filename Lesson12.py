# Hàm - Chương trình con

# Hàm không có giá trị trả về
def say_hello():
    print("Hello Khiêm")
    print("Hello Bảo Hoàng")

    # gọi hàm khi cần sử dụng
say_hello()

# Hàm có dữ liệu đầu vào (tham số)
def hello2(name):
    print("Hello ", name)

hello2('Minh Trí')
hello2('Mai Hoàng Minh')

# Hàm có giá trị trả về (sử dụng được như 1 biến)
def dtic_HCN(a:float, b:float):
    return a * b
    # Gọi hàm và lưu kết quả vào biến
print('Kết quả:', dtic_HCN(5,10))

# Ví dụ:
def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(check_even(20))
print(check_even(21))

# ================== LUYỆN TẬP =======================
# Bài 1: Viết một hàm sum_odd(numbers) để tính tổng các số lẻ trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về tổng các số lẻ trong danh sách đó.
numbers = [10, 5, 1, 2, 6, 4, 9, 3, 7, 8]
def sum_odd(arr):
    sum = 0                 # Khai báo biến lưu tổng
    for item in arr:        # Duyệt danh sách, cách 2 - chỉ có giá trị
        if item % 2 != 0:   # Kiểm tra số lẻ
            sum += item     # Cộng giá trị phần tử vào biến sum
    return sum              # Trả về giá trị sum khi duyệt xong vòng lặp
print('Tổng số lẻ trong danh sách:', sum_odd(numbers))

# Bài 2: Viết một hàm is_prime(n) để kiểm tra xem một số nguyên dương n có phải là số nguyên tố hay không.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về True nếu n là số nguyên tố, ngược lại trả về False.
def is_prime(n:int):
    count = 0                   # Khai báo biến đếm 
    for i in range(1, n + 1):   # Duyệt số từ 1 đến n
        if n % i == 0:          # Kiểm tra n có chia hết cho i không
            count += 1          # Chia hết thì tăng count thêm 1
    if count == 2:              # count = 2 thì n là số nguyên tố
        return True             # Trả về True
    else:                       # count != 2 thì n không phải số nguyên tố
        return False            # Trả về False

print('7:', is_prime(7))  # True
print('8:',is_prime(8))  # False

# Bài 3: Viết một hàm count_words(s) để đếm số lượng từ trong một chuỗi s.
# 	YC1: Hàm nhận vào một chuỗi ký tự s.
# 	YC2: Hàm trả về số lượng từ trong chuỗi đó.
str1 = 'Khiêm thích mặc quần hoa'
def count_words(s:str):
    # strip(): xóa khoảng trắng ở đầu và cuối chuỗi
    # split(): tách chuỗi và lưu các phần tử đc tách vào danh sách
    arr = s.strip().split()     # Chuyển chuỗi thành danh sách từ
    return len(arr)             # Kích thước danh sách = số lượng từ
print('Số lượng từ trong chuỗi:', count_words(str1))


# Bài 4: Viết một hàm sum_of_digits(n) để tính tổng các chữ số của một số nguyên dương n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về tổng các chữ số của n.
def sum_of_digits(n:int):
    sum = 0
    while n > 0:              # Duyệt số n cho đến khi n = 0
        sum = sum + n%10      # Lấy hàng đơn vị của n
        n = n // 10           # Loại bỏ hàng đơn vị của n
    return sum
print('Tổng các chữ số của 12345:', sum_of_digits(12345))

# Bài 5: Viết một hàm find_max(numbers) để tìm vị trí số lớn nhất trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về vị trí số lớn nhất trong danh sách đó.
numbers = [10, 5, 1, 2, 6, 4, 9, 3, 7, 8]

def find_max(arr):
    max_value = max(arr)        # Tìm giá trị lớn nhất của danh sách
    for i in range(len(arr)):   # Duyệt danh sách, cách 1 - có index
        if arr[i] == max_value: # Tìm vị trí của max_value
            return i            # Trả về vị trí
print('Vị trí phần tử lớn nhất:', find_max(numbers))

# Bài 6: Viết một hàm sum_to_n(n) để tính tổng các số từ 1 đến n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	Yc2: Hàm trả về tổng các số từ 1 đến n.
def sum_to_n(n:int):
    sum = 0
    for i in range(1, n+1):  # Duyệt số từ 1 đến n
        sum = sum + i        # Tính tổng các số từ 1 đến n
    return sum
print('Tổng các số từ 1 đến 10:', sum_to_n(10))

# Ôn tập:
# Bài 1: Nhập vào từ bàn phím các thông tin các nhân: 
    # Họ tên, Tuổi, Trường học, giới tính, điểm trung bình.
    # In ra màn hình các thông tin vừa nhập

# Bài 2: Nhập vào chiều dài và chiều rộng hình chữ nhật
    # In ra màn hình chu vi và diện tích hình chữ nhật đó.

# Bài 3: Nhập số nguyên n từ bàn phím.
    # Kiểm tra xem n có phải là số chẵn hay không.

# Bài 4: Nhập điểm số từ bàn phím. Hãy in ra mà hình xếp hạng học lực, biết rằng:
    # 8-10: Giỏi, 6.5-8: Khá, 5-6.5: Trung Bình, 0-5: Yếu

# Bài 5: Nhập 2 số nguyên a và b từ bàn phím
    # Yêu cầu 1: In ra tất cả các số trong khoảng [a, b] hoặc ngược lại
    # Yêu cầu 2: Tính tổng các số chia hết cho 3 trog khoảng vừa in
    # Yêu cầu 3: In ra số lượng số lẻ có trong khoảng trên

# Bài 6: In ra bảng cửu chương từ 5 đến 9

# Bài 7: Nhập số nguyên dương n. Tính tổng tất cả các chữ số của n.
    # Ví dụ: n = 123 => Tổng các chữ số = 1+2+3 = 6

# Bài 8: Nhập n là số giây cần chuyển đổi (số nguyên)
    # In ra màn hình dạng h-m-s
    # Ví dụ: 3661s = 1h 1p 1s

# Bài 9: Danh sách
    # YC1: Nhập vào từ bàn phím 1 danh sách bao gồm 10 số nguyên
    # YC2: Thêm số '-5' vào vị trí thứ 2 (index=2) trong danh sách
    # YC3: Tính tổng các cố chẵn trong danh sách
    # YC4: Đếm số lượng số lẻ có trong danh sách
    # YC5: Tìm giá trị phần tử lớn nhất của danh sách
    # YC6: Tìm vị trí phần tử nhỏ nhất của danh sách
    # YC7: Dùng hàm tính giá trị trung bình của các phần tử trong danh sách


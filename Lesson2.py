# # Variables - Biến số
#     # Dùng để lưu trữ dữ liệu
#     # Có thể thay đổi trong khi lập trình

# # Khai báo biến số: [Tên biến] = [Giá trị]
#     # Khai báo 1 biến
# x = 10
#     # Khai báo nhiều biến số 1 lúc
# a, b, c = 5, 6, 7

# # Data types - Kiểu dữ liệu
#     # String - chuỗi ký tự / xâu ký tự
# name = 'Duc Trung'    
#     # Integer (int): số nguyên
# age = 30
#     # Float: số thực, số thập phân
# score = 9.5
#     # Bool / Boolean: chỉ gồm 2 giá trị True/False - Đúng/Sai
# male = True

# # Kiểm tra kiểu dữ liệu - type()
# print('Kiểu dữ liệu của name:', type(name))
# print('Kiểu dữ liệu của age:', type(age))
# print('Kiểu dữ liệu của score:', type(score))
# print('Kiểu dữ liệu của male:', type(male))

# # 4 cách hiển thị dữ liệu
#     # Cách 1: Dùng dấu cộng
# print('Họ tên: ' + name)        
# print('Tuổi: ' + str(age))      # ép kiểu dữ liệu
#     # Cách 2: Dùng dấu phẩy
# print('Điểm số:', score)
# print('Giới tính nam:', male)
#     # Cách 3: Dùng format - f: truyền dữ liệu vào string
# print('Tôi tên là ' + name + ', hiện đang ' + str(age) + ' tuổi.')
# print(f'Tôi tên là {name}, hiện đang {age} tuổi.')
#     # Cách 4: in trên nhiều dòng
# print(f'''
# Điểm số trung bình: {score}
# Giới tính nam: {male}
# ''')

# # Nhập dữ liệu - input()
# teacher = input('Nhập tên giáo viên: ')
# print('Kiểu dữ liệu của teacher:', type(teacher))
# weight = float(input('Nhập cân nặng: '))
# print('Kiểu dữ liệu của weight:', type(weight))

# # =============== BÀI TẬP ================
# # Bài 1: Chuyển đổi USD sang VND
#     # Nhập số lượng USD muốn chuyển đổi (float)
usd = float(input('Nhập số USD muốn đổi: '))
#     # Đổi USD sang VND, tỉ giá: 1 USD = 25000 VND
vnd = usd * 25000
#     # Hiển thị số tiền sau chuyển đổi (VD: 10 USD = 250000 VND)
print(f'{usd} USD = {vnd} VND')

# Bài 2: Nhập chiều dài, chiều rộng HCN.
# Tính chu vi, diện tích HCN và hiển thị ra màn hình
    # Nhập chiều dài, chiều rộng HCN (float)
cd = float(input('Nhập chiều dài: '))
cr = float(input('Nhập chiều rộng: '))
    # Tính chu vi, diện tích HCN
cvi = (cd + cr) * 2
dt = cd * cr
    # Hiển thị kết quả
print('Chu vi HCN:', cvi)
print('Diện tích HCN:', dt)
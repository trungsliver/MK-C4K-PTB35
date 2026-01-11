# String - Chuỗi / xâu ký tự
name = 'Hoang Anh'

# Độ dài string
print('Độ dài string:', len(name))

# Ký tự thứ n trong string: string[n]
print('Ký tự thứ đầu tiên:', name[0])
print('Ký tự thứ 3:', name[3])  
print('Ký tự cuối cùng:', name[-1])

# Duyệt string
    # Cách 1: Dùng cả index và value
for i in range(len(name)):
    print(f'Ký tự thứ {i} là: {name[i]}')

    # Cách 2: Chỉ dùng value
for item in name:
    print('Ký tự:', item)

# Xâu con (substring)
str1 = 'TungTiTon'
str2 = 'TiTon'
str3 = 'DepTrai'

    # Kiểm tra xâu con: hàm in => True/False
print(str2 in str1)
print(str3 in str1)

    # Tìm vị trí xâu con: hàm find() => index
print(str1.find(str2))  # Tìm thấy trả về vị trí đầu tiên  
print(str1.find(str3))  # Không tìm thấy trả về -1
print(str1.find('Ton')) # 6 

# Slicing - cắt chuỗi
name = 'VuHoangAoXanh'
    # Cắt từ đầu string
print(name[:7])   
    # Cắt đến cuối string
print(name[7:])
    # Cắt giữa string
print(name[2:7])

# Strip() - Xoá khoảng trắng thừa ở đầu và cuối
name = '      Duc Anh hihi      '
print('Thông thường:', name)
print('Đã strip:', name.strip())

# Thay thế string: hàm replace()
song = 'baby shark doo doo doo doo doo doo'
    # Thay thế toàn bộ
song2 = song.replace('doo', 'minh')
print('Sau khi thay thế:', song2)
    # Thay thế với số lượng chỉ định
song3 = song.replace('doo', 'minh', 3)
print('Sau khi thay thế 3 lần:', song3)

# Kết hợp chuỗi - join()
arr = ['r','o','n','a','l','d','o']
str1 = ' '.join(arr)
str2 = '-'.join(arr)
str3 = ''.join(arr)
print('Kết hợp với khoảng trắng:', str1)    # r o n a l d o
print('Kết hợp với dấu - :', str2)          # r-o-n-a-l-d-o
print('Kết hợp không dấu:', str3)           # ronaldo

# Tách chuỗi - split()

    # Tách theo khoảng trắng
str1 = '1 2 3 4 5 6 7 8 9'
arr1 = str1.split()
print('Mảng sau khi tách:', arr1)

    # Tách theo ký tự chỉ định
str2 = 'apple,banana,grape,orange'
arr2 = str2.split(',')
print('Mảng sau khi tách:', arr2)

# Chuyển đổi kiểu dữ liệu trong danh sách
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    # Cách 1:
num1 = []
for item in numbers:
    item_converted = int(item)
    num1.append(item_converted)
print('Danh sách số (cách 1):', num1)

    # Cách 2: 
num2 = [int(item) for item in numbers]
print('Danh sách số (cách 2):', num2)

# -------------------------Luyện tập-----------------------
# Bài 1: Nhập 2 thông tin: họ, tên. In ra màn hình tên đầy đủ

# Bài 2: Nhập vào 1 xâu ký tự định dạng dd/mm/yyyy (01/08/2024)
    # Tách ngày, tháng, năm và hiển thị ra màn hình

# Bài 3: Nhập vào thông tin dạng username:password
    # kiểm tra xem thông tin vừa nhập có trùng với thông tin có sẵn
    # YC2: bắt người dùng nhập đến khi nào trùng username và password thì kết thúc
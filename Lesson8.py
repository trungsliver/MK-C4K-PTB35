# Danh sách - Array / List
# 4 thao tác: CRUD: Create - Read - Update - Delete

# Create - Khởi tạo danh sách
    # Danh sách rỗng - không có phần tử
arr = []
    # Danh sách có phần tử
ptb35 = ['Duc Anh', 'Vu Hoang', 'Hoang Anh', 'Nhat Minh', 'Nguyen Vu', 'Minh Tung']
    # len(): trả về độ dài / số lượng phần tử danh sách
print('arr length:', len(arr))
print('ptb35 length:', len(ptb35))

# Read - Duyệt, hiện phần tử danh sách
    # Hiện phần tử bằng chỉ số index
print(ptb35[3])   # Nhat Minh
    # Hiện phần tử đầu tiên
print(ptb35[0])   # Duc Anh
    # Hiện phần tử cuối cùng
print(ptb35[-1])  # Minh Tung

    # Duyệt và hiện tất cả phần tử
        # Cách 1: Dùng cả index và value
for i in range(len(ptb35)):
    print(f'Index {i}:', ptb35[i])
        # Cách 2: Chỉ dùng value
for item in ptb35:
    print('Value:', item)
        # Cách 3: Dùng hàm có sẵn
for index, value in enumerate(ptb35):
    print(f'Index {index}:', value)
        # Cách 4: test
print(ptb35)

# Update - Chỉnh sửa danh sách
    # Thêm phần tử vào cuối danh sách - append(value)
ptb35.append('Duc Trung')
    # Thêm vào vị trí chỉ định - insert(index, value)
ptb35.insert(2, 'Imposter')
    # Chỉnh sửa value phần tử
ptb35[0] = 'áo cam'


# Delete - Xóa phần tử danh sách
    # Xóa phần tử bằng giá trị - remove(value)
ptb35.remove('Duc Trung')
    # Xóa phần tử bằng chỉ số index - pop(index)
ptb35.pop(2)
    # Xóa toàn bộ danh sách - clear()
ptb35.clear()

# Sắp xếp phần tử danh sách - sort()
numbers = [5, 2, 9, 7, 1, 6, 3, 8, 4]
    # Theo thứ tự tăng dần
numbers.sort()
print(numbers)
    # Theo thứ tự giảm dần
numbers.sort(reverse=True)
print(numbers)

# Tìm phần tử lớn nhất & nhỏ nhất
print('Max number:', max(numbers))
print('Min number:', min(numbers))

# ================ LUYỆN TẬP ================
# Bài 1: Nhập từ bàn phím 1 số nguyên n
# Yêu cầu: Kiểm tra xem n có phải là số nguyên tố hay không
# Biết rằng số nguyên tố là số chỉ chia hết cho 1 và chính nó

n = int(input('Nhập số nguyên n: '))
    # count dùng để đếm số lần chia hết
count = 0
    # Duyệt từ 1 đến n
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
    # Kiểm tra count
if count == 2:
    print(f'{n} là số nguyên tố')
else:
    print(f'{n} không phải số nguyên tố')

# Bài 2: In ra các số nguyên tố trong khoảng [50,100] và tính tổng các số đó
    # Khai báo báo biến lưu tổng
total = 0
    # Duyệt n từ 50 đến 100
for n in range(50, 101):
    # Kiểm tra n có phải số nguyên tố không
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    # Nếu n là số nguyên tố thì in ra và tính tổng
    if count == 2:
        print(n, end=' ')
        total += n
print('\nTổng các số nguyên tố trong khoảng [50,100]:', total)
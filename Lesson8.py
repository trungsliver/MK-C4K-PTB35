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
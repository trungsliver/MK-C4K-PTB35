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
# ============== Chữa BTVN =============
# Bài 1: Thầy giáo mang kẹo làm quà cho cả lớp nhân dịp lớp có kết quả kiểm tra tốt. Túi kẹo có n viên và lớp có m học sinh. Số kẹo được chia đều cho tất cả học sinh trong lớp. 
# Viết chương trình: Nhập n và m vào từ bàn phím, đưa ra màn hình số kẹo mỗi học sinh nhận được và số kẹo còn thừa sau khi chia.

n = int(input('Nhập số viên kẹo: '))
m = int(input('Nhập số học sinh: '))

print('Số kẹo mỗi học sinh nhận được:', n // m)
print('Số kẹo còn thừa sau khi chia:', n % m)

# Bài 2: Viết chương trình nhập vào một số nguyên s là số giây cần xử lý. Hãy đối số giây cho trước thành số giờ, phút, giây và in kết quả ra màn hình.
# Ví dụ: 3661s = 1h 1m 1s

time = int(input("Nhập số giây: "))

h = time // 3600
m = (time % 3600) // 60
s = time % 60

print(f"{time}s = {h}h {m}m {s}s")

# Bài 3: Nhập số điện bạn sử dụng (kWh)
# Tính tiền điện theo dữ liệu sau và hiển thị ra màn hình
# Bậc 1:    0kWh - 50kWh           giá 1.8k VND
# Bậc 2:    51kWh - 100kWh         giá 2k VND
# Bậc 3:    101kWh - 200kWh        giá 2.3k VND
# Bậc 4:    trên 201kWh            giá 3k VND
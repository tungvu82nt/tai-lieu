# MyIP: Công cụ kiểm tra thông tin IP toàn diện

**Tác giả:** Thanh Kim  
**Danh mục:** Basic Hacking  
**Ngày đăng:** 20/11/2024  

**MyIP**, một công cụ kiểm tra mạng toàn diện, nổi lên như một giải pháp hữu hiệu giúp người dùng thấu hiểu và quản lý kết nối internet của mình một cách hiệu quả. Trong bối cảnh thế giới số ngày càng phát triển, việc đảm bảo an toàn và tối ưu hóa hiệu suất mạng trở nên vô cùng quan trọng. MyIP không chỉ đơn thuần hiển thị địa chỉ IP, mà còn cung cấp một loạt các tính năng kiểm tra chuyên sâu, từ tốc độ mạng, rò rỉ DNS, WebRTC đến kiểm tra kiểm duyệt và tra cứu Whois.

## **Những tính năng chính của MyIP**

- **Hiển Thị Địa Chỉ IP**: Ứng dụng sẽ Xác định và hiển thị các địa chỉ IP cục bộ từ nhiều nhà cung cấp IPv4 và IPv6 khác nhau.
- **Thông Tin IP**: Cung cấp chi tiết về mọi địa chỉ IP, bao gồm quốc gia, khu vực, ASN, vị trí địa lý, và nhiều thông tin khác.
- **Kiểm Tra Tình Khả Dụng:** Xác định tính khả dụng của các trang web như Google, GitHub, YouTube, ChatGPT, và nhiều trang khác.
- **Phát Hiện WebRTC:** Xác định địa chỉ IP sử dụng trong các kết nối WebRTC.
- **Kiểm Tra Rò Rỉ DNS:** Hiển thị dữ liệu từ điểm cuối DNS để đánh giá nguy cơ rò rỉ DNS khi sử dụng VPN hoặc proxy.
- **Kiểm Tra Tốc Độ Mạng:** Đánh giá tốc độ kết nối mạng của bạn với các mạng biên.
- **Kiểm Tra Quy Tắc Proxy:** Kiểm tra các cài đặt quy tắc của phần mềm proxy để đảm bảo chúng hoạt động chính xác.
- **Kiểm Tra Độ Trễ Toàn Cầu:** Thực hiện các bài kiểm tra độ trễ trên các máy chủ tại các khu vực khác nhau trên thế giới.
- **MTR Test:** Thực hiện các bài kiểm tra MTR trên các máy chủ tại các khu vực khác nhau trên toàn cầu.
- **DNS Resolver:** Thực hiện phân giải DNS của một tên miền từ nhiều nguồn khác nhau và thu thập kết quả phân giải thời gian thực để xác định sự nhiễm độc DNS.
- **Kiểm Tra Kiểm Duyệt:** Kiểm tra xem liệu một trang web có bị chặn ở một số quốc gia hay không.
- **Tra Cứu Whois:** Thực hiện tra cứu thông tin whois cho tên miền hoặc địa chỉ IP.
- **Tra Cứu Địa Chỉ MAC:** Truy vấn thông tin của một địa chỉ vật lý.
- **Chế Độ Tối:** Tự động chuyển đổi giữa chế độ tối và sáng dựa trên cài đặt hệ thống, hoặc bạn có thể chuyển đổi thủ công.
- **Chế Độ Tối Giản:** Chế độ tối ưu hóa cho di động, rút ngắn độ dài trang để truy cập nhanh các thông tin cần thiết.
- **Tra Cứu Thông Tin IP:** Cung cấp công cụ tra cứu thông tin về bất kỳ địa chỉ IP nào.
- **Hỗ Trợ PWA:** Có thể thêm vào như một ứng dụng trên điện thoại hoặc dưới dạng ứng dụng Chrome trên máy tính.
- **Phím Tắt:** Hỗ trợ phím tắt cho tất cả các chức năng, nhấn ? để xem danh sách phím tắt.

Dựa trên kết quả kiểm tra khả dụng, chỉ ra liệu kết nối internet toàn cầu có khả thi hay không.
- Hỗ Trợ tiếng Anh, tiếng Trung và tiếng Pháp.

## **Cách sử dụng MyIP**

### **Triển khai MyIP trong môi trường Node**

**Bước 1:** Đầu tiên, đảm bảo bạn đã cài đặt Node.js trước khi thực hiện nhé

**Bước 2:** Sao chép mã sau:

```bash
git clone https://github.com/jason5ng32/MyIP.git
```

**Bước 3:** Chạy lệnh sau để cài đặt và build:

```bash
npm install && npm run build
```

**Bước 4:** Tiến hành chạy chương trình bằng lệnh này:

```bash
npm start
```

Chương trình sẽ chạy trên cổng 18966.

### **Sử dụng Docker**

Nhấp vào Nút 'Deploy to Docker' ở đầu trang để hoàn tất việc triển khai.

Hoặc sử dụng lệnh Shell sau:

```bash
docker run -d -p 18966:18966 --name myip --restart always jason5ng32/myip:latest
```

## **Biến Môi Trường (Environment Variable)**

Bạn có thể sử dụng chương trình mà không cần thêm bất kỳ biến môi trường nào, nhưng nếu bạn muốn sử dụng một số tính năng nâng cao, bạn có thể thêm các biến môi trường vào.

### **Sử dụng biến môi trường trong Node.js**

Để tùy chỉnh MyIP trong Node.js, bạn có thể sử dụng biến môi trường. Dưới đây là các bước chi tiết:

**Bước 1:** Để tạo các biến môi trường, bạn có thể làm theo các bước sau:

```bash
cp .env.example .env
```

**Bước 2:** Sau đó, chỉnh sửa nội dung file .env và thêm các dòng như sau:

```bash
BACKEND_PORT=11966
FRONTEND_PORT=18966
BING_MAP_API_KEY="YOUR_KEY_HERE"
ALLOWED_DOMAINS="example.com"
IPCHECKING_API="YOUR_KEY_HERE"
```

**Bước 3:** Cuối cùng, khởi động lại dịch vụ backend để áp dụng thay đổi.

**Giải thích các biến môi trường:**

- BACKEND_PORT: Cổng mà máy chủ backend sẽ lắng nghe.
- FRONTEND_PORT: Cổng mà giao diện người dùng frontend sẽ chạy.
- BING_MAP_API_KEY: Khóa API của Bing Maps, sử dụng cho các tính năng liên quan đến vị trí địa lý.
- ALLOWED_DOMAINS: Danh sách các tên miền được phép truy cập ứng dụng.
- IPCHECKING_API: Khóa API của dịch vụ kiểm tra IP, sử dụng để xác minh địa chỉ IP.

### **Sử dụng biến môi trường trong Docker**

Bạn cũng có thể sử dụng biến môi trường khi chạy MyIP trong Docker. Ví dụ:

```bash
docker run -d -p 18966:18966 \
-e BING_MAP_API_KEY="YOUR_KEY_HERE" \
-e ALLOWED_DOMAINS="example.com" \
-e IPCHECKING_API="YOUR_TOKEN_HERE" \
--name myip \
jason5ng32/myip:latest
```

## **Cách sử dụng MyIP nâng cao**

Nếu bạn đang sử dụng proxy để truy cập internet, hãy cân nhắc thêm quy tắc sau vào cấu hình proxy của mình (chỉnh sửa tùy theo ứng dụng bạn sử dụng). Thiết lập này cho phép bạn kiểm tra cả IP thực và IP khi sử dụng proxy:

```bash
# IP Testing
IP-CIDR,1.0.0.1/32,DIRECT,no-resolve
IP-CIDR6,2606:4700:4700::1111/128,DIRECT,no-resolve
DOMAIN-SUFFIX,ipify.org,Proxy

# Rule Testing
DOMAIN,ptest-1.ipcheck.ing,Proxy1
DOMAIN,ptest-2.ipcheck.ing,Proxy2
DOMAIN,ptest-3.ipcheck.ing,Proxy3
DOMAIN,ptest-4.ipcheck.ing,Proxy4
DOMAIN,ptest-5.ipcheck.ing,Proxy5
DOMAIN,ptest-6.ipcheck.ing,Proxy6
DOMAIN,ptest-7.ipcheck.ing,Proxy7
DOMAIN,ptest-8.ipcheck.ing,Proxy8
```

**Giải thích quy tắc Proxy:**

- IP-CIDR và IP-CIDR6: Định tuyến các yêu cầu đến các địa chỉ IP cụ thể trực tiếp, không thông qua proxy.
- DOMAIN-SUFFIX: Định tuyến các yêu cầu đến tên miền ipify.org thông qua proxy.
- DOMAIN: Định tuyến các yêu cầu đến các tên miền ptest-*.ipcheck.ing thông qua các proxy khác nhau (Proxy1 đến Proxy8).

**Lưu ý:** Cấu hình này chỉ là ví dụ, bạn cần điều chỉnh theo cấu hình proxy cụ thể của mình.

## **Lời Kết**

Tóm lại, **MyIP** là một công cụ mạnh mẽ và linh hoạt, cung cấp một giải pháp toàn diện để kiểm tra mạng và bảo vệ quyền riêng tư trực tuyến. Với giao diện thân thiện và dễ sử dụng, MyIP là lựa chọn hoàn hảo dành cho người dùng cá nhân và ngay cả chuyên gia.

**Tags:** MyIP

---

*Nguồn: AnonyViet*
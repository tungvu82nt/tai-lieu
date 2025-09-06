# Seekr: Thu thập & quản lý dữ liệu OSINT

**Tác giả:** Thanh Kim  
**Danh mục:** Basic Hacking  
**Ngày đăng:** Không xác định  

Việc thu thập và phân tích thông tin từ các nguồn mở (OSINT) ngày càng trở nên quan trọng. Cho dù bạn là nhà nghiên cứu, nhà báo, chuyên gia an ninh mạng hay chỉ đơn giản là người muốn tìm hiểu thêm về thế giới xung quanh, việc có một công cụ OSINT mạnh mẽ và hiệu quả là điều cần thiết. Hãy cùng tìm hiểu về **Seekr**, một bộ công cụ OSINT đa năng và dễ sử dụng, hứa hẹn sẽ cách mạng hóa cách bạn tiếp cận và khai thác thông tin từ nguồn mở.

## **Giới thiệu về Seekr**

Seekr là một bộ công cụ đa năng được thiết kế để thu thập và quản lý dữ liệu OSINT (Open Source Intelligence) thông qua một giao diện web trực quan và dễ sử dụng. Giao diện desktop của Seekr cho phép bạn tích hợp tất cả các công cụ OSINT yêu thích của mình vào một nơi duy nhất.

Được viết bằng ngôn ngữ Go với BadgerDB là cơ sở dữ liệu, Seekr cung cấp một loạt các tính năng mạnh mẽ cho việc thu thập, tổ chức và phân tích dữ liệu. Cho dù bạn là nhà nghiên cứu, điều tra viên hay chỉ đơn giản là người muốn thu thập thông tin, Seekr sẽ giúp bạn dễ dàng tìm kiếm và quản lý dữ liệu cần thiết.

## **Các tính năng chính của Seekr**

- KHÔNG yêu cầu API key cho tất cả các tính năng, giúp tiết kiệm thời gian và công sức cho việc đăng ký và quản lý API key.
- Giao diện Desktop quen thuộc và dễ sử dụng.
- Cơ sở dữ liệu cho các mục tiêu OSINT được lưu trữ và tổ chức một cách hiệu quả.
- Tích hợp / điều chỉnh nhiều công cụ OSINT phổ biến (ví dụ: phoneinfoga)
- Tìm kiếm thông tin liên quan đến địa chỉ email trên GitHub.
- Nhập thông tin bạn có và nhận được đề xuất về các công cụ web hữu ích.
- Thẻ tài khoản cho mỗi người trong cơ sở dữ liệu để quản lý thông tin về các cá nhân một cách chi tiết.
- Tự động tìm kiếm và liên kết các tài khoản trực tuyến.
- Các trường (fields) được xác định trước thường được sử dụng trong cơ sở dữ liệu, giúp tiết kiệm thời gian nhập liệu và đảm bảo tính nhất quán.
- Tùy chỉnh theme và plugin để mở rộng chức năng của Seekr.

## **Hướng dẫn cài đặt Seekr**

**Lưu ý:** Các bản build không ổn định có thể chứa lỗi và không được khuyến nghị sử dụng trong môi trường sản xuất.

### **Cài đặt Seekr trên Windows**

- **Bản ổn định:**

Tải xuống và chạy file exe mới nhất. Sau đó, mở giao diện web trong trình duyệt.

- **Bản không ổn định:**

Đầu tiên bạn hãy cài đặt TypeScript và Go. Sau đó để cài Seekr trên Windows, hãy chạy các lệnh sau:

```bash
git clone https://github.com/seekr-osint/seekr
cd seekr
go generate ./...
tsc --project web
go run main.go
```

### **Cài đặt Seekr với Docker**

```bash
docker pull ghcr.io/seekr-osint/seekr:latest
docker run -p 8569:8569 ghcr.io/seekr-osint/seekr:latest
```

### **Cài đặt Seekr trên Linux**

- **Bản ổn định:**

Tải xuống file binary ổn định mới nhất

- **Bản không ổn định:**

Đảm bảo bạn đã cài đặt TypeScript và Go. Để cài đặt Seekr trên Linux, hãy chạy các lệnh sau:

```bash
git clone https://github.com/seekr-osint/seekr
cd seekr
go generate ./...
tsc --project web
go run main.go
```

Sau đó, mở giao diện web trong trình duyệt.

### **Chạy Seekr trên NixOS**

Seekr được build với NixOS và hỗ trợ nix flakes. Để chạy Seekr trên NixOS, hãy chạy các lệnh sau:

```bash
nix shell github:seekr-osint/seekr
seekr
```

## **Cách sử dụng Seekr**

Bạn có thể tham khảo hướng dẫn sử dụng công cụ này qua bài viết khác về SEEKR: Bộ công cụ thu thập dữ liệu bằng OSINT.

## **Lời Kết**

**Seekr** là một công cụ OSINT linh hoạt, cung cấp cho người dùng một giải pháp toàn diện để thu thập, tổ chức và phân tích dữ liệu từ các nguồn mở. Với giao diện thân thiện, tích hợp nhiều công cụ phổ biến và khả năng tùy chỉnh cao, Seekr là lựa chọn lý tưởng cho các nhà nghiên cứu, điều tra viên và bất kỳ ai muốn khai thác sức mạnh của OSINT.

**Tags:** Seekr

---

*Nguồn: AnonyViet*
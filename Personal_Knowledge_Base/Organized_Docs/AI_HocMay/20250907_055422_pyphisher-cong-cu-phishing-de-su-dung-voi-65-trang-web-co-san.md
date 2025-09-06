# PyPhisher: Công cụ phishing dễ sử dụng với 65 trang web có sẵn

**Tác giả:** Ellyx13  
**Danh mục:** Basic Hacking  
**Ngày đăng:** 26/05/2022

[PyPhisher](https://github.com/KasRoudra/PyPhisher) là một công cụ lừa đảo cuối cùng trong python. Bao gồm các trang web phổ biến như Facebook, Twitter, Instagram, Github, Reddit, Gmail và nhiều trang web khác.

## Tuyên bố từ chối trách nhiệm

Công cụ này được phát triển cho mục đích giáo dục. Nó trình bày cách thức hoạt động của lừa đảo. Nếu bạn muốn truy cập trái phép vào phương tiện truyền thông xã hội của người nào đó, bạn phải chịu rủi ro của riêng mình. Bạn có trách nhiệm của riêng mình và bạn phải chịu mọi thiệt hại hoặc vi phạm pháp luật bởi công cụ này. Tác giả không chịu trách nhiệm khi bạn sử dụng sai PyPhisher vào mục đích xấu.

## Cách cài đặt PyPhisher

Cài đặt các dependencies chính (git và python):

- **Trên Debian:**
  ```bash
  sudo apt install git python -y
  ```

- **Trên Arch:**
  ```bash
  sudo pacman -S git python --noconfirm
  ```

- **Trên Fedora:**
  ```bash
  sudo yum install git python -y
  ```

- **Trên Termux:**
  ```bash
  pkg install git python -y
  ```

Tải kho lưu trữ PyPhiser về:
```bash
git clone https://github.com/KasRoudra/PyPhisher
```

Truy cập vào thư mục vừa tải về:
```bash
cd PyPhisher
```

Chạy PyPhiser:
```bash
python3 pyphisher.py
```

Hoặc bạn cũng có thể trực tiếp bằng lệnh:
```bash
wget https://raw.githubusercontent.com/KasRoudra/PyPhisher/main/pyphisher.py && python3 pyphisher.py
```

### Các tuỳ chọn:

```
Cách sử dụng: pyphisher.py [-h] [-p PORT] [-o OPTION]
                    [--update | --no-update]

Tuỳ chọn:
  -h, --help            hiển thị thông báo trợ giúp và thoát
  -p PORT, --port PORT  Cổng máy chủ của PyPhisher [ Mặc định : 8080 ]
  -o OPTION, --option OPTION
                        Chỉ mục mẫu của PyPhisher [ Mặc định : null ]
  --update, --no-update
                        Kiểm tra cập nhật (Mặc định : True)
```

## Các tính năng của PyPhiser

- Đa nền tảng (Hỗ trợ hầu hết các bản phân phối của linux)
- 65 mẫu trang web
- Đường hầm kép (Ngrok và Cloudflared)
- Dễ sử dụng
- Trình chẩn đoán lỗi có thể xảy ra
- Tạo mặt nạ url
- Tùy chỉnh của url
- Tệp di động (Có thể chạy từ bất kỳ thư mục nào)
- Nhận Địa chỉ IP và nhiều chi tiết khác cùng với thông tin đăng nhập

## Yêu cầu

- `Python(3)`
- `PHP`
- `Curl`
- `Unzip`
- `Wget`
- Dung lượng 100MB

Nếu không có các gói trên, thì tất cả các gói bắt buộc sẽ được cài đặt trong lần chạy đầu tiên.

## Cách sử dụng PyPhiser

Mình test trên WSL2 Ubuntu. Ngoài ra, bạn cũng có thể test trên máy linux thật hoặc sử dụng Termux trên điện thoại nhé.

**Bước 1:** Cài đặt và chạy PyPhiser như mình đã hướng dẫn ở trên.

**Bước 2:** Chọn trang web mẫu mà bạn muốn phishing. Mình sẽ chọn số 1 nhé.

**Bước 3:** Sau khi chọn xong thì công cụ sẽ cung cấp cho bạn 4 url giả mạo trang web. Bạn chỉ cần đưa 1 trong 4 url này cho victim nhấp vô là được.

**Bước 4:** Còn nếu bạn muốn tuỳ chỉnh url thì nhấn y. Yêu cầu đầu tiên là nhập domain bạn muốn, mình nhập facebook.com. Yêu cầu thứ 2 là nhập từ khoá bạn muốn xuất hiện trong url, mình nhập login. Và công cụ sẽ cung cấp url như dưới.

Trang web mà victim truy cập sẽ có giao diện y như facebook thật. Nhưng nếu bạn để ý kỹ thì url sẽ không giống như facebook thật.

Khi mình đăng nhập vô trang facebook giả mạo thì nó sẽ chuyển mình sang trang đặt lại mật khẩu của facebook thật.

Và đây là thành quả. Công cụ này không chỉ ghi lại tài khoản, mật khẩu mà victim nhập mà nó còn cung cấp luôn cả IP và một số thông tin khác của victim nữa. Nhưng bạn lưu ý là vị trí toạ độ sẽ không chính xác nhé.

## Kết luận

PyPhisher là một công cụ mạnh mẽ để hiểu về cách thức hoạt động của các cuộc tấn công phishing. Với 65 mẫu trang web có sẵn và khả năng tùy chỉnh URL, nó cung cấp một môi trường học tập tốt cho việc nghiên cứu bảo mật. Tuy nhiên, cần nhớ rằng công cụ này chỉ nên được sử dụng cho mục đích giáo dục và nghiên cứu bảo mật hợp pháp.

**Tags:** lừa đảo, phishing, PyPhisher, python
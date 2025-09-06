# Cách dùng Hydra để tấn công Brute Force

Trong bài viết này, chúng ta sẽ nói về công cụ brute force Hydra. Theo Wikipedia, Hydra là một trình bẻ khóa đăng nhập mạng song song. Nó có sẵn trên một số bản phân phối Linux Penetration Testing như Kali Linux, Parrot OS, Black Arch và BackBox. Hydra có khả năng thực hiện các cuộc tấn công chống lại nhiều dịch vụ mạng khác nhau như Remote Desktop, Secure Shell và nhiều dịch vụ khác. Nó cũng có khả năng thực hiện các cuộc tấn công brute force chống lại các ứng dụng web.

![Hydra: Công cụ tấn công Brute Force](https://anonyviet.com/wp-content/uploads/2022/07/hydrimage.jpg)

## Cách cài đặt Hydra

Hydra có xu hướng được cài đặt sẵn trên hầu hết các bản phân phối pentest. Tuy nhiên, nó cũng có thể được cài đặt bằng cách sử dụng apt. Nếu kho lưu trữ của bạn không có Hydra thì nó có thể dễ dàng được cài đặt từ GitHub bằng cách sử dụng lệnh git clone.

![Cách dùng Hydra để tấn công Brute Force](https://anonyviet.com/wp-content/uploads/2022/07/0_qqwIFMU6PSu0fYhV.jpg)

## Brute Forcing RDP

Giao thức Máy tính Từ xa hay RDP (Remote Desktop Protocol) là một công cụ quản lý từ xa chủ yếu được sử dụng trong môi trường Windows. Nó sử dụng các dịch vụ đầu cuối để cho phép người dùng kết nối với máy chủ đích bằng RDP Client. Sau đó, người dùng sẽ được nhìn thấy những gì hiển thị trên máy người khác. Hơn nữa, điều này sẽ cho phép họ thực hiện các nhiệm vụ quản lý. RDP thường bị tin tặc tấn công bằng các công cụ tự động như Hydra. Bạn có thể xem ảnh bên dưới để biết lệnh tấn công RDP. Cờ L chỉ định danh sách người dùng, cờ P chỉ định danh sách mật khẩu. Các biến thể chữ thường sẽ cho phép bạn chỉ định các từ riêng lẻ. Cờ -F yêu cầu Hydra dừng lại khi nó đã tìm thấy mật khẩu chính xác. Sau đó, chúng ta cần chỉ định giao thức, địa chỉ IP.

```bash
sudo hydra -L usernames.txt -P passwords.txt -F rdp://10.0.2.5 -V
```

![Cách dùng Hydra để tấn công Brute Force](https://anonyviet.com/wp-content/uploads/2022/07/0_xhq1H1codG1C7qMF.jpg)

## Brute Forcing SSH

SSH hoặc Secure Shell là một giao thức quản lý từ xa khác. Nó được tìm thấy trong môi trường Linux hoặc Unix nhưng gần đây đã được thêm vào Windows. Hơn nữa, nó được coi là sự kế thừa của telnet. Telnet không được mã hóa nên mọi thứ được truyền ở dạng văn bản thuần. Nếu một tác nhân đe dọa trên mạng của bạn thực hiện một cuộc tấn công man-in-the-middle, tin tặc sẽ có thể thấy tên người dùng và mật khẩu của bạn được truyền đến máy chủ telnet. SSH là một giao thức được mã hóa, vì vậy nếu lưu lượng truy cập bị xen vào, thì tin tặc cũng sẽ không thể đọc được. Bạn có thể thực hiện các cuộc tấn công brute force SSH như sau:

```bash
sudo hydra -L username.txt -P passwords.txt -F ssh://10.0.2.5 -V
```

![Cách dùng Hydra để tấn công Brute Force](https://anonyviet.com/wp-content/uploads/2022/07/0_GEldJoYjh61o9WSP-1.jpg)

## Brute Forcing FTP

FTP là một giao thức để truyền tệp và cũng có thể bị Hydra tấn công brute force. Cú pháp sẽ giống hệt như RDP và SSH. Chỉ cần thay thế giao thức FTP. Còn rất nhiều tuỳ chọn khác của Hydra và bạn có thể tinh chỉnh các cuộc tấn công của mình để cụ thể hơn. Để thực hiện một cuộc tấn công brute force FTP:

```bash
Sudo hydra -L username.txt -P passwords.txt -F ftp://10.0.2.5 -V
```

![Cách dùng Hydra để tấn công Brute Force](https://anonyviet.com/wp-content/uploads/2022/07/0_fXbnwVMQL4M8P5cm.jpg)

## Brute Forcing ứng dụng web

Bạn cũng có thể brute force các ứng dụng web. Tuy nhiên, cú pháp để làm như vậy phức tạp hơn một chút. Bạn sẽ bắt đầu bằng cách chỉ định danh sách tên người dùng và mật khẩu. Tuy nhiên, bây giờ bạn cần chỉ định loại tấn công web cho dù đó là "http-post-form" hay "http-get-form" hay nó đang sử dụng xác thực cơ bản. Sau đó, bạn cần chỉ định đường dẫn đến tệp để tấn công. Tiếp theo, bạn cần xác định các tham số để tấn công (tên người dùng và mật khẩu). Hơn nữa, bạn cần chỉ định placeholders cho người dùng và chuyển các biến. Cuối cùng, bạn cần chỉ định bất kỳ cookie nào. Bạn có thể xem ví dụ dưới đây:

```bash
hydra -L users.txt -P password.txt 10.0.2.5 http-post-form "/path/index.php:name=^USER^&password=^PASS^&enter=Sign+in:Login name or password is incorrect" -V
```

![Cách dùng Hydra để tấn công Brute Force](https://anonyviet.com/wp-content/uploads/2022/07/0_v2_0vFTmo1i4juoU.jpg)

## Giao diện người dùng đồ họa Hydra

Hydra cũng có giao diện người dùng đồ họa. Để khởi chạy nó, bạn cần chạy lệnh xhydra. Nếu bạn thích GUI thì đây có thể là phương pháp sử dụng hydra ưa thích của bạn. Cá nhân mình thích sử dụng dòng lệnh hơn, mình thực sự thấy nó dễ cấu hình hơn GUI.

![Cách dùng Hydra để tấn công Brute Force](https://anonyviet.com/wp-content/uploads/2022/07/0_2-R49Ay9x0YHdlrd.jpg)

## Kết luận

Hydra là một công cụ mạnh mẽ để thực hiện các cuộc tấn công brute force chống lại nhiều dịch vụ mạng khác nhau. Nó hỗ trợ nhiều giao thức như RDP, SSH, FTP và cả các ứng dụng web. Với khả năng tấn công song song và giao diện dòng lệnh linh hoạt, Hydra là một công cụ không thể thiếu trong bộ công cụ penetration testing.

**Lưu ý:** Bài viết này chỉ mang tính chất giáo dục. Việc sử dụng Hydra để tấn công các hệ thống mà bạn không có quyền là bất hợp pháp và có thể dẫn đến hậu quả pháp lý nghiêm trọng.
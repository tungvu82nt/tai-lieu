# BigBountyRecon: Công cụ do thám bằng Google Dork

BigBountyRecon sử dụng 58 kỹ thuật khác nhau bằng cách sử dụng các công cụ mã nguồn mở và dorks khác nhau của Google để đẩy nhanh quá trình do thám mục tiêu. Trinh sát là bước quan trọng nhất trong bất kỳ thử nghiệm thâm nhập hoặc quy trình săn lỗi nào. Nó cung cấp cho kẻ tấn công một số thông tin sơ bộ về mục tiêu. Hơn nữa, sẽ rất hữu ích khi hiểu rõ những biện pháp bảo vệ nào đang được áp dụng cũng như một số ước tính sơ bộ về mức độ bảo mật của mục tiêu.

Công cụ này có thể được sử dụng để săn lỗi. Ý tưởng của công cụ này là nhanh chóng kiểm tra và thu thập thông tin về mục tiêu của bạn mà không cần đầu tư thời gian và ghi nhớ các tác vụ này. Ngoài ra, nó có thể giúp bạn xác định một số cách tiếp cận để nhanh chóng khai thác mục tiêu.

## Kỹ thuật mà BigBountyRecon sử dụng

BigBountyRecon có tới 58 kỹ thuật khác nhau, nhưng để tiết kiệm thời gian thì mình chỉ giới thiệu 10 kỹ thuật mà mình thấy ấn tượng cũng như được sử dụng nhiều nhất dưới đây:

1. **Danh sách thư mục**: Tìm các thư mục mở bằng Google Dork trên mục tiêu giúp bạn hiểu cấu trúc thư mục trên máy chủ web. Nó có thể làm lộ thông tin nhạy cảm hoặc có thể dẫn đến lộ thông tin.

2. **Tệp cấu hình**: Thông thường, tệp cấu hình chứa thông tin nhạy cảm như mật khẩu được mã hóa cứng, vị trí ổ đĩa nhạy cảm hoặc key API có thể giúp bạn có được quyền truy cập đặc quyền vào tài nguyên nội bộ.

3. **Tệp cơ sở dữ liệu**: Tệp cơ sở dữ liệu là tệp dữ liệu được sử dụng để lưu trữ nội dung của cơ sở dữ liệu ở định dạng các bảng và trường riêng biệt. Tùy thuộc vào bản chất của ứng dụng web, các tệp này có thể cung cấp quyền truy cập vào thông tin nhạy cảm.

4. **WordPress**: WordPress là một CMS mã nguồn mở được viết bằng PHP. WordPress có hàng nghìn plugin để xây dựng, tùy chỉnh và nâng cao các trang web. Nhưng cũng có rất nhiều lỗ hổng trong các plugin này.

5. **Tệp nhật ký**: Các tệp nhật ký đôi khi cung cấp thông tin chi tiết về hoạt động của người dùng trong một ứng dụng cụ thể. Các tệp này thường được dùng để xem cookie phiên hoặc các loại mã thông báo khác.

6. **Tệp sao lưu và tệp cũ**: Các tệp sao lưu là bản sao gốc của các hệ thống quan trọng. Chúng cung cấp quyền truy cập vào PII hoặc quyền truy cập vào các hồ sơ nhạy cảm.

7. **Trang đăng nhập**: Điều cực kỳ quan trọng là xác định các trang đăng nhập của mục tiêu của bạn để thực hiện bruteforce hoặc thử thông tin đăng nhập mặc định để có thêm quyền truy cập vào các tài nguyên của tổ chức.

8. **Lỗi SQL**: Lỗi SQL làm rò rỉ thông tin nhạy cảm về hệ thống phụ trợ. Điều này có thể giúp bạn liệt kê các loại cơ sở dữ liệu và xem liệu ứng dụng có dễ bị tấn công bằng lỗi liên quan đến xác thực đầu vào như SQL Injection hay không.

9. **Tệp cấu hình Apache**: Máy chủ Apache HTTP được cấu hình bằng cách đặt các chỉ thị trong tệp cấu hình văn bản thuần. Tệp cấu hình chính thường là httpd.conf. Tùy thuộc vào các mục nhập trong các tệp cấu hình này, nó có thể tiết lộ các chuỗi kết nối cơ sở dữ liệu, tên người dùng và mật khẩu, hoạt động bên trong, các thư viện được sử dụng và tham chiếu cũng như logic của ứng dụng.

10. **Tệp Robots.txt**: Tệp Robots.txt hướng dẫn robot web cách thu thập dữ liệu trên trang web của chúng. Tùy thuộc vào nội dung của tệp, kẻ tấn công có thể phát hiện ra các thư mục và tệp ẩn.

Ngoài ra, còn có thêm 48 kỹ thuật khác mà bạn có thể tìm hiểu tại GitHub.

## Cách sử dụng BigBountyRecon

**Bước 1:** Đầu tiên các bạn tải công cụng BigBountyRecon tại đây.

**Bước 2:** Tiếp theo các bạn cần mở file EXE vừa mới tải về.

**Bước 3:** Nhập tên miền của mục tiêu.

**Bước 4:** Nhấp vào các nút khác nhau trong công cụ để tìm thông tin.

**Bước 5:** Trong trường hợp gặp Google Captcha, bạn chỉ cần xác thực và tiếp tục.

---

*Nguồn: AnonyViet*
*Tags: BigBountyRecon, dork, Google Dork*
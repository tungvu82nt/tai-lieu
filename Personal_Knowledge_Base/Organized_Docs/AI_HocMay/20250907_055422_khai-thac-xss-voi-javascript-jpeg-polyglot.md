# Khai thác XSS với Javascript/JPEG Polyglot

**Tác giả:** Ellyx13  
**Danh mục:** Basic Hacking  
**Nguồn:** [AnonyViet](https://anonyviet.com/khai-thac-xss-voi-javascript-jpeg-polyglot/)

---

Cũng giống như PNG, JPEG và DOC là các loại tệp hợp lệ, polyglot là sự kết hợp của hai loại tệp khác nhau. Ví dụ: Phar + JPEG (tệp lưu trữ PHP và tệp JPEG), GIFAR (tệp Gif và Rar) Javascript + JPEG,….

## Giới thiệu về Polyglot

Các ứng dụng chỉ cho phép một số loại tệp nhất định trên các tính năng như tải tệp lên và không cho phép các loại tệp khác như tệp .php hoặc .js vì chúng có thể cho phép kẻ tấn công tải lên các tệp độc hại trên ứng dụng. Các ứng dụng thực hiện kiểm tra đuổi file bằng phần mở rộng kép (.jpg.php) hoặc sử dụng byte rỗng trong phần mở rộng (.php%00.jpg), tên tệp (.htaccess, .config,…) và nếu chữ ký của tệp được tải lên cũng phù hợp với loại nội dung của nó.

Ứng dụng khác nhau sử dụng các phương pháp khác nhau và polyglot có thể được sử dụng để bỏ qua một số kiểm tra xác thực này.

## Kiến trúc JPEG

Hình ảnh JPEG được biểu diễn dưới dạng một chuỗi các phân đoạn trong đó mỗi phân đoạn bắt đầu bằng header. Mỗi header bắt đầu bằng một số byte. Payload theo header là khác nhau tùy theo loại header. Các loại điểm đánh dấu JPEG phổ biến như được liệt kê bên dưới:

```
0xffd8: "Start of Image",
0xffe0: "Application Default Header",
0xffdb: "Quantization Table",
0xffc0: "Start of Frame",
0xffc4: "Define Huffman Table",
0xffda: "Start of Scan",
0xffd9: "End of Image"
```

Mỗi tệp nhị phân chứa một vài header. Chúng rất quan trọng đối với tệp vì chúng xác định thông tin cụ thể của tệp. Hầu hết các header được theo sau bởi thông tin độ dài. Điều này cho chúng ta biết phân đoạn cụ thể đó dài bao nhiêu.

Phần đầu của header hình ảnh chứa FF D8. Nếu chúng ta không nhìn thấy nó, chúng ta có thể cho rằng đây là một tệp khác. Một điểm đánh dấu quan trọng khác là FF D9 cho biết phần cuối của hình ảnh.

## Tạo Polyglot Javascript/JPEG

Để làm cho payload trông giống như một tệp JPEG hợp pháp, chúng ta sẽ thêm độ dài của header, header nhận xét, các byte rỗng vào pad và sau đó là vectơ tấn công javascript.

Giả sử vectơ tấn công là một lỗ hổng XSS `*/=alert("XSS")/*` Chuyển nó thành hệ thập lục phân sẽ như thế này.

**Payload trong hex:**
`2A 2F 3D 61 6C 65 72 74 28 22 58 53 53 2E 22 29`

Chúng ta có thể sử dụng một trình soạn thảo hex để đưa javascript vào metadata của hình ảnh. Điều này hoạt động được vì các trình duyệt diễn giải code khi chúng hiển thị hình ảnh thành HTML.

### Các bước thực hiện:

1. **Chuẩn bị tệp JPEG:** Lấy một tệp JPEG bất kỳ (ví dụ: test.jpg)

2. **Phân tích cấu trúc:** Sử dụng hexdump để xem cấu trúc của tệp JPEG
   - FF D8: Bắt đầu hình ảnh
   - 00 10: Độ dài header (16 byte)

3. **Thời gian tiêm payload:** Chúng ta sẽ đưa payload vào giữa FF E0 và FF DB
   - Bắt đầu với 2F 2A (hex của /*)
   - Thay thế 00 10 bằng 2F 2A (tương đương thập phân: 12074 byte)

4. **Tính toán padding:** 
   - Kích thước payload: 18 byte
   - Byte rỗng cần thêm: 12074 - 16 - 18 = 12040 byte

5. **Chèn payload và padding:**
   ```bash
   # Đọc test.jpg, chèn payload và thêm null bytes
   # Ghi kết quả vào test_new.jpg
   ```

6. **Đóng comment:** Thêm */ trước FF D9 để đóng thẻ comment

## Sử dụng Polyglot

Để thực thi tệp hình ảnh như JavaScript:

```html
<script charset="ISO-8859-1" src="test_new.jpeg">
```

**Lưu ý quan trọng:**
- Trên Firefox khi sử dụng bộ ký tự UTF-8, nó sẽ làm hỏng polyglot
- Cần chỉ định bộ ký tự ISO-8859-1 trên thẻ script để hoạt động
- Mozilla đã sửa lỗi này trong Firefox 51 và các phiên bản sau

## Kết quả

Khi thực hiện đúng các bước trên, polyglot javascript/jpeg sẽ hoạt động và thực thi mã JavaScript được nhúng trong tệp JPEG, có thể được sử dụng để khai thác lỗ hổng XSS.

## Ứng dụng trong Penetration Testing

Kỹ thuật này có thể được sử dụng để:
- Bypass các bộ lọc upload file
- Khai thác lỗ hổng XSS thông qua file upload
- Thực hiện các cuộc tấn công client-side
- Kiểm tra tính bảo mật của ứng dụng web

---

**Tags:** javascript, JPEG, Polyglot, XSS

**Tác giả:** Ellyx13 - "Có người không dám bước vì sợ gãy chân, nhưng sợ gãy chân mà không dám bước đi thì khác nào chân đã gãy."
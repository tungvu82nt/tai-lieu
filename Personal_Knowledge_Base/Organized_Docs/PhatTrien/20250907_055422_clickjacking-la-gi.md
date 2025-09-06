# Clickjacking là gì?

Trong bài viết này, chúng ta sẽ cùng tìm hiểu về lỗ hổng clickjacking. Một kỹ thuật không mới nhưng cũng vô cùng nguy hiểm nhằm đánh lừa những cú click chuột của người dùng.

## Clickjacking là gì?

### 1. Thẻ iframe

Trước khi đi sâu vào clickjacking, chúng ta cần hiểu thẻ iframe là gì.

Nhìn vào đoạn code dưới đây.

```html
<!DOCTYPE html>
<html>
<body>
<iframe src="https://www.w3schools.com"></iframe>
</body>
</html>
```

Đoạn code trên rất đơn giản.

Những gì thẻ iframe thực hiện chỉ đơn giản là đưa một trang khác vào trang của bạn.

Như bạn thấy, trang w3 đã được đưa vào trang.

Dễ phải không? Với thẻ iframe, bạn có thể đưa trang web khác vào trang của mình.

### 2. Lỗ hổng clickjacking cơ bản

Vậy, vấn đề của thẻ iframe là gì?

Vấn đề chính là iframe có thể bị ẩn đằng sau một cái gì đó.

Nghe hơi khó hiểu đúng chứ, nhưng thực tế thì nó dễ hiểu lắm.

Mình sẽ sử dụng phòng thí nghiệm Portswigger để giải thích cho cuộc tấn công.

Đăng nhập ứng dụng với các thông tin xác thực đã cho.

Nếu chúng ta chuyển đến Account, chúng ta có thể xóa tài khoản của mình.

Nếu trang dễ bị clickjacking, chúng ta có thể ẩn iframe và thuyết phục người dùng nhấp vào nút (hoặc từ) khác mà chúng ta đã thêm vào trang mà họ không biết gì cả.

Những gì bạn phải làm chỉ đơn giản là cung cấp đoạn code bên dưới cho nạn nhân.

```html
<!DOCTYPE html>
<html>
<body>
<style>
   iframe {
       position:relative;
       width:500px;
       height: 700px;
       opacity: 0.0001;
       z-index: 2;
   }
   div {
       position:absolute;
       top:320px;
       left:60px
       z-index: 1;
   }
</style>
<div>Test me</div>
<iframe src="Your_URL"></iframe>
</body>
</html>
```

Tóm lại, đoạn code trên đảm bảo rằng văn bản Test me được căn chỉnh chính xác trên nút delete của trang iframe.

Chúng ta có thể thấy từ các thông số CSS rằng iframe có độ mờ rất thấp, vì vậy nó sẽ ẩn đối với người dùng cũng như thẻ z-index sẽ đảm bảo rằng trang Portswigger nằm trên đầu Test me.

### 3. Cơ chế bảo vệ chống lại clickjacking

Có một số cách để giảm thiểu lỗ hổng clickjacking, mình sẽ bắt đầu liệt kê từ phương pháp kém tin cậy nhất đến an toàn nhất.

#### 1. Frame Busting

Frame Busting, là một kỹ thuật phía máy khách sử dụng JavaScript để tránh trang của bạn có thể được đóng khung thành một trang khác.

Như hầu hết các kỹ thuật phía máy khách, nó có thể dễ dàng bị bỏ qua bằng cách sử dụng thuộc tính hộp cát của thẻ iframe, ví dụ: tham số allow-script sẽ cho phép thẻ thực thi code JavaScript do đó bỏ qua cơ chế bảo vệ.

#### 2. X-Frame

X-Frame là một kỹ thuật phía máy chủ giúp giảm thiểu nhấp chuột bằng cách sử dụng tiêu đề X-Frame.

Tiêu đề này có thể được cấu hình với 3 tham số trong một yêu cầu HTTP.

- **Deny**: Mọi iframe sẽ bị chặn.
- **Sameorigin**: Iframe được cho phép, nhưng chỉ có thể được nhúng vào khung trên trang có cùng nguồn gốc với chính nó (Ví dụ: nếu http://example.com chỉ yêu cầu iframe của chính nó thì nó sẽ được phép sử dụng iframe đó).
- **Allow from**: Các trang web trong danh sách trắng có thể sử dụng iframe.

```
X-Frame-Options: deny
X-Frame-Options: sameorigin
X-Frame-Options: allow-from http://example.com
```

Ngay cả khi nó là một kỹ thuật tuyệt vời, ngày nay nó được coi là không còn được dùng nữa và CSP được sử dụng để thay thế nó.

#### 3. CSP

CSP là viết tắt của chính sách bảo mật nội dung (content security policy) là một cơ chế phòng thủ được thực hiện bởi các trang web để ngăn chặn clickjacking và các cuộc tấn công từ phía client như XSS.

Nó thường được triển khai trong máy chủ web dưới dạng return header.

Bạn có thể sử dụng tham số frame-ancestors để clickjacking với tùy chọn none tương đương với deny của X-Frame, và với tên của trang web được phép nhúng vào trang web.

```
Content-Security-Policy: frame-ancestors 'none'
Content-Security-Policy: frame-ancestors 'self'
Content-Security-Policy: frame-ancestors http://example.com
```

## Kết luận

Ngay cả khi một trang có thể được đưa vào iframe, điều đó không có nghĩa là bản thân nó là một lỗ hổng.

Trên thực tế, clickjacking chỉ có thể được khai thác khi trong trang có biểu mẫu hoặc lỗ hổng XSS.

---

*Nguồn: [AnonyViet](https://anonyviet.com/clickjacking-la-gi/)*
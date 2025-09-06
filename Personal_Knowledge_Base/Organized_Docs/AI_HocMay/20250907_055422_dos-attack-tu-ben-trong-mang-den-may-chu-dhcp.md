# DOS ATTACK từ bên trong mạng đến máy chủ DHCP

Bạn có thể lừa máy chủ DHCP không cung cấp địa chỉ IP cho các thiết bị, chặn hoàn toàn các kết nối mới bằng cách thực hiện một cuộc tấn công DoS được gọi là "tấn công đói DHCP". Mình sẽ hướng dẫn bạn cách thực hiện và cách bảo vệ mạng của bạn.

## Tấn công DoS vào máy chủ DHCP

DHCP là một giao thức dùng để cấu hình tự động các thiết bị. Thông thường, chúng là các thiết bị đầu cuối như máy tính, điện thoại hoặc máy in nhận địa chỉ IP, mask, default gateway, DNS,… nhờ DHCP.

Nhưng điều gì sẽ xảy ra khi ai đó ngăn cản cơ chế này hoạt động? Sẽ không có kết nối mạng cũng như kết nối internet. Chúng ta gọi kiểu tấn công này là tấn công DoS (Tấn công từ chối dịch vụ).

Cuộc tấn công được gọi là "tấn công đói DHCP" dựa trên thực tế là mỗi máy chủ DHCP có số lượng địa chỉ IP được xác định chính xác có thể được cấp cho các thiết bị. Ví dụ: mạng con có thể là 192.168.0.0/24, đại diện cho một phạm vi tối đa là 253 địa chỉ có thể sử dụng cho máy khách.

Nhưng khi kẻ tấn công yêu cầu tất cả các địa chỉ IP có sẵn bằng cách ghi đè một số lượng lớn các địa chỉ MAC không có thật, máy chủ sẽ không có bất kỳ địa chỉ IP nào cung cấp cho các thiết bị mới.

Cuộc tấn công này thậm chí còn tạo cơ hội cho kẻ tấn công nắm bắt được lưu lượng truy cập. Sau khi tắt máy chủ DHCP, kẻ tấn công có thể chuyển sang máy chủ DHCP của riêng mình. Ví dụ: một máy chủ DNS giả mạo có thể được cung cấp trong cấu hình DHCP để tấn công bạn. Mình thấy đây là một cuộc tấn công nguy hiểm.

## Mô phỏng cuộc tấn công

Mình sẽ cho bạn thấy cách thực hiện cuộc tấn công này dễ như thế nào. Mình sẽ sử dụng router và laptop của Cisco với bản phân phối KALI Linux để thử nghiệm. Mình sẽ sử dụng một công cụ có tên là Yersinia.

## Cấu hình cơ bản của máy chủ DHCP trên bộ định tuyến CISCO

```
ip dhcp excluded-address 192.168.0.1
 !
 ip dhcp pool LAN
 network 192.168.0.0 255.255.255.0
 default-router 192.168.0.1
 dns-server 8.8.8.8
```

Sau khi kết nối trạm đầu tiên, mình thấy một địa chỉ IP được chỉ định.

```
R1-NETVEL#show ip dhcp binding
```

Mình cũng thấy một lượng nhỏ các yêu cầu DHCP đến với bộ định tuyến.

```
R1-NETVEL#show ip dhcp server statistics
```

Và chỉ một địa chỉ IP được chỉ định

```
R1-NETVEL#show ip dhcp pool
```

## Khởi động cuộc tấn công

Mình sẽ sử dụng công cụ Yersinia. Bạn cũng có thể thực hiện việc này thông qua CLI, nhưng trong trường hợp này, mình thích GUI hơn. Bạn có thể mở nó bằng lệnh sau.

```
root@kali:~#yersinia -G
```

Hoặc bạn cũng có thể khởi động cuộc tấn công bằng vài cú click chuột thông qua giao diện đồ hoạ.

Bắt đầu: Khởi động cuộc tấn công -> gửi gói KHÁM PHÁ

Dừng: Liệt kê các cuộc tấn công -> Hủy cuộc tấn công

Sau một thời gian, máy chủ DHCP sẽ có nhiều yêu cầu hơn khả năng nó có thể xử lý. Đó là tấn công DoS.

```
R1-NETVEL#show ip dhcp binding
```

```
R1-NETVEL#show ip dhcp server statistics
```

```
R1-NETVEL#show ip dhcp pool
```

Như chúng ta thấy, cách tấn công tương đối đơn giản, nhưng rất nguy hiểm. Nó có thể được ngăn chặn bằng nhiều cách, chẳng hạn như giới hạn số lượng địa chỉ MAC đi qua cổng (bảo mật cổng) hoặc nếu chúng ta muốn ngăn kẻ tấn công cung cấp máy chủ DHCP của riêng mình, chúng ta có thể triển khai DHCP snooping.

## Kết luận

Tấn công đói DHCP là một phương thức tấn công DoS đơn giản nhưng hiệu quả, có thể làm tê liệt hoàn toàn khả năng kết nối mạng của các thiết bị mới. Việc hiểu rõ cách thức hoạt động của cuộc tấn công này giúp chúng ta có thể triển khai các biện pháp bảo vệ phù hợp như port security và DHCP snooping để ngăn chặn các cuộc tấn công tương tự.

Tags: DDOS, dhcp, DOS
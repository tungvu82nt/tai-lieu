# Cách quét lỗ hổng hệ thống bằng MITRE ATT&CK

MITRE ATT&CK là gì? Cùng mình tìm hiểu trong bài này nhé. Thời đại công nghệ ngày càng phát triển thì chúng ta càng nhận thức rõ hơn về tầm quan trọng của an ninh mạng. Sự nguy hiểm của tội phạm mạng cũng tăng theo từng năm. Để đối phó với việc này, những chuyên gia an ninh mạng đang bắt tay vào việc phát triển các công cụ bảo mật mới để chống lại tin tặc mỗi ngày. Trong số các công cụ này, có một Framework rất nổi tiếng là MITRE ATT&CK chứa các kỹ thuật, lỗ hổng và quy trình tấn công khác nhau để các tổ chức xác định các lỗ hổng trong hệ thống của họ.

## MITRE ATT&CK là gì?

MITRE ATT&CK (MITER AT&CK) là một framework mở chứa các chiến thuật và kỹ thuật tấn công trong thực tế. Framework này hoàn toàn miễn phí, nó cung cấp nhiều công cụ khác nhau để bảo vệ dữ liệu hoặc hệ thống an ninh.

Framework này cho phép chúng ta sử dụng chung một bộ nguyên tắc giao tiếp với các nhóm an ninh mạng khác gồm red team, blue team, SecOps,… Ngoài ra, nó cũng bắt chước hành vi và chiến thuật của kẻ tấn công nhằm giúp ta xác định rủi ro và chuẩn bị phương pháp phòng thủ để chống lại các cuộc tấn công có thể xảy ra. Vậy nên đây là một nguồn tài nguyên tuyệt vời dành cho các nhóm bảo mật CNTT.

Mặc dù nó mang lại rất nhiều lợi ích nhưng nó vẫn là một công cụ, nên nó không hoàn hảo. MITER AT&CK có một số hạn chế vì không phải tất cả các kỹ thuật đều độc hại, vậy nên nó có thể phát hiện một số kỹ thuật không phải là rủi ro thực sự.

Tuy nhiên, ưu điểm của nó lớn hơn nhược điểm mà nó mang lại. Vậy nên mình nghĩ bạn nên dùng thử, biết đâu nó lại có ích cho hệ thống của bạn.

## Cách sử dụng MITRE ATT&CK

Trên thực tế, Framework này chỉ mô tả và phân loại hành vi độc hại, vì vậy chúng ta cần một công cụ để áp dụng tất cả thông tin mà nó cung cấp.

Bạn có thể triển khai nó bằng cách ánh xạ hoặc tích hợp liên tục (CI/CD) bằng các công cụ an ninh mạng khác nhau. Phương pháp thông thường nhất là sử dụng các công cụ như Security Information and Event Management (SIEM) hoặc Cloud Access Security Broker (CASB).

Ngoài ra, bạn có thể triển khai nó trong môi trường CI/CD của mình bằng các công cụ như GitLab hoặc Jenkins.

## Sử dụng MITRE ATT&CK với Kubescape Cloud

Có rất nhiều công cụ khác nhau để quét và bảo mật hệ thống bằng MITRE ATT&CK. Nhưng trong bài viết này, mình sẽ sử dụng công cụ mã nguồn mở Kubescape.

Kubescape là một công cụ mã nguồn mở dùng để quét lỗ hổng bảo mật trên các cụm K8s và tệp YAML, nó kiểm tra các lỗ hổng phần mềm bằng cách sử dụng RBAC và phân tích rủi ro, đồng thời phát hiện cấu hình sai theo nhiều Framework khác nhau, bao gồm Khung MITRE ATT&CK.

### Demo đơn giản sử dụng Linux

Mình chỉ demo đơn giản vì theo nhu cầu của từng người thì quá trình sẽ khá khác nhau. Các bạn chỉ cần 3 bước để sử dụng Kubescape.

**Bước 1:** Tải Kubescape.

Mình sẽ tải Kubescape xuống máy có Kubectl. Vậy nên, bạn cần phải cài Kubectl và có cluster đang chạy. Sau đó, bạn chỉ cần mở terminal và chạy lệnh dưới:

```bash
curl -s https://raw.githubusercontent.com/kubescape/kubescape/master/install.sh | /bin/bash
```

**Bước 2:** Chạy kubescape. Sau khi cài đặt thành công Kubescape, bạn có thể quét hệ thống bằng lệnh dưới đây:

```bash
kubescape scan --submit
```

Như các bạn thấy, cluster mà mình tạo có khá nhiều rủi ro. Ngoài ra, bạn cũng có thể xuất kết quả quét sang định dạng PDF.

## Kết luận

MITRE ATT&CK là một framework mạnh mẽ giúp các tổ chức xác định và đánh giá các lỗ hổng bảo mật trong hệ thống của họ. Việc sử dụng các công cụ như Kubescape kết hợp với framework này sẽ giúp bạn có cái nhìn tổng quan về tình trạng bảo mật của hệ thống và đưa ra các biện pháp phòng chống phù hợp.

**Tags:** Framework, Kubectl, MITRE ATT&CK, rà quét lỗ hổng, scan, scan hệ thống
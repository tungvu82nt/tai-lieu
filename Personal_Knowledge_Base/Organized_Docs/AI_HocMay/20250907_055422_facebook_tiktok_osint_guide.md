# Hướng Dẫn Tra Cứu Thông Tin UID Facebook và Username TikTok

## 📋 Tổng Quan

Việc tra cứu thông tin từ UID Facebook và username TikTok có thể thực hiện thông qua nhiều công cụ OSINT (Open Source Intelligence) khác nhau. Dưới đây là danh sách các phương pháp và công cụ hiệu quả nhất.

## 🔍 Công Cụ Tra Cứu UID Facebook

### 1. **Lookup-id.com**
- **Link:** https://lookup-id.com/
- **Chức năng:** Tìm Facebook ID của bất kỳ profile hoặc Group nào
- **Cách sử dụng:** Nhập URL profile Facebook để lấy UID

### 2. **Facebook Graph Searcher**
- **Link:** https://intelx.io/tools?tab=facebook
- **Chức năng:** Tìm kiếm thông tin trên Facebook
- **Đặc điểm:** Sử dụng Facebook Graph API để tra cứu

### 3. **AnalyzeID**
- **Link:** https://analyzeid.com/
- **Chức năng:** Tìm kiếm các trang web có cùng chủ sở hữu
- **Đặc điểm:** Bao gồm khớp Facebook App ID

### 4. **Facebook Recover Lookup**
- **Link:** https://www.facebook.com/login/identify?ctx=recover
- **Chức năng:** Kiểm tra email/số điện thoại có liên kết với tài khoản Facebook
- **Cách dùng:** Nhập thông tin để kiểm tra sự tồn tại của tài khoản

### 5. **StalkFace**
- **Link:** https://stalkface.com/en/
- **Chức năng:** Bộ công cụ để theo dõi ai đó trên Facebook
- **Lưu ý:** Sử dụng có trách nhiệm và tuân thủ pháp luật

## 🎵 Công Cụ Tra Cứu Username TikTok

### 1. **Sherlock**
- **Cài đặt:**
  ```bash
  git clone https://github.com/sherlock-project/sherlock.git
  cd sherlock
  pip install -r requirements.txt
  ```
- **Sử dụng:**
  ```bash
  python sherlock.py [username]
  ```
- **Chức năng:** Tìm username trên 300+ mạng xã hội bao gồm TikTok

### 2. **FindUser**
- **Link:** https://github.com/xHak9x/finduser
- **Cài đặt:**
  ```bash
  git clone https://github.com/xHak9x/finduser.git
  cd finduser
  chmod +x finduser.sh
  ```
- **Sử dụng:**
  ```bash
  ./finduser.sh
  ```
- **Chức năng:** Tìm username trên 75+ mạng xã hội

### 3. **SocialScan**
- **Cài đặt:**
  ```bash
  pip install socialscan
  ```
- **Sử dụng:**
  ```bash
  socialscan [username]
  ```
- **Chức năng:** Kiểm tra tính khả dụng của username/email trên các platform

### 4. **Social Mapper**
- **Link:** https://github.com/Greenwolf/social_mapper
- **Chức năng:** Tìm kiếm profile qua nhận dạng khuôn mặt
- **Đặc điểm:** Sử dụng AI để tương quan profile qua các trang khác nhau

## 🛠️ Công Cụ OSINT Tổng Hợp

### 1. **Seekr**
- **Link:** https://github.com/seekr-osint/seekr
- **Đặc điểm:**
  - Không cần API key
  - Giao diện desktop thân thiện
  - Tích hợp nhiều công cụ OSINT
  - Tự động tìm kiếm và liên kết tài khoản
- **Cài đặt:**
  ```bash
  # Windows
  git clone https://github.com/seekr-osint/seekr
  cd seekr
  go generate ./...
  tsc --project web
  go run main.go
  ```

### 2. **TheHarvester**
- **Sử dụng:**
  ```bash
  theHarvester -d [domain] -l 100 -b google,bing,linkedin
  ```
- **Chức năng:** Thu thập emails, domains, IPs từ nguồn công khai

### 3. **Maltego**
- **Chức năng:** Phân tích OSINT và link analysis
- **Đặc điểm:** Giao diện đồ họa để điều tra và mapping mối quan hệ

## 📱 Phương Pháp Thủ Công

### Tra Cứu Facebook UID:
1. **Từ URL Profile:**
   - Mở profile Facebook
   - Xem source code (Ctrl+U)
   - Tìm kiếm "entity_id" hoặc "profile_id"

2. **Từ Graph API:**
   ```
   https://graph.facebook.com/[username]
   ```

3. **Từ Photo URL:**
   - Lấy URL của ảnh profile
   - UID thường nằm trong đường dẫn ảnh

### Tra Cứu TikTok Username:
1. **Kiểm tra Profile:**
   - Truy cập https://www.tiktok.com/@[username]
   - Kiểm tra thông tin công khai

2. **Tìm kiếm Cross-Platform:**
   - Sử dụng cùng username trên các platform khác
   - Kiểm tra bio và link liên kết

## ⚖️ Lưu Ý Pháp Lý và Đạo Đức

### ⚠️ Quan Trọng:
- **Tuân thủ pháp luật:** Chỉ sử dụng thông tin công khai
- **Tôn trọng quyền riêng tư:** Không xâm phạm thông tin cá nhân
- **Mục đích chính đáng:** Chỉ sử dụng cho mục đích nghiên cứu, bảo mật
- **Không lạm dụng:** Tránh harassment hoặc stalking

### 📋 Checklist Trước Khi Sử Dụng:
- [ ] Có mục đích chính đáng?
- [ ] Thông tin có công khai không?
- [ ] Có vi phạm Terms of Service không?
- [ ] Có tuân thủ GDPR/quy định bảo mật dữ liệu không?

## 🔧 Script Tự Động Hóa

### Script Kiểm Tra Username Đa Platform:
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script kiểm tra username trên nhiều platform
Tác giả: OSINT Specialist
"""

import requests
import json
from concurrent.futures import ThreadPoolExecutor

def check_tiktok_user(username):
    """
    Kiểm tra username TikTok có tồn tại không
    """
    url = f"https://www.tiktok.com/@{username}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return {"platform": "TikTok", "username": username, "exists": True, "url": url}
        else:
            return {"platform": "TikTok", "username": username, "exists": False, "url": url}
    except:
        return {"platform": "TikTok", "username": username, "exists": "Error", "url": url}

def check_facebook_user(username):
    """
    Kiểm tra username Facebook có tồn tại không
    """
    url = f"https://www.facebook.com/{username}"
    try:
        response = requests.get(url, timeout=10)
        if "This content isn't available right now" not in response.text:
            return {"platform": "Facebook", "username": username, "exists": True, "url": url}
        else:
            return {"platform": "Facebook", "username": username, "exists": False, "url": url}
    except:
        return {"platform": "Facebook", "username": username, "exists": "Error", "url": url}

def main():
    """
    Hàm chính để chạy kiểm tra
    """
    username = input("Nhập username cần kiểm tra: ")
    
    print(f"\n🔍 Đang kiểm tra username: {username}")
    print("=" * 50)
    
    # Chạy kiểm tra song song
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [
            executor.submit(check_tiktok_user, username),
            executor.submit(check_facebook_user, username)
        ]
        
        for future in futures:
            result = future.result()
            status = "✅ Tồn tại" if result["exists"] == True else "❌ Không tồn tại" if result["exists"] == False else "⚠️ Lỗi"
            print(f"{result['platform']}: {status} - {result['url']}")

if __name__ == "__main__":
    main()
```

### Cách Sử Dụng Script:
1. Lưu code vào file `username_checker.py`
2. Cài đặt dependencies: `pip install requests`
3. Chạy: `python username_checker.py`

## 📚 Tài Nguyên Bổ Sung

### Websites Hữu Ích:
- **OSINT Framework:** https://osintframework.com/
- **OSINT Tools:** https://osinttools.io/
- **Social Media OSINT Collection:** https://github.com/osintambition/Social-Media-OSINT-Tools-Collection

### Courses và Training:
- **OSINT Curious:** https://osintcurio.us/
- **Bellingcat Online Investigation Toolkit**
- **SANS FOR578: Cyber Threat Intelligence**

## 🔄 Cập Nhật và Bảo Trì

### Lưu Ý:
- Các API và phương thức có thể thay đổi theo thời gian
- Cần cập nhật công cụ thường xuyên
- Theo dõi thay đổi Terms of Service của các platform
- Backup dữ liệu quan trọng

---

**Tác giả:** Chuyên gia OSINT  
**Ngày tạo:** $(date)  
**Phiên bản:** 1.0  
**Giấy phép:** Chỉ sử dụng cho mục đích giáo dục và nghiên cứu  

---

*⚠️ Disclaimer: Tài liệu này chỉ mang tính chất giáo dục. Người sử dụng có trách nhiệm tuân thủ pháp luật và đạo đức khi sử dụng các công cụ và phương pháp được mô tả.*
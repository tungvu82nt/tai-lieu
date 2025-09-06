# Ultimate OSINT Toolkit - Hướng Dẫn Sử Dụng Chi Tiết

## Tổng Quan

Ultimate OSINT Toolkit là một bộ công cụ OSINT (Open Source Intelligence) toàn diện được phát triển bằng Python, tích hợp các công cụ và kỹ thuật thu thập thông tin từ nhiều nguồn khác nhau.

## Tính Năng Chính

### 🔍 Facebook OSINT
- Trích xuất UID từ URL Facebook
- Kiểm tra thông tin profile Facebook
- Xác minh email/số điện thoại có liên kết với Facebook
- Phân tích metadata từ trang Facebook

### 🎵 TikTok OSINT
- Kiểm tra sự tồn tại của username TikTok
- Tìm kiếm các biến thể username
- Thu thập thông tin profile TikTok
- Phân tích metadata từ trang TikTok

### 🌐 Cross-Platform Social Media OSINT
- Tìm kiếm username trên 12+ nền tảng mạng xã hội
- Kiểm tra sự tồn tại của tài khoản
- Tìm kiếm nâng cao với các biến thể username
- Hỗ trợ đa luồng để tăng tốc độ

### 📧 Email OSINT
- Phân tích cấu trúc email
- Xác định nhà cung cấp email
- Trích xuất tên có thể từ địa chỉ email
- Kiểm tra email breach (cần API key)

### 📱 Phone OSINT
- Phân tích số điện thoại
- Xác định mã quốc gia
- Phân tích cấu trúc số điện thoại
- Xác định loại số điện thoại

### 📊 Báo Cáo và Xuất Dữ Liệu
- Xuất báo cáo định dạng JSON
- Xuất báo cáo định dạng Markdown
- Tóm tắt kết quả tự động
- Timestamp và metadata đầy đủ

## Cài Đặt

### Yêu Cầu Hệ Thống
- Python 3.7+
- Windows/Linux/macOS
- Kết nối Internet

### Cài Đặt Dependencies

```bash
# Cài đặt các thư viện cần thiết
pip install requests beautifulsoup4 colorama

# Hoặc sử dụng requirements.txt
pip install -r requirements.txt
```

### Tạo File Requirements.txt

```txt
requests>=2.25.1
beautifulsoup4>=4.9.3
colorama>=0.4.4
lxml>=4.6.3
```

## Cách Sử Dụng

### 1. Chế Độ Command Line

#### Facebook OSINT
```bash
# Kiểm tra Facebook UID
python ultimate_osint_toolkit.py --facebook-uid 100012345678901

# Trích xuất UID từ URL
python ultimate_osint_toolkit.py --facebook-url "https://www.facebook.com/profile.php?id=100012345678901"
```

#### TikTok OSINT
```bash
# Kiểm tra TikTok username
python ultimate_osint_toolkit.py --tiktok-username "example_user"
```

#### Cross-Platform Search
```bash
# Tìm kiếm username trên nhiều nền tảng
python ultimate_osint_toolkit.py --username "example_user"

# Tìm kiếm nâng cao với biến thể
python ultimate_osint_toolkit.py --advanced-search "example_user"
```

#### Email và Phone Analysis
```bash
# Phân tích email
python ultimate_osint_toolkit.py --email "example@gmail.com"

# Phân tích số điện thoại
python ultimate_osint_toolkit.py --phone "+84901234567"
```

#### Xuất Báo Cáo
```bash
# Xuất báo cáo JSON (mặc định)
python ultimate_osint_toolkit.py --username "example" --output json

# Xuất báo cáo Markdown
python ultimate_osint_toolkit.py --username "example" --output md
```

### 2. Chế Độ Tương Tác

```bash
# Khởi động chế độ tương tác
python ultimate_osint_toolkit.py --interactive
```

Trong chế độ tương tác, bạn sẽ có menu lựa chọn:

```
=== CHỌN CHỨC NĂNG ===
1. Facebook OSINT
2. TikTok OSINT
3. Cross-Platform Username Search
4. Advanced Username Search
5. Email Analysis
6. Phone Analysis
0. Thoát
```

### 3. Sử Dụng Như Module Python

```python
from ultimate_osint_toolkit import FacebookOSINT, TikTokOSINT, SocialMediaOSINT

# Facebook OSINT
fb_osint = FacebookOSINT()
result = fb_osint.get_profile_info("100012345678901")
print(result)

# TikTok OSINT
tiktok_osint = TikTokOSINT()
result = tiktok_osint.get_user_info("example_user")
print(result)

# Cross-platform search
social_osint = SocialMediaOSINT()
results = social_osint.check_username_availability("example_user")
print(results)
```

## Các Nền Tảng Được Hỗ Trợ

| Nền Tảng | URL Pattern | Ghi Chú |
|----------|-------------|----------|
| Instagram | `https://www.instagram.com/{username}/` | ✅ Hoạt động |
| Twitter | `https://twitter.com/{username}` | ✅ Hoạt động |
| YouTube | `https://www.youtube.com/@{username}` | ✅ Hoạt động |
| GitHub | `https://github.com/{username}` | ✅ Hoạt động |
| LinkedIn | `https://www.linkedin.com/in/{username}/` | ⚠️ Rate limited |
| Reddit | `https://www.reddit.com/user/{username}` | ✅ Hoạt động |
| Pinterest | `https://www.pinterest.com/{username}/` | ✅ Hoạt động |
| Tumblr | `https://{username}.tumblr.com/` | ✅ Hoạt động |
| Medium | `https://medium.com/@{username}` | ✅ Hoạt động |
| Telegram | `https://t.me/{username}` | ⚠️ Limited info |
| Discord | `https://discord.com/users/{username}` | ⚠️ Limited info |
| Snapchat | `https://www.snapchat.com/add/{username}` | ⚠️ Limited info |

## Cấu Trúc Output

### JSON Output Example
```json
{
  "timestamp": "20241201_143022",
  "generated_at": "2024-12-01T14:30:22.123456",
  "total_targets": 1,
  "results": {
    "cross_platform": {
      "Instagram": {
        "platform": "Instagram",
        "url": "https://www.instagram.com/example_user/",
        "status_code": 200,
        "accessible": true,
        "exists": true
      },
      "Twitter": {
        "platform": "Twitter",
        "url": "https://twitter.com/example_user",
        "status_code": 404,
        "accessible": true,
        "exists": false
      }
    }
  },
  "summary": {
    "total_searches": 12,
    "successful_finds": 3,
    "platforms_found": {
      "Instagram": 1,
      "GitHub": 1,
      "Reddit": 1
    },
    "errors": 0
  }
}
```

### Markdown Output Example
```markdown
# Báo cáo OSINT

**Thời gian tạo:** 2024-12-01T14:30:22.123456

**Tổng số mục tiêu:** 1

## Tóm tắt

- Tổng số tìm kiếm: 12
- Tìm thấy thành công: 3
- Lỗi: 0

## Chi tiết Kết quả

### example_user

- ✅ **Instagram**: https://www.instagram.com/example_user/
- ❌ **Twitter**: Không tồn tại
- ✅ **GitHub**: https://github.com/example_user
```

## Tính Năng Nâng Cao

### 1. Rate Limiting
Công cụ tự động áp dụng rate limiting để tránh bị chặn:
- Delay 1-2 giây giữa các request
- Sử dụng ThreadPoolExecutor với max_workers=5
- Retry mechanism cho failed requests

### 2. Error Handling
- Comprehensive exception handling
- Detailed error logging
- Graceful degradation khi một service không khả dụng

### 3. Customizable Headers
- User-Agent rotation
- Custom headers cho từng platform
- Session management

### 4. Advanced Search Patterns
Tự động tạo các biến thể username:
- `username`
- `username_official`
- `official_username`
- `username1`, `username2`, `username3`
- `username_`, `_username`
- Loại bỏ dấu chấm, gạch dưới, gạch ngang

## Lưu Ý Bảo Mật và Pháp Lý

### ⚠️ Quan Trọng
1. **Chỉ sử dụng cho mục đích hợp pháp**: Nghiên cứu, bảo mật, điều tra hợp pháp
2. **Tuân thủ Terms of Service**: Của các nền tảng mạng xã hội
3. **Respect Privacy**: Không sử dụng để quấy rối hoặc xâm phạm quyền riêng tư
4. **Rate Limiting**: Không spam requests
5. **Data Protection**: Bảo vệ dữ liệu thu thập được

### Disclaimer
```
Công cụ này được phát triển cho mục đích giáo dục và nghiên cứu bảo mật.
Người sử dụng chịu trách nhiệm đảm bảo việc sử dụng tuân thủ pháp luật
và các quy định hiện hành. Tác giả không chịu trách nhiệm cho việc
sử dụng sai mục đích hoặc bất hợp pháp.
```

## Troubleshooting

### Lỗi Thường Gặp

#### 1. Import Error
```bash
ModuleNotFoundError: No module named 'requests'
```
**Giải pháp:**
```bash
pip install requests beautifulsoup4 colorama
```

#### 2. Connection Error
```
ConnectionError: Failed to establish a new connection
```
**Giải pháp:**
- Kiểm tra kết nối Internet
- Kiểm tra firewall/proxy settings
- Thử lại sau vài phút

#### 3. Rate Limited
```
HTTP 429: Too Many Requests
```
**Giải pháp:**
- Tăng delay giữa các requests
- Sử dụng proxy/VPN
- Chờ và thử lại sau

#### 4. Blocked by Platform
```
HTTP 403: Forbidden
```
**Giải pháp:**
- Thay đổi User-Agent
- Sử dụng proxy
- Giảm tần suất requests

### Debug Mode
Thêm logging chi tiết:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Mở Rộng và Tùy Chỉnh

### Thêm Nền Tảng Mới
```python
class CustomPlatformOSINT(OSINTToolkit):
    def __init__(self):
        super().__init__()
        self.base_url = "https://example.com"
        
    def check_user(self, username):
        # Implementation here
        pass
```

### Thêm Phương Thức Phân Tích
```python
def custom_analysis(self, data):
    # Custom analysis logic
    return processed_data
```

### Integration với APIs Khác
```python
# HaveIBeenPwned API
# Shodan API
# VirusTotal API
# etc.
```

## Performance Optimization

### 1. Async/Await Support
```python
import asyncio
import aiohttp

# Async implementation for better performance
```

### 2. Caching
```python
import functools

@functools.lru_cache(maxsize=128)
def cached_request(url):
    # Cached requests
    pass
```

### 3. Database Storage
```python
import sqlite3

# Store results in database for analysis
```

## Roadmap

### Version 2.0 Features
- [ ] Async/await support
- [ ] Database integration
- [ ] Web interface
- [ ] API endpoints
- [ ] Machine learning analysis
- [ ] Advanced visualization
- [ ] Plugin system
- [ ] Docker containerization

### Additional Platforms
- [ ] WhatsApp Business
- [ ] Signal
- [ ] Clubhouse
- [ ] Twitch
- [ ] OnlyFans
- [ ] Patreon

## Đóng Góp

Chúng tôi hoan nghênh mọi đóng góp! Vui lòng:

1. Fork repository
2. Tạo feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

### Coding Standards
- PEP 8 compliance
- Type hints
- Comprehensive docstrings
- Unit tests
- Error handling

## License

MIT License - Xem file LICENSE để biết chi tiết.

## Liên Hệ

- **Email**: support@osint-toolkit.com
- **GitHub**: https://github.com/osint-toolkit
- **Documentation**: https://docs.osint-toolkit.com

---

**Cập nhật lần cuối**: 01/12/2024
**Phiên bản**: 1.0.0
**Tác giả**: AI Assistant
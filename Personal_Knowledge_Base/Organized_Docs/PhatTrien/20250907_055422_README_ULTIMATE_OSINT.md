# Ultimate OSINT Toolkit Collection

## 🎯 Tổng Quan

Bộ sưu tập công cụ OSINT (Open Source Intelligence) toàn diện được phát triển để hỗ trợ việc thu thập thông tin từ các nguồn mở một cách hiệu quả và có hệ thống. Bộ công cụ này tích hợp nhiều kỹ thuật và phương pháp OSINT khác nhau, từ cơ bản đến nâng cao.

## 📁 Cấu Trúc Dự Án

```
d:\A1\1\
├── ultimate_osint_toolkit.py          # Bộ công cụ OSINT chính
├── osint_demo.py                      # Script demo và test
├── OSINT_TOOLKIT_GUIDE.md             # Hướng dẫn chi tiết
├── comprehensive_osint_tools_guide.md # Tổng hợp công cụ OSINT
├── requirements.txt                   # Dependencies
└── README_ULTIMATE_OSINT.md          # File này
```

## 🚀 Bắt Đầu Nhanh

### 1. Cài Đặt Dependencies

```bash
# Cài đặt các thư viện cần thiết
pip install -r requirements.txt

# Hoặc cài đặt thủ công
pip install requests beautifulsoup4 colorama lxml
```

### 2. Chạy Demo

```bash
# Chạy demo tương tác
python osint_demo.py

# Hoặc chạy demo đầy đủ
python osint_demo.py --full
```

### 3. Sử Dụng Toolkit

```bash
# Chế độ tương tác
python ultimate_osint_toolkit.py --interactive

# Tìm kiếm username trên nhiều nền tảng
python ultimate_osint_toolkit.py --username "example_user"

# Kiểm tra Facebook profile
python ultimate_osint_toolkit.py --facebook-uid "100012345678901"

# Phân tích email
python ultimate_osint_toolkit.py --email "example@gmail.com"
```

## 🛠️ Tính Năng Chính

### 🔍 Facebook OSINT
- ✅ Trích xuất UID từ URL Facebook
- ✅ Kiểm tra thông tin profile
- ✅ Xác minh email/phone liên kết
- ✅ Phân tích metadata

### 🎵 TikTok OSINT
- ✅ Kiểm tra username existence
- ✅ Tìm kiếm biến thể username
- ✅ Thu thập profile information
- ✅ Metadata analysis

### 🌐 Cross-Platform Social Media
- ✅ 12+ nền tảng được hỗ trợ
- ✅ Tìm kiếm đồng thời
- ✅ Advanced username variations
- ✅ Multi-threading support

### 📧 Email Intelligence
- ✅ Email structure analysis
- ✅ Provider identification
- ✅ Name extraction
- ✅ Breach checking (với API)

### 📱 Phone Intelligence
- ✅ Number format analysis
- ✅ Country code detection
- ✅ Carrier identification
- ✅ Type classification

### 📊 Reporting & Export
- ✅ JSON format export
- ✅ Markdown reports
- ✅ Automatic summaries
- ✅ Timestamp tracking

## 🎮 Hướng Dẫn Sử Dụng

### Demo Script

```bash
# Chạy demo tương tác
python osint_demo.py
```

Demo script cung cấp:
- Test tất cả tính năng
- Ví dụ thực tế
- Kết quả mẫu
- Error handling demo

### Command Line Usage

```bash
# Facebook OSINT
python ultimate_osint_toolkit.py --facebook-uid "zuck"
python ultimate_osint_toolkit.py --facebook-url "https://facebook.com/zuck"

# TikTok OSINT
python ultimate_osint_toolkit.py --tiktok-username "charlidamelio"

# Cross-platform search
python ultimate_osint_toolkit.py --username "github"
python ultimate_osint_toolkit.py --advanced-search "admin"

# Email & Phone
python ultimate_osint_toolkit.py --email "test@gmail.com"
python ultimate_osint_toolkit.py --phone "+84901234567"

# Export options
python ultimate_osint_toolkit.py --username "test" --output json
python ultimate_osint_toolkit.py --username "test" --output md
```

### Python Module Usage

```python
from ultimate_osint_toolkit import FacebookOSINT, SocialMediaOSINT

# Facebook OSINT
fb = FacebookOSINT()
result = fb.get_profile_info("zuck")
print(result)

# Social Media Search
social = SocialMediaOSINT()
results = social.check_username_availability("github")
for platform, info in results.items():
    if info.get('exists'):
        print(f"Found on {platform}: {info['url']}")
```

## 🌟 Các Nền Tảng Được Hỗ Trợ

| Platform | Status | Notes |
|----------|--------|-------|
| 📷 Instagram | ✅ Active | Full support |
| 🐦 Twitter | ✅ Active | Full support |
| 📺 YouTube | ✅ Active | Full support |
| 💻 GitHub | ✅ Active | Full support |
| 💼 LinkedIn | ⚠️ Limited | Rate limited |
| 🤖 Reddit | ✅ Active | Full support |
| 📌 Pinterest | ✅ Active | Full support |
| 📝 Tumblr | ✅ Active | Full support |
| ✍️ Medium | ✅ Active | Full support |
| 💬 Telegram | ⚠️ Limited | Public channels only |
| 🎮 Discord | ⚠️ Limited | Limited info |
| 👻 Snapchat | ⚠️ Limited | Limited info |

## 📈 Kết Quả Mẫu

### JSON Output
```json
{
  "timestamp": "20241201_143022",
  "results": {
    "cross_platform": {
      "Instagram": {
        "exists": true,
        "url": "https://www.instagram.com/github/",
        "accessible": true
      },
      "GitHub": {
        "exists": true,
        "url": "https://github.com/github",
        "accessible": true
      }
    }
  },
  "summary": {
    "total_searches": 12,
    "successful_finds": 2,
    "platforms_found": ["Instagram", "GitHub"]
  }
}
```

### Markdown Report
```markdown
# Báo cáo OSINT

## Tóm tắt
- Tổng số tìm kiếm: 12
- Tìm thấy thành công: 2
- Lỗi: 0

## Chi tiết Kết quả

### github
- ✅ **Instagram**: https://www.instagram.com/github/
- ✅ **GitHub**: https://github.com/github
- ❌ **Twitter**: Không tồn tại
```

## 🔧 Tùy Chỉnh và Mở Rộng

### Thêm Nền Tảng Mới

```python
class CustomPlatformOSINT(OSINTToolkit):
    def __init__(self):
        super().__init__()
        self.platforms['NewPlatform'] = 'https://newplatform.com/{}'
    
    def check_custom_platform(self, username):
        # Custom implementation
        pass
```

### Custom Analysis

```python
def custom_email_analysis(email):
    # Your custom logic
    return analysis_result
```

### API Integration

```python
# HaveIBeenPwned
# Shodan
# VirusTotal
# Custom APIs
```

## 📚 Tài Liệu Tham Khảo

### Files Included
1. **`OSINT_TOOLKIT_GUIDE.md`** - Hướng dẫn chi tiết đầy đủ
2. **`comprehensive_osint_tools_guide.md`** - Tổng hợp công cụ OSINT
3. **`ultimate_osint_toolkit.py`** - Source code chính
4. **`osint_demo.py`** - Demo và test script

### External Resources
- [OSINT Framework](https://osintframework.com/)
- [Awesome OSINT](https://github.com/jivoi/awesome-osint)
- [OSINT Techniques](https://www.osinttechniques.com/)

## ⚠️ Lưu Ý Quan Trọng

### Pháp Lý và Đạo Đức
- ✅ Chỉ sử dụng cho mục đích hợp pháp
- ✅ Tuân thủ Terms of Service
- ✅ Respect privacy và GDPR
- ✅ Không harassment hoặc stalking
- ✅ Educational purposes only

### Kỹ Thuật
- ⚠️ Rate limiting để tránh bị block
- ⚠️ Sử dụng proxy khi cần thiết
- ⚠️ Error handling và retry logic
- ⚠️ Data protection và encryption

### Disclaimer
```
Công cụ này được phát triển cho mục đích giáo dục và nghiên cứu bảo mật.
Người sử dụng chịu trách nhiệm đảm bảo việc sử dụng tuân thủ pháp luật
và các quy định hiện hành. Tác giả không chịu trách nhiệm cho việc
sử dụng sai mục đích hoặc bất hợp pháp.
```

## 🐛 Troubleshooting

### Lỗi Thường Gặp

#### Import Error
```bash
ModuleNotFoundError: No module named 'requests'
# Giải pháp: pip install requests beautifulsoup4 colorama
```

#### Connection Error
```bash
ConnectionError: Failed to establish connection
# Giải pháp: Kiểm tra internet, firewall, proxy
```

#### Rate Limited
```bash
HTTP 429: Too Many Requests
# Giải pháp: Tăng delay, sử dụng proxy, chờ và retry
```

### Debug Mode
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🚀 Performance Tips

### Optimization
- Sử dụng threading cho multiple requests
- Implement caching cho repeated queries
- Rate limiting để tránh blocks
- Connection pooling

### Best Practices
- Validate input data
- Handle exceptions gracefully
- Log activities for audit
- Secure API keys
- Regular updates

## 🔮 Roadmap

### Version 2.0 Features
- [ ] Async/await support
- [ ] Web interface
- [ ] Database integration
- [ ] Machine learning analysis
- [ ] Advanced visualization
- [ ] Plugin architecture
- [ ] Docker containerization
- [ ] API endpoints

### Additional Platforms
- [ ] WhatsApp Business
- [ ] Signal
- [ ] Clubhouse
- [ ] Twitch
- [ ] OnlyFans
- [ ] Patreon
- [ ] VKontakte
- [ ] Weibo

## 🤝 Đóng Góp

Chúng tôi hoan nghênh mọi đóng góp!

### Cách Đóng Góp
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

## 📞 Hỗ Trợ

### Liên Hệ
- **GitHub Issues**: Báo cáo bugs và feature requests
- **Documentation**: Đọc hướng dẫn chi tiết
- **Community**: Tham gia discussions

### FAQ

**Q: Có cần API keys không?**
A: Một số tính năng như breach checking cần API keys, nhưng hầu hết tính năng hoạt động mà không cần.

**Q: Có an toàn không?**
A: Có, công cụ chỉ thu thập thông tin công khai và tuân thủ rate limits.

**Q: Có thể chạy trên mobile không?**
A: Hiện tại chỉ hỗ trợ desktop, mobile support sẽ có trong tương lai.

**Q: Làm sao để thêm nền tảng mới?**
A: Xem phần "Tùy chỉnh và Mở rộng" trong hướng dẫn.

## 📄 License

MIT License - Xem file LICENSE để biết chi tiết.

## 🙏 Acknowledgments

- Cảm ơn cộng đồng OSINT
- Các nhà phát triển open source tools
- Security researchers
- Beta testers và contributors

---

**Phiên bản**: 1.0.0  
**Cập nhật lần cuối**: 01/12/2024  
**Tác giả**: AI Assistant  
**Ngôn ngữ**: Python 3.7+  
**Platform**: Cross-platform  

---

*Happy OSINT Hunting! 🕵️‍♂️*
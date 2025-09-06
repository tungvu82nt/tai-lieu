# Hướng dẫn Toàn diện về Công cụ OSINT và Mạng Xã hội

**Tác giả:** AI Assistant  
**Ngày tạo:** $(Get-Date -Format "dd/MM/yyyy")  
**Mô tả:** Tổng hợp chi tiết các công cụ OSINT, mạng xã hội và thu thập thông tin từ nhiều nguồn khác nhau

---

## 📋 Mục lục

1. [Công cụ OSINT Chuyên dụng](#công-cụ-osint-chuyên-dụng)
2. [Công cụ Mạng Xã hội](#công-cụ-mạng-xã-hội)
3. [Công cụ Thu thập Thông tin](#công-cụ-thu-thập-thông-tin)
4. [Công cụ Phân tích và Điều tra](#công-cụ-phân-tích-và-điều-tra)
5. [Công cụ Tự động hóa](#công-cụ-tự-động-hóa)
6. [Script và Tool tùy chỉnh](#script-và-tool-tùy-chỉnh)
7. [Tài nguyên và Framework](#tài-nguyên-và-framework)

---

## 🔍 Công cụ OSINT Chuyên dụng

### 1. **Seekr** - Thu thập & quản lý dữ liệu OSINT
**Nguồn:** `anony/seekr-thu-thap-quan-ly-du-lieu-osint.md`

**Mô tả:** Bộ công cụ đa năng được thiết kế để thu thập và quản lý dữ liệu OSINT thông qua giao diện web trực quan.

**Tính năng chính:**
- KHÔNG yêu cầu API key cho tất cả các tính năng
- Giao diện Desktop quen thuộc và dễ sử dụng
- Cơ sở dữ liệu cho các mục tiêu OSINT được lưu trữ hiệu quả
- Tích hợp nhiều công cụ OSINT phổ biến (phoneinfoga)
- Tìm kiếm thông tin liên quan đến địa chỉ email trên GitHub
- Thẻ tài khoản cho mỗi người trong cơ sở dữ liệu
- Tự động tìm kiếm và liên kết các tài khoản trực tuyến

**Cài đặt:**
```bash
# Windows (bản không ổn định)
git clone https://github.com/seekr-osint/seekr
cd seekr
go generate ./...
tsc --project web
go run main.go

# Docker
docker pull ghcr.io/seekr-osint/seekr:latest
docker run -p 8569:8569 ghcr.io/seekr-osint/seekr:latest

# Linux
git clone https://github.com/seekr-osint/seekr
cd seekr
go generate ./...
tsc --project web
go run main.go
```

### 2. **MyIP** - Công cụ kiểm tra thông tin IP toàn diện
**Nguồn:** `anony/myip-cong-cu-kiem-tra-thong-tin-ip-toan-dien.md`

**Mô tả:** Công cụ kiểm tra mạng toàn diện giúp người dùng thấu hiểu và quản lý kết nối internet.

**Tính năng chính:**
- Hiển thị địa chỉ IP (IPv4 và IPv6)
- Thông tin IP chi tiết (quốc gia, khu vực, ASN, vị trí địa lý)
- Kiểm tra tình khả dụng của các trang web
- Phát hiện WebRTC
- Kiểm tra rò rỉ DNS
- Kiểm tra tốc độ mạng
- Kiểm tra quy tắc proxy
- Kiểm tra độ trễ toàn cầu
- MTR Test
- DNS Resolver
- Kiểm tra kiểm duyệt
- Tra cứu Whois
- Tra cứu địa chỉ MAC

**Cài đặt:**
```bash
# Node.js
git clone https://github.com/jason5ng32/MyIP.git
npm install && npm run build
npm start

# Docker
docker run -d -p 18966:18966 --name myip --restart always jason5ng32/myip:latest
```

### 3. **BigBountyRecon** - Công cụ do thám bằng Google Dork
**Nguồn:** `anony/bigbountyrecon-cong-cu-do-tham-bang-google-dork.md`

**Mô tả:** Sử dụng 58 kỹ thuật khác nhau bằng các công cụ mã nguồn mở và Google Dorks để đẩy nhanh quá trình do thám mục tiêu.

**Kỹ thuật chính:**
1. **Danh sách thư mục** - Tìm các thư mục mở
2. **Tệp cấu hình** - Tìm thông tin nhạy cảm
3. **Tệp cơ sở dữ liệu** - Truy cập dữ liệu nhạy cảm
4. **WordPress** - Phát hiện lỗ hổng plugin
5. **Tệp nhật ký** - Thông tin hoạt động người dùng
6. **Tệp sao lưu và tệp cũ** - Bản sao gốc hệ thống
7. **Trang đăng nhập** - Xác định điểm truy cập
8. **Lỗi SQL** - Rò rỉ thông tin hệ thống
9. **Tệp cấu hình Apache** - Chuỗi kết nối DB
10. **Tệp Robots.txt** - Thư mục và tệp ẩn

---

## 👥 Công cụ Mạng Xã hội

### 1. **Sherlock** - Hunt down social media accounts
**Nguồn:** `kali/kali_tools_detailed.md`, `kali/Social-Engineering/README.md`

**Mô tả:** Tìm kiếm tài khoản mạng xã hội theo username trên hơn 300 mạng xã hội.

**Sử dụng:**
```bash
sherlock target_username
```

### 2. **Social Media Finder Tools** (từ hackingtool)
**Nguồn:** `hackingtool/tools/others/socialmedia_finder.py`

**Các công cụ bao gồm:**

#### **FacialFind**
- **Chức năng:** Tìm kiếm bằng nhận dạng khuôn mặt
- **Mô tả:** Facial recognition search engine

#### **FindUser**
- **Chức năng:** Tìm username trên 75+ mạng xã hội
- **Cài đặt:**
```bash
git clone https://github.com/xHak9x/finduser.git
cd finduser
pip3 install -r requirements.txt
```
- **Sử dụng:**
```bash
python3 finduser.py username
```

#### **SocialScan**
- **Chức năng:** Kiểm tra tính khả dụng của username hoặc email
- **Cài đặt:**
```bash
pip3 install socialscan
```
- **Sử dụng:**
```bash
socialscan username email@example.com
```

### 3. **PyPhisher** - Công cụ phishing với 65 trang web
**Nguồn:** `anony/pyphisher-cong-cu-phishing-de-su-dung-voi-65-trang-web-co-san.md`

**Mô tả:** Công cụ lừa đảo cuối cùng trong Python với các trang web phổ biến.

**Tính năng:**
- 65 mẫu trang web
- Đường hầm kép (Ngrok và Cloudflared)
- Tạo mặt nạ URL
- Tùy chỉnh URL
- Nhận địa chỉ IP và thông tin chi tiết

**Cài đặt:**
```bash
git clone https://github.com/KasRoudra/PyPhisher
cd PyPhisher
python3 pyphisher.py
```

---

## 🔍 Công cụ Thu thập Thông tin

### 1. **TheHarvester** - OSINT information gathering
**Nguồn:** `kali/Social-Engineering/README.md`

**Mô tả:** Thu thập emails, domains, IPs từ public sources.

**Sử dụng:**
```bash
# Email collection
theHarvester -d company.com -l 200 -b google,bing,linkedin

# LinkedIn enumeration
theHarvester -d company.com -l 100 -b linkedin

# Domain information
theHarvester -d example.com -l 500 -b all
```

### 2. **Maltego** - OSINT và link analysis
**Nguồn:** `kali/kali_tools_detailed.md`, `kali/Social-Engineering/README.md`

**Mô tả:** Visual intelligence platform cho OSINT và relationship mapping.

**Sử dụng:**
```bash
maltego
```

### 3. **Information Gathering Tools** (từ hackingtool)
**Nguồn:** `hackingtool/tools/information_gathering_tools.py`

#### **NMAP** - Network scanning
```bash
sudo nmap -O -Pn target_ip
```

#### **Dracnmap** - Network exploitation với NMAP
```bash
git clone https://github.com/Screetsec/Dracnmap.git
cd Dracnmap && chmod +x dracnmap-v2.2.sh
sudo ./dracnmap-v2.2.sh
```

#### **RedHawk** - All In One Scanning
```bash
git clone https://github.com/Tuhinshubhra/RED_HAWK.git
cd RED_HAWK
php rhawk.php
```

#### **ReconSpider** - Advanced OSINT Framework
```bash
git clone https://github.com/bhavsec/reconspider.git
cd reconspider
sudo python3 setup.py install
python3 reconspider.py
```

#### **Infoga** - Email OSINT
```bash
git clone https://github.com/m4ll0k/Infoga.git
cd Infoga
sudo python3 setup.py install
python3 infoga.py
```

#### **ReconDog** - Information Gathering Suite
```bash
git clone https://github.com/s0md3v/ReconDog.git
cd ReconDog
sudo python dog
```

#### **Striker** - Recon & Vulnerability Scanning
```bash
git clone https://github.com/s0md3v/Striker.git
cd Striker
pip3 install -r requirements.txt
sudo python3 striker.py example.com
```

#### **SecretFinder** - API keys và sensitive data
```bash
git clone https://github.com/m4ll0k/SecretFinder.git secretfinder
cd secretfinder
sudo pip3 install -r requirements.txt
```

#### **Shodan** - IP information
```bash
git clone https://github.com/m4ll0k/Shodanfy.py.git
```

#### **Breacher** - Admin panel finder
```bash
git clone https://github.com/s0md3v/Breacher.git
cd Breacher
python3 breacher.py -u example.com
```

---

## 📊 Công cụ Phân tích và Điều tra

### 1. **SpiderFoot** - OSINT automation tool
**Nguồn:** `kali/kali_tools_list.md`

**Sử dụng:**
```bash
spiderfoot
spiderfoot-cli
```

### 2. **Amass** - Lập bản đồ bề mặt tấn công
**Nguồn:** `kali/kali_tools_categories.md`

### 3. **Recon-ng** - Framework trinh sát web
**Nguồn:** `kali/kali_tools_categories.md`

### 4. **Subfinder** - Subdomain discovery tool
**Nguồn:** `kali/kali_tools_list.md`

```bash
subfinder
```

---

## 🤖 Công cụ Tự động hóa

### 1. **Social Media OSINT Tool** (Tự phát triển)
**Nguồn:** `social_media_osint_tool.py`

**Tính năng:**
- Tra cứu Facebook UID
- Kiểm tra TikTok username
- Tìm kiếm cross-platform
- Lưu kết quả JSON
- Chế độ command line và interactive

**Sử dụng:**
```bash
python social_media_osint_tool.py --facebook-uid 123456789
python social_media_osint_tool.py --tiktok-username example_user
python social_media_osint_tool.py --cross-search username
```

### 2. **Quick Demo Tool** (Tự phát triển)
**Nguồn:** `quick_demo.py`

**Tính năng:**
- Demo nhanh các tính năng
- Kiểm tra Facebook UID
- Kiểm tra TikTok username
- Cross-platform check

---

## 📚 Script và Tool tùy chỉnh

### 1. **Facebook & TikTok OSINT Scripts**

#### **Facebook UID Extraction**
```python
def extract_uid_from_url(self, url):
    """Trích xuất UID từ URL Facebook"""
    patterns = [
        r'facebook\.com/profile\.php\?id=(\d+)',
        r'facebook\.com/([^/]+)/?$',
        r'fb\.me/([^/]+)'
    ]
    # Implementation...
```

#### **TikTok Username Validation**
```python
def get_user_info(self, username):
    """Lấy thông tin người dùng TikTok"""
    try:
        url = f"https://www.tiktok.com/@{username}"
        response = requests.get(url, headers=self.headers, timeout=10)
        # Implementation...
    except Exception as e:
        return {"error": str(e)}
```

### 2. **Cross-Platform Search**
```python
def search_cross_platform(self, username):
    """Tìm kiếm username trên nhiều nền tảng"""
    platforms = {
        'Instagram': f'https://www.instagram.com/{username}/',
        'Twitter': f'https://twitter.com/{username}',
        'YouTube': f'https://www.youtube.com/@{username}',
        'GitHub': f'https://github.com/{username}',
        'LinkedIn': f'https://www.linkedin.com/in/{username}/',
        'Reddit': f'https://www.reddit.com/user/{username}',
        'Pinterest': f'https://www.pinterest.com/{username}/',
        'Tumblr': f'https://{username}.tumblr.com/'
    }
    # Implementation...
```

---

## 🌐 Tài nguyên và Framework

### 1. **OSINT Framework**
- **URL:** https://osintframework.com/
- **Mô tả:** Tổng hợp các công cụ OSINT theo danh mục

### 2. **Social Media OSINT Tools Collection**
- **GitHub:** osintambition/Social-Media-OSINT-Tools-Collection
- **Bao gồm:** Công cụ cho Facebook, Instagram, LinkedIn, Twitter, TikTok

### 3. **Kali Linux Tools**
- **URL:** https://www.kali.org/tools/
- **Mô tả:** Danh sách đầy đủ các công cụ trong Kali Linux

### 4. **Facebook OSINT Tools**
- **Lookup-id.com** - Tìm Facebook ID
- **Social Searcher** - Theo dõi đề cập công khai
- **Who posted this** - Tìm kiếm từ khóa
- **AnalyzeID** - Phân tích Facebook ID
- **Facebook Graph Searcher** - Tìm kiếm Graph API
- **StalkFace** - Thu thập thông tin profile

### 5. **TikTok OSINT Tools**
- **TikTok Scraper** - Thu thập dữ liệu TikTok
- **TikTok Username Checker** - Kiểm tra tính khả dụng
- **TikTok Analytics Tools** - Phân tích engagement

---

## ⚖️ Lưu ý Pháp lý và Đạo đức

### **Nguyên tắc Sử dụng:**
1. **Chỉ sử dụng cho mục đích hợp pháp** - Nghiên cứu, giáo dục, bảo mật
2. **Tôn trọng quyền riêng tư** - Không xâm phạm thông tin cá nhân
3. **Tuân thủ Terms of Service** - Của các nền tảng mạng xã hội
4. **Không lạm dụng** - Tránh spam hoặc overload servers
5. **Báo cáo có trách nhiệm** - Nếu phát hiện lỗ hổng bảo mật

### **Khuyến nghị:**
- Sử dụng VPN khi cần thiết
- Implement rate limiting
- Respect robots.txt
- Sử dụng User-Agent hợp lệ
- Lưu trữ dữ liệu an toàn

---

## 🔧 Cài đặt và Cấu hình

### **Requirements chung:**
```bash
# Python packages
pip install requests beautifulsoup4 lxml selenium
pip install social-analyzer sherlock-project

# System tools
sudo apt update
sudo apt install nmap curl wget git python3 python3-pip
sudo apt install nodejs npm golang-go

# Browser automation
pip install selenium webdriver-manager
```

### **Docker Setup:**
```bash
# Pull essential OSINT tools
docker pull kalilinux/kali-rolling
docker pull ghcr.io/seekr-osint/seekr:latest
docker pull jason5ng32/myip:latest

# Run containers
docker run -it kalilinux/kali-rolling
docker run -p 8569:8569 ghcr.io/seekr-osint/seekr:latest
docker run -p 18966:18966 jason5ng32/myip:latest
```

---

## 📈 Best Practices

### **1. Workflow OSINT hiệu quả:**
1. **Reconnaissance** - Thu thập thông tin cơ bản
2. **Enumeration** - Liệt kê chi tiết
3. **Analysis** - Phân tích và correlation
4. **Verification** - Xác minh thông tin
5. **Documentation** - Ghi chép và báo cáo

### **2. Automation Tips:**
- Sử dụng caching để tránh duplicate requests
- Implement retry logic với exponential backoff
- Use async/await cho performance tốt hơn
- Log tất cả activities
- Backup dữ liệu định kỳ

### **3. Security Considerations:**
- Không hardcode credentials
- Sử dụng environment variables
- Encrypt sensitive data
- Regular security updates
- Monitor for suspicious activities

---

## 🎯 Kết luận

Bộ công cụ OSINT và mạng xã hội này cung cấp một arsenal toàn diện cho việc thu thập, phân tích và quản lý thông tin từ các nguồn mở. Từ các công cụ chuyên dụng như Seekr và MyIP đến các framework mạnh mẽ như Maltego và TheHarvester, người dùng có thể thực hiện các cuộc điều tra OSINT hiệu quả và chuyên nghiệp.

**Lưu ý quan trọng:** Tất cả các công cụ này phải được sử dụng một cách có trách nhiệm và tuân thủ các quy định pháp lý hiện hành. Mục đích chính là giáo dục, nghiên cứu bảo mật và các hoạt động hợp pháp.

---

**Tags:** OSINT, Social Media, Information Gathering, Cybersecurity, Reconnaissance, Facebook, TikTok, Instagram, Twitter, LinkedIn

**Nguồn tham khảo:**
- Kali Linux Tools Documentation
- HackingTool Repository
- AnonyViet Articles
- OSINT Framework
- Social Media OSINT Tools Collection
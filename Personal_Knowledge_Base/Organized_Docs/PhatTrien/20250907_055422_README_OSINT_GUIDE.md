# 🔍 Hướng Dẫn Toàn Diện: Tra Cứu Facebook UID & TikTok Username

## 📋 Tổng Quan

Repo này cung cấp các công cụ và phương pháp toàn diện để tra cứu thông tin từ:
- **Facebook UID** (User ID)
- **TikTok Username**
- **Cross-platform social media investigation**

## 🚀 Cài Đặt Nhanh

### Yêu Cầu Hệ Thống
```bash
# Python 3.7+
pip install requests
pip install beautifulsoup4
pip install lxml
```

### Sử Dụng Script Chính
```bash
# Chạy interactive mode
python social_media_osint_tool.py

# Tra cứu Facebook UID
python social_media_osint_tool.py --facebook-uid 100012345678901

# Tra cứu TikTok username
python social_media_osint_tool.py --tiktok-username username123

# Cross-platform search
python social_media_osint_tool.py --cross-search username123

# Lưu kết quả
python social_media_osint_tool.py --facebook-uid 123456 --save results.json
```

## 🎯 Các Phương Pháp Tra Cứu

### 1. Facebook UID Investigation

#### A. Công Cụ Online

**🔗 Lookup-id.com**
- URL: https://lookup-id.com/
- Tính năng: Chuyển đổi Facebook URL thành UID và ngược lại
- Cách dùng: Paste URL profile Facebook để lấy UID

**🔗 Facebook Graph Searcher**
- URL: https://graph.facebook.com/{UID}
- API chính thức của Facebook (có giới hạn)
- Trả về thông tin cơ bản nếu profile public

**🔗 AnalyzeID**
- URL: https://analyzeid.com/
- Phân tích chi tiết Facebook profile
- Hiển thị thông tin metadata

**🔗 Facebook Recover Lookup**
- URL: https://www.facebook.com/login/identify
- Kiểm tra email/phone có liên kết với Facebook
- Phương pháp: Nhập email/phone vào form recovery

#### B. Phương Pháp Thủ Công

**Trích xuất UID từ URL:**
```
# Các dạng URL chứa UID:
https://www.facebook.com/profile.php?id=100012345678901
https://www.facebook.com/100012345678901
https://m.facebook.com/profile.php?id=100012345678901

# Trong source code:
"entity_id":"100012345678901"
"profile_id":"100012345678901"
"fbid":"100012345678901"
```

**Kiểm tra Profile Existence:**
```bash
curl -I "https://www.facebook.com/100012345678901"
# Status 200: Profile tồn tại
# Status 404: Profile không tồn tại hoặc bị ẩn
```

### 2. TikTok Username Investigation

#### A. Công Cụ Chuyên Dụng

**🔗 TikTok Profile Checker**
```python
# Sử dụng script có sẵn
from social_media_osint_tool import TikTokOSINT

tiktok = TikTokOSINT()
result = tiktok.get_user_info("username")
print(result)
```

**🔗 Sherlock (Multi-platform)**
```bash
# Cài đặt Sherlock
git clone https://github.com/sherlock-project/sherlock.git
cd sherlock
pip install -r requirements.txt

# Tìm username trên nhiều platform
python sherlock username123
```

**🔗 Social Analyzer**
```bash
# Cài đặt
git clone https://github.com/qeeqbox/social-analyzer.git
cd social-analyzer
pip install -r requirements.txt

# Chạy
python social-analyzer.py --username username123 --websites tiktok
```

#### B. API Methods

**TikTok Web Scraping:**
```python
import requests
import re

def check_tiktok_user(username):
    url = f"https://www.tiktok.com/@{username}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    response = requests.get(url, headers=headers)
    
    if "Couldn't find this account" in response.text:
        return {"exists": False}
    else:
        # Extract info from HTML
        name_match = re.search(r'<title>([^|]+)', response.text)
        return {
            "exists": True,
            "name": name_match.group(1) if name_match else "N/A",
            "url": url
        }
```

### 3. Cross-Platform Investigation

#### A. Username Enumeration

**Các Platform Phổ Biến:**
```python
platforms = {
    'facebook': 'https://facebook.com/{}',
    'instagram': 'https://instagram.com/{}',
    'twitter': 'https://twitter.com/{}',
    'tiktok': 'https://tiktok.com/@{}',
    'youtube': 'https://youtube.com/c/{}',
    'linkedin': 'https://linkedin.com/in/{}',
    'github': 'https://github.com/{}',
    'reddit': 'https://reddit.com/user/{}'
}
```

**Batch Checking Script:**
```python
def check_username_across_platforms(username):
    results = {}
    
    for platform, url_template in platforms.items():
        url = url_template.format(username)
        try:
            response = requests.head(url, timeout=5)
            results[platform] = {
                'exists': response.status_code == 200,
                'url': url,
                'status_code': response.status_code
            }
        except:
            results[platform] = {'exists': False, 'error': True}
    
    return results
```

## 🛠️ Công Cụ OSINT Nâng Cao

### 1. Maltego
- **Mô tả**: Nền tảng tình báo trực quan mạnh mẽ
- **Tính năng**: Link analysis, data mining, forensics
- **Cài đặt**: https://www.maltego.com/
- **Sử dụng**: Import entities, run transforms, visualize connections

### 2. TheHarvester
```bash
# Cài đặt
git clone https://github.com/laramies/theHarvester.git
cd theHarvester
pip install -r requirements.txt

# Thu thập thông tin
python theHarvester.py -d facebook.com -l 500 -b google
python theHarvester.py -d tiktok.com -l 500 -b bing
```

### 3. Seekr (OSINT Framework)
```bash
# Cài đặt
git clone https://github.com/seekr-osint/seekr.git
cd seekr
pip install -r requirements.txt

# Chạy web interface
python app.py
# Truy cập: http://localhost:5000
```

### 4. Social Mapper
```bash
# Cài đặt
git clone https://github.com/Greenwolf/social_mapper.git
cd social_mapper
pip install -r requirements.txt

# Tìm kiếm bằng ảnh
python social_mapper.py -f face -i ./images/target.jpg -m fast
```

## 📊 Phân Tích Dữ Liệu

### 1. Correlation Analysis
```python
def analyze_social_footprint(facebook_data, tiktok_data):
    correlations = []
    
    # So sánh tên
    if facebook_data.get('name') and tiktok_data.get('display_name'):
        name_similarity = calculate_similarity(
            facebook_data['name'], 
            tiktok_data['display_name']
        )
        correlations.append(('name_similarity', name_similarity))
    
    # So sánh thời gian hoạt động
    # So sánh followers/friends count
    # So sánh bio/description
    
    return correlations
```

### 2. Timeline Construction
```python
def build_activity_timeline(social_data):
    timeline = []
    
    for platform, data in social_data.items():
        if data.get('creation_date'):
            timeline.append({
                'platform': platform,
                'event': 'account_created',
                'date': data['creation_date']
            })
    
    return sorted(timeline, key=lambda x: x['date'])
```

## 🔒 Bảo Mật & Đạo Đức

### ⚠️ Lưu Ý Quan Trọng

1. **Tuân thủ pháp luật**: Chỉ sử dụng cho mục đích hợp pháp
2. **Tôn trọng quyền riêng tư**: Không xâm phạm thông tin cá nhân
3. **Rate limiting**: Tránh spam requests
4. **Terms of Service**: Tuân thủ ToS của các platform

### 🛡️ Best Practices

```python
# Sử dụng delays giữa requests
import time
time.sleep(1)  # 1 giây delay

# Rotate User-Agent
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
]

# Sử dụng proxy nếu cần
proxies = {
    'http': 'http://proxy:port',
    'https': 'https://proxy:port'
}
```

## 📈 Tối Ưu Hóa & Mở Rộng

### 1. Caching Results
```python
import json
import os
from datetime import datetime, timedelta

class OSINTCache:
    def __init__(self, cache_dir='./cache'):
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)
    
    def get(self, key, max_age_hours=24):
        cache_file = os.path.join(self.cache_dir, f"{key}.json")
        
        if os.path.exists(cache_file):
            with open(cache_file, 'r') as f:
                data = json.load(f)
            
            cached_time = datetime.fromisoformat(data['timestamp'])
            if datetime.now() - cached_time < timedelta(hours=max_age_hours):
                return data['result']
        
        return None
    
    def set(self, key, result):
        cache_file = os.path.join(self.cache_dir, f"{key}.json")
        
        data = {
            'timestamp': datetime.now().isoformat(),
            'result': result
        }
        
        with open(cache_file, 'w') as f:
            json.dump(data, f)
```

### 2. Async Processing
```python
import asyncio
import aiohttp

async def async_check_username(session, platform, username):
    url = platforms[platform].format(username)
    
    try:
        async with session.head(url) as response:
            return {
                'platform': platform,
                'exists': response.status == 200,
                'url': url
            }
    except:
        return {'platform': platform, 'exists': False, 'error': True}

async def batch_username_check(username):
    async with aiohttp.ClientSession() as session:
        tasks = [
            async_check_username(session, platform, username)
            for platform in platforms.keys()
        ]
        
        results = await asyncio.gather(*tasks)
        return {r['platform']: r for r in results}
```

## 📚 Tài Nguyên Bổ Sung

### 🔗 Links Hữu Ích

- **OSINT Framework**: https://osintframework.com/
- **Bellingcat Toolkit**: https://github.com/bellingcat/toolkit
- **OSINT Curious**: https://osintcurio.us/
- **Social Media OSINT Tools**: https://github.com/osintambition/Social-Media-OSINT-Tools-Collection

### 📖 Documentation

- **Facebook Graph API**: https://developers.facebook.com/docs/graph-api/
- **TikTok Developer**: https://developers.tiktok.com/
- **OSINT Techniques**: https://www.osinttechniques.com/

### 🎓 Learning Resources

- **SANS SEC487**: Open Source Intelligence (OSINT) Gathering and Analysis
- **Udemy OSINT Courses**: Various OSINT training courses
- **YouTube Channels**: 
  - The Cyber Mentor
  - John Hammond
  - OSINT Curious

## 🤝 Đóng Góp

Nếu bạn muốn đóng góp vào dự án:

1. Fork repository
2. Tạo feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## 📄 License

Dự án này được phát hành dưới MIT License. Xem file LICENSE để biết thêm chi tiết.

## ⚖️ Disclaimer

Công cụ này chỉ dành cho mục đích giáo dục và nghiên cứu. Người dùng có trách nhiệm tuân thủ pháp luật địa phương và quốc tế khi sử dụng. Tác giả không chịu trách nhiệm về việc sử dụng sai mục đích.

---

**🎯 Happy OSINT Hunting! 🕵️‍♂️**
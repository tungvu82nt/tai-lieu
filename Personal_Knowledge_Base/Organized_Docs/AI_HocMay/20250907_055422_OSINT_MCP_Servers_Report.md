# BÁO CÁO TỔNG HỢP: CÁC MCP SERVER OSINT CHO THU THẬP THÔNG TIN CÁ NHÂN

## TÓM TẮT ĐIỀU TRA

Qua quá trình crawl và phân tích trang web cursor.directory/mcp, tôi đã xác định được một số MCP server quan trọng có khả năng thu thập thông tin cá nhân như email, số điện thoại và tài khoản mạng xã hội. Các công cụ này được thiết kế cho mục đích OSINT (Open-Source Intelligence) hợp pháp.

## CÁC MCP SERVER OSINT CHÍNH

### 1. MCP-MAIGRET
**Nguồn:** https://github.com/BurtTheCoder/mcp-maigret
**Mô tả:** MCP server cho Maigret - công cụ OSINT mạnh mẽ thu thập thông tin tài khoản người dùng từ các nguồn công khai

**Tính năng chính:**
- **Tìm kiếm Username:** Tìm kiếm username trên hàng trăm mạng xã hội và website
- **Phân tích URL:** Phân tích URL để trích xuất thông tin và tìm kiếm username liên quan
- **Đa định dạng:** Hỗ trợ xuất kết quả dạng txt, html, pdf, json, csv, xmind
- **Lọc theo site:** Lọc tìm kiếm theo tags (ví dụ: photo, dating, us)
- **Docker-based:** Thực thi đáng tin cậy và nhất quán

**Công cụ có sẵn:**
1. **search_username:** Tìm kiếm username trên các mạng xã hội
2. **parse_url:** Phân tích URL để trích xuất thông tin

**Cài đặt:**
```bash
npm install -g mcp-maigret
```

**Cấu hình Claude Desktop:**
```json
{
  "mcpServers": {
    "maigret": {
      "command": "mcp-maigret",
      "env": {
        "MAIGRET_REPORTS_DIR": "/path/to/reports/directory"
      }
    }
  }
}
```

### 2. SOCIAL MEDIA LEADS ANALYZER (APIFY)
**Nguồn:** https://apify.com/apify/social-media-leads-analyzer
**Mô tả:** Công cụ trích xuất email, số điện thoại và thông tin mạng xã hội từ website

**Tính năng:**
- Trích xuất dữ liệu từ 8 nền tảng mạng xã hội
- Thu thập email và số điện thoại
- Xuất kết quả JSON, CSV, HTML
- API tích hợp
- Lập lịch chạy tự động

**Giá:** $20.00 / 1,000 kết quả

**Cấu hình MCP:**
```json
{
    "mcpServers": {
        "apify": {
            "command": "npx",
            "args": [
                "mcp-remote",
                "https://mcp.apify.com/sse?actors=apify/social-media-leads-analyzer",
                "--header",
                "Authorization: Bearer <YOUR_API_TOKEN>"
            ]
        }
    }
}
```

### 3. CÁC CÔNG CỤ APIFY KHÁC

#### Social Media Finder
- **Tác giả:** tri_angle/social-media-finder
- **Chức năng:** Tìm kiếm profile mạng xã hội theo tên hoặc nickname
- **Nền tảng:** 13 nền tảng phổ biến (TikTok, Twitch, LinkedIn, Medium...)

#### Contact Detail Scraper
- **Tác giả:** pintostudio/contact-detail-scraper
- **Chức năng:** Trích xuất email, số điện thoại, profile mạng xã hội từ website
- **Xuất:** Excel, CSV, JSON, HTML, XML

#### Deep Email, Phone, & Social Media Scraper
- **Tác giả:** peterasorensen/snacci
- **Chức năng:** Trích xuất thông tin liên lạc từ website với khả năng điều hướng thông minh
- **Đặc điểm:** Ưu tiên các trang có khả năng chứa thông tin liên lạc

#### All Social Media Phone Number Scraper
- **Tác giả:** scraper-mind/all-social-media-phone-number-scraper
- **Chức năng:** Thu thập số điện thoại từ Instagram, Facebook, Twitter và nhiều nền tảng khác
- **Đặc điểm:** Giá rẻ nhất, nhanh chóng và chính xác

## CÁC MCP SERVER HỖ TRỢ KHÁC

### BrowserTools MCP
- **Chức năng:** Phân tích logs và tương tác với browser để debug nhanh
- **Ứng dụng:** Hỗ trợ điều tra web-based

### Puppeteer MCP
- **Chức năng:** Tự động hóa browser, chụp screenshot, thực thi JavaScript
- **Ứng dụng:** Thu thập dữ liệu từ các trang web động

### Firecrawl MCP
- **Chức năng:** Chuyển đổi toàn bộ website thành dữ liệu sẵn sàng cho LLM
- **Ứng dụng:** Crawl và phân tích nội dung website

### Fetch MCP
- **Chức năng:** Thu thập và chuyển đổi nội dung web, HTML sang markdown
- **Ứng dụng:** Xử lý nội dung web cho phân tích

## HƯỚNG DẪN SỬ DỤNG AN TOÀN

### ⚠️ CẢNH BÁO QUAN TRỌNG

**Các công cụ này được thiết kế cho mục đích nghiên cứu OSINT hợp pháp. Vui lòng:**

- Chỉ tìm kiếm thông tin có sẵn công khai
- Tôn trọng luật bảo vệ quyền riêng tư và dữ liệu
- Tuân thủ điều khoản dịch vụ của các nền tảng
- Sử dụng có trách nhiệm và đạo đức
- Lưu ý một số trang có thể giới hạn hoặc chặn tìm kiếm tự động

### YÊU CẦU HỆ THỐNG

- Node.js (v18 trở lên)
- Docker
- macOS, Linux, hoặc Windows với Docker Desktop
- Quyền ghi vào thư mục reports

## KẾT LUẬN

Các MCP server OSINT này cung cấp khả năng mạnh mẽ để thu thập thông tin cá nhân từ các nguồn công khai. **MCP-Maigret** nổi bật như công cụ toàn diện nhất với khả năng tìm kiếm trên hàng trăm nền tảng, trong khi các công cụ Apify cung cấp các giải pháp chuyên biệt cho từng nhu cầu cụ thể.

**Lưu ý:** Tất cả các công cụ này phải được sử dụng tuân thủ pháp luật và đạo đức nghề nghiệp trong lĩnh vực OSINT.

---

**Ngày tạo báo cáo:** $(Get-Date -Format "dd/MM/yyyy HH:mm:ss")
**Nguồn dữ liệu:** cursor.directory/mcp, GitHub, Apify Store
**Phương pháp:** Web crawling và phân tích thông tin công khai
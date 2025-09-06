#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script để sắp xếp lại kho tài liệu cá nhân
Loại bỏ file trùng lặp và tổ chức theo cấu trúc thống nhất
"""

import os
import shutil
import hashlib
import json
from pathlib import Path
from datetime import datetime

class FileOrganizer:
    def __init__(self, base_path):
        self.base_path = Path(base_path)
        self.duplicates = {}
        self.file_hashes = {}
        self.stats = {
            'moved': 0,
            'duplicates': 0,
            'errors': 0,
            'processed': 0
        }

    def calculate_file_hash(self, file_path):
        """Tính hash MD5 của file để phát hiện trùng lặp"""
        try:
            with open(file_path, 'rb') as f:
                return hashlib.md5(f.read()).hexdigest()
        except Exception as e:
            print(f"Lỗi khi tính hash {file_path}: {e}")
            return None

    def find_duplicates(self):
        """Tìm các file trùng lặp trong toàn bộ workspace"""
        print("🔍 Đang tìm file trùng lặp...")

        # Duyệt qua tất cả file
        for root, dirs, files in os.walk(self.base_path):
            # Bỏ qua thư mục .git và các thư mục không cần thiết
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__', 'node_modules']]

            for file in files:
                if file.endswith('.md'):
                    file_path = Path(root) / file
                    file_hash = self.calculate_file_hash(file_path)

                    if file_hash:
                        if file_hash in self.file_hashes:
                            # File trùng lặp
                            if file_hash not in self.duplicates:
                                self.duplicates[file_hash] = [self.file_hashes[file_hash]]
                            self.duplicates[file_hash].append(file_path)
                        else:
                            self.file_hashes[file_hash] = file_path

        print(f"📊 Tìm thấy {len(self.duplicates)} nhóm file trùng lặp")

    def move_to_organized_structure(self):
        """Di chuyển file vào cấu trúc Organized_Docs"""
        organized_path = self.base_path / "Organized_Docs"

        # Đảm bảo thư mục đích tồn tại
        organized_path.mkdir(exist_ok=True)

        print("📁 Đang sắp xếp file...")

        # Di chuyển file từ các thư mục số thứ tự
        source_dirs = ['01_AI_Tools', '02_OSINT_Tools', '03_Security_Hacking_Tools', '04_Documentation', 'AI_Tools', 'Security_Tools']

        for source_dir in source_dirs:
            source_path = self.base_path / source_dir
            if source_path.exists():
                print(f"  ↳ Đang xử lý {source_dir}...")

                for file_path in source_path.rglob('*.md'):
                    if file_path.is_file():
                        self.move_file_to_category(file_path, organized_path)
                        self.stats['processed'] += 1

        # Xử lý các thư mục khác
        other_dirs = ['Other', 'Technology', 'Tutorials']
        for other_dir in other_dirs:
            other_path = self.base_path / other_dir
            if other_path.exists():
                print(f"  ↳ Đang xử lý {other_dir}...")

                for file_path in other_path.rglob('*.md'):
                    if file_path.is_file():
                        self.move_file_to_category(file_path, organized_path)
                        self.stats['processed'] += 1

    def move_file_to_category(self, file_path, organized_path):
        """Di chuyển file vào thư mục phù hợp"""
        try:
            # Đọc nội dung file để xác định chủ đề
            content = ""
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read(1000)  # Đọc 1000 ký tự đầu
            except:
                try:
                    with open(file_path, 'r', encoding='gbk') as f:
                        content = f.read(1000)
                except:
                    content = file_path.name

            # Xác định thư mục đích dựa trên nội dung
            target_dir = self.categorize_file(content, file_path.name)

            # Tạo thư mục đích
            target_path = organized_path / target_dir
            target_path.mkdir(exist_ok=True)

            # Tạo tên file mới (thêm timestamp để tránh trùng lặp)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            new_filename = f"{timestamp}_{file_path.name}"
            new_path = target_path / new_filename

            # Di chuyển file
            shutil.move(str(file_path), str(new_path))
            self.stats['moved'] += 1

            print(f"    ✓ {file_path.name} → {target_dir}/{new_filename}")

        except Exception as e:
            print(f"    ✗ Lỗi khi di chuyển {file_path}: {e}")
            self.stats['errors'] += 1

    def categorize_file(self, content, filename):
        """Phân loại file dựa trên nội dung và tên file"""
        content_lower = content.lower()
        filename_lower = filename.lower()

        # AI & Machine Learning
        ai_keywords = ['ai', 'artificial intelligence', 'machine learning', 'deep learning', 'chatgpt', 'claude', 'gemini', 'gpt', 'llm', 'chatbot']
        if any(keyword in content_lower or keyword in filename_lower for keyword in ai_keywords):
            return "AI_HocMay"

        # Network Security
        security_keywords = ['security', 'hacking', 'penetration', 'vulnerability', 'exploit', 'malware', 'virus', 'trojan', 'phishing', 'hacker', 'pentest']
        if any(keyword in content_lower or keyword in filename_lower for keyword in security_keywords):
            return "BaoMatMang"

        # OSINT
        osint_keywords = ['osint', 'intelligence', 'reconnaissance', 'facebook', 'tiktok', 'social media', 'username', 'email', 'phone']
        if any(keyword in content_lower or keyword in filename_lower for keyword in osint_keywords):
            return "PhatTrien"  # OSINT tools sẽ vào PhatTrien

        # Development
        dev_keywords = ['programming', 'development', 'web', 'app', 'software', 'code', 'javascript', 'python', 'java', 'github']
        if any(keyword in content_lower or keyword in filename_lower for keyword in dev_keywords):
            return "PhatTrien"

        # Cloud & Infrastructure
        cloud_keywords = ['cloud', 'aws', 'azure', 'google cloud', 'docker', 'kubernetes', 'serverless', 'infrastructure']
        if any(keyword in content_lower or keyword in filename_lower for keyword in cloud_keywords):
            return "DamMay_HaTang"

        # Data Science
        data_keywords = ['data science', 'dataset', 'machine learning', 'statistics', 'python', 'pandas', 'numpy', 'matplotlib']
        if any(keyword in content_lower or keyword in filename_lower for keyword in data_keywords):
            return "KhoaHocDuLieu"

        # Default category
        return "HuongDan_TongHop"

    def remove_duplicate_files(self):
        """Xóa các file trùng lặp, giữ lại file trong Organized_Docs"""
        print("🗑️ Đang xóa file trùng lặp...")

        organized_path = self.base_path / "Organized_Docs"

        for hash_value, file_paths in self.duplicates.items():
            # Giữ lại file trong Organized_Docs, xóa các file khác
            organized_files = [p for p in file_paths if str(organized_path) in str(p)]
            other_files = [p for p in file_paths if str(organized_path) not in str(p)]

            if organized_files:
                # Có file trong Organized_Docs, xóa các file khác
                for file_path in other_files:
                    try:
                        if file_path.exists():
                            os.remove(file_path)
                            self.stats['duplicates'] += 1
                            print(f"    🗑️ Đã xóa file trùng lặp: {file_path}")
                    except Exception as e:
                        print(f"    ✗ Lỗi khi xóa {file_path}: {e}")
            else:
                # Không có file trong Organized_Docs, giữ lại file đầu tiên
                for file_path in file_paths[1:]:
                    try:
                        if file_path.exists():
                            os.remove(file_path)
                            self.stats['duplicates'] += 1
                            print(f"    🗑️ Đã xóa file trùng lặp: {file_path}")
                    except Exception as e:
                        print(f"    ✗ Lỗi khi xóa {file_path}: {e}")

    def clean_empty_directories(self):
        """Xóa các thư mục trống"""
        print("🧹 Đang dọn dẹp thư mục trống...")

        for root, dirs, files in os.walk(self.base_path, topdown=False):
            for dir_name in dirs:
                dir_path = Path(root) / dir_name
                try:
                    if not any(dir_path.rglob('*')):
                        dir_path.rmdir()
                        print(f"    🗑️ Đã xóa thư mục trống: {dir_path}")
                except:
                    pass

    def generate_readme(self):
        """Tạo README.md mới cho từng thư mục"""
        organized_path = self.base_path / "Organized_Docs"

        categories = {
            "AI_HocMay": {
                "title": "🤖 AI & Học Máy",
                "description": "Các tài liệu về trí tuệ nhân tạo và học máy",
                "topics": ["ChatGPT", "Claude", "Gemini", "AI Tools", "Machine Learning"]
            },
            "BaoMatMang": {
                "title": "🛡️ Bảo Mật Mạng",
                "description": "Các tài liệu về bảo mật và an ninh mạng",
                "topics": ["Penetration Testing", "Vulnerability", "Malware", "Network Security"]
            },
            "PhatTrien": {
                "title": "💻 Phát Triển Phần Mềm",
                "description": "Các tài liệu về phát triển phần mềm",
                "topics": ["Web Development", "OSINT Tools", "GitHub Projects", "Programming"]
            },
            "DamMay_HaTang": {
                "title": "☁️ Đám Mây & Hạ Tầng",
                "description": "Các tài liệu về đám mây và hạ tầng",
                "topics": ["AWS", "Google Cloud", "Docker", "Kubernetes"]
            },
            "KhoaHocDuLieu": {
                "title": "📊 Khoa Học Dữ Liệu",
                "description": "Các tài liệu về khoa học dữ liệu",
                "topics": ["Python", "Datasets", "Machine Learning", "Statistics"]
            },
            "HuongDan_TongHop": {
                "title": "📚 Hướng Dẫn Tổng Hợp",
                "description": "Các hướng dẫn và tài liệu tổng hợp",
                "topics": ["Tutorials", "Guides", "Documentation"]
            }
        }

        # Tạo README cho từng thư mục
        for category, info in categories.items():
            category_path = organized_path / category
            if category_path.exists():
                readme_path = category_path / "README.md"

                # Đếm số file
                md_files = list(category_path.glob("*.md"))
                file_count = len([f for f in md_files if f.name != "README.md"])

                # Tạo nội dung README
                readme_content = f"""# {info['title']}

{info['description']}

## 📊 Thông Tin
- **Số lượng file**: {file_count} files
- **Cập nhật**: {datetime.now().strftime('%d/%m/%Y')}

## 📋 Chủ Đề Chính
"""

                for topic in info['topics']:
                    readme_content += f"- {topic}\n"

                readme_content += "\n## 📁 Danh Sách Files\n\n"

                # Liệt kê các file
                for md_file in sorted(md_files):
                    if md_file.name != "README.md":
                        readme_content += f"- [{md_file.name}]({md_file.name})\n"

                readme_content += "\n---\n*Tự động tạo bởi File Organizer*"

                # Ghi file
                with open(readme_path, 'w', encoding='utf-8') as f:
                    f.write(readme_content)

                print(f"    ✓ Đã tạo README cho {category}")

        # Tạo README tổng thể
        total_files = sum(len(list((organized_path / cat).glob("*.md"))) for cat in categories.keys() if (organized_path / cat).exists())

        main_readme = f"""# 📁 Kho Tài Liệu Cá Nhân - Đã Sắp Xếp

Chào mừng bạn đến với kho tài liệu cá nhân đã được sắp xếp theo chủ đề!

## 📂 Cấu Trúc Thư Mục

"""

        for category, info in categories.items():
            category_path = organized_path / category
            if category_path.exists():
                file_count = len([f for f in category_path.glob("*.md") if f.name != "README.md"])
                main_readme += f"### {info['title']} ({file_count} files)\n"
                main_readme += f"{info['description']}\n\n"
                main_readme += f"**Chủ đề:** {', '.join(info['topics'])}\n\n"

        main_readme += f"""## 📊 Thống Kê
- **Tổng số file**: {total_files} files
- **Số thư mục**: {len(categories)} categories
- **Đã sắp xếp**: ✅ Hoàn thành
- **Cập nhật gần nhất**: {datetime.now().strftime('%d/%m/%Y')}

## 🔍 Cách Sử Dung
1. Chọn thư mục theo chủ đề bạn quan tâm
2. Đọc README.md trong từng thư mục để biết thêm chi tiết
3. Duyệt qua các file markdown
4. Sử dụng tìm kiếm để tìm nội dung cụ thể

---
*Tự động sắp xếp bởi File Organizer vào {datetime.now().strftime('%d/%m/%Y %H:%M')}*
"""

        with open(organized_path / "README.md", 'w', encoding='utf-8') as f:
            f.write(main_readme)

        print("    ✓ Đã tạo README tổng thể")

    def run(self):
        """Chạy toàn bộ quá trình sắp xếp"""
        print("🚀 Bắt đầu sắp xếp kho tài liệu...")
        print("=" * 50)

        # Bước 1: Tìm file trùng lặp
        self.find_duplicates()

        # Bước 2: Di chuyển file vào cấu trúc mới
        self.move_to_organized_structure()

        # Bước 3: Xóa file trùng lặp
        self.remove_duplicate_files()

        # Bước 4: Dọn dẹp thư mục trống
        self.clean_empty_directories()

        # Bước 5: Tạo README
        self.generate_readme()

        # In thống kê
        print("=" * 50)
        print("📊 THỐNG KÊ HOÀN THÀNH:")
        print(f"  • Đã xử lý: {self.stats['processed']} files")
        print(f"  • Đã di chuyển: {self.stats['moved']} files")
        print(f"  • Đã xóa trùng lặp: {self.stats['duplicates']} files")
        print(f"  • Lỗi: {self.stats['errors']} files")
        print("=" * 50)
        print("✅ Hoàn thành sắp xếp kho tài liệu!")

if __name__ == "__main__":
    organizer = FileOrganizer("D:/TÀI LIÊU/Personal_Knowledge_Base")
    organizer.run()

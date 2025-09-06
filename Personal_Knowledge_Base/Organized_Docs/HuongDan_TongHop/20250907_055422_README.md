# 🔐 Password Attacks - Tấn công Mật khẩu

> Các công cụ để crack, brute force và phân tích mật khẩu

---

## 💧 [Hydra](https://www.kali.org/tools/hydra/)
**Chức năng:** Brute force login đa giao thức  
**Mô tả:** Công cụ brute force mạnh nhất hỗ trợ 50+ giao thức  
**Lệnh chính:** `hydra`, `hydra-wizard`, `pw-inspector`  
**Ví dụ:** `hydra -l admin -P passwords.txt ssh://192.168.1.1` (SSH brute force)

---

## 👑 [John the Ripper](https://www.kali.org/tools/john/)
**Chức năng:** Crack mật khẩu đa định dạng  
**Mô tả:** Công cụ crack mật khẩu linh hoạt với nhiều mode  
**Lệnh chính:** `john`, `unshadow`, `zip2john`, `rar2john`  
**Ví dụ:** `john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt`

---

## ⚡ [Hashcat](https://www.kali.org/tools/hashcat/)
**Chức năng:** Crack mật khẩu GPU-accelerated  
**Mô tả:** Công cụ crack mật khẩu nhanh nhất sử dụng GPU  
**Lệnh chính:** `hashcat`  
**Ví dụ:** `hashcat -m 0 -a 0 hashes.txt rockyou.txt` (MD5 dictionary attack)

---

## 🐄 [Cowpatty](https://www.kali.org/tools/cowpatty/)
**Chức năng:** WPA-PSK dictionary attack  
**Mô tả:** Chuyên crack mật khẩu WiFi WPA/WPA2  
**Lệnh chính:** `cowpatty`, `genpmk`  
**Ví dụ:** `cowpatty -r capture.cap -f wordlist.txt -s ESSID`

---

## 🔓 [Crack](https://www.kali.org/tools/crack/)
**Chức năng:** Phát hiện mật khẩu yếu  
**Mô tả:** Công cụ cổ điển để tìm mật khẩu dễ đoán  
**Lệnh chính:** `crack`  
**Ví dụ:** `crack /etc/passwd` (crack system passwords)

---

## 🔄 **Các công cụ chuyển đổi định dạng:**

### 📦 [zip2john](https://www.kali.org/tools/john/#zip2john)
**Chức năng:** Chuyển ZIP thành format John  
**Ví dụ:** `zip2john file.zip > hash.txt`

### 📄 [rar2john](https://www.kali.org/tools/john/#rar2john)
**Chức năng:** Chuyển RAR thành format John  
**Ví dụ:** `rar2john file.rar > hash.txt`

### 🔑 [keepass2john](https://www.kali.org/tools/john/#keepass2john)
**Chức năng:** Chuyển KeePass thành format John  
**Ví dụ:** `keepass2john database.kdbx > hash.txt`

### 🌐 [wpapcap2john](https://www.kali.org/tools/john/#wpapcap2john)
**Chức năng:** Chuyển WPA capture thành format John  
**Ví dụ:** `wpapcap2john capture.cap > hash.txt`

---

## 📊 **Hash Types phổ biến:**

| Hash Type | Hashcat Mode | John Format | Ví dụ |
|-----------|--------------|-------------|-------|
| MD5 | 0 | Raw-MD5 | `5d41402abc4b2a76b9719d911017c592` |
| SHA1 | 100 | Raw-SHA1 | `aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d` |
| NTLM | 1000 | NT | `b4b9b02e6f09a9bd760f388b67351e2b` |
| WPA/WPA2 | 2500 | WPAPSK | Từ .cap file |
| bcrypt | 3200 | bcrypt | `$2a$10$...` |

---

## 🎯 **Attack Modes:**

### 📖 **Dictionary Attack**
```bash
# John
john --wordlist=rockyou.txt hashes.txt

# Hashcat
hashcat -m 0 -a 0 hashes.txt rockyou.txt

# Hydra
hydra -l admin -P passwords.txt ssh://target
```

### 🎭 **Mask Attack**
```bash
# Hashcat - 8 ký tự: 4 chữ + 4 số
hashcat -m 0 -a 3 hashes.txt ?l?l?l?l?d?d?d?d

# John với mask
john --mask=?l?l?l?l?d?d?d?d hashes.txt
```

### 🔄 **Combination Attack**
```bash
# Hashcat - kết hợp 2 wordlist
hashcat -m 0 -a 1 hashes.txt wordlist1.txt wordlist2.txt
```

---

## 💡 **Tips & Best Practices:**

### 🚀 **Tối ưu hiệu suất:**
- 🎮 Sử dụng GPU cho Hashcat (nhanh hơn 100x)
- 💾 Sử dụng SSD cho wordlist lớn
- 🔧 Điều chỉnh workload tuning
- 📊 Monitor nhiệt độ GPU

### 📚 **Wordlist recommendations:**
- `rockyou.txt` - Phổ biến nhất
- `SecLists` - Tổng hợp wordlist chuyên nghiệp
- `CrackStation` - Wordlist lớn
- Custom wordlist từ target reconnaissance

### ⚡ **Rule-based attacks:**
```bash
# John với rules
john --wordlist=passwords.txt --rules hashes.txt

# Hashcat với rules
hashcat -m 0 -a 0 hashes.txt passwords.txt -r best64.rule
```

---

## ⚠️ **Lưu ý quan trọng:**
- 🎯 Chỉ test trên hệ thống được phép
- ⏱️ Password cracking có thể mất nhiều thời gian
- 🔥 Monitor nhiệt độ hardware khi chạy lâu
- 💾 Backup kết quả thường xuyên
- 📝 Document methodology và kết quả

## 🔗 **Tài liệu tham khảo:**
- [Hashcat Wiki](https://hashcat.net/wiki/)
- [John the Ripper Documentation](https://www.openwall.com/john/doc/)
- [Password Cracking Rules](https://github.com/NotSoSecure/password_cracking_rules)
- [SecLists Wordlists](https://github.com/danielmiessler/SecLists)
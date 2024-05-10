# 以网页链接版访问
# 连接邮件服务器
# 每个服务商的邮件服务器端口号是不一样的，需要根据自己使用的服务器而更改
try:
    server = imaplib.IMAP4_SSL(smtp_server,port=port)
    print("连接邮箱服务器")
    server.starttls() # 启用安全传输模式（如果已启用）
    server.login(username, password) # 使用您的授权码或密码登录邮箱
    print('login successfully!')
except Exception as e:
    print('Failed to login:', e)
finally:
    server.quit() # 断开与邮件服务器的连接

# 设置邮件信息
to_addr =  '' # 收件人邮箱地址
subject = 'Test Email' # 邮件主题
content = 'This is the body of the email.' # 邮件正文

# 创建邮件对象
msg = MIMEMultipart()
msg['From'] = username  #发件人
msg['To'] = to_addr     #收件人
msg['Subject'] = subject #邮件主题

# 添加邮件正文
msg.attach(MIMEText(content, 'html'))

# 连接到SMTP服务器并发送邮件
try:
    server = smtplib.SMTP(smtp_server,port)
    print("连接邮箱服务器")
    server.starttls() # 启用安全传输模式（如果已启用）
    server.login(username, password) # 使用您的授权码或密码登录邮箱
    server.sendmail(username, to_addr, msg.as_string())
    print('Email sent successfully!')
except Exception as e:
    print('Failed to send email:', e)
finally:
    server.quit() # 断开与SMTP服务器的连接

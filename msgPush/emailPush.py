
def send_email_notification(message_content ,receiver_email = 1 ):
    """
    发送电子邮件通知
    :param receiver_email: 接收者邮箱
    :param message_content: 要发送的消息内容
    """
    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header

    # 设置邮件服务器、端口、发件人和密码（建议使用应用专用密码）
    smtp_server = 'smtp.sina.com'
    smtp_port = 465
    sender_email = input('请输入发件人邮箱前缀：')+'@sina.com'
    print(sender_email)
    sender_password = input('请输入发件人密码：')
    print(sender_password)
    if receiver_email == 1:
        receiver_email = input('请输入收件人邮箱前缀：')+'@gmail.com'
        print(receiver_email)
    try:
        # 创建 MIME 文本对象
        msg = MIMEText(message_content, 'plain', 'utf-8')
        msg['From'] = Header(sender_email)
        msg['To'] = Header(receiver_email)
        msg['Subject'] = Header('系统通知')

        # 连接 SMTP 服务器并发送邮件
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        # server.starttls()  # 启用 TLS 加密
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, [receiver_email], msg.as_string())
        server.quit()

        print(f'邮件已成功发送至 {receiver_email}')
        return True

    except Exception as e:
        print(f'邮件发送失败: {e}')

if __name__ == '__main__':
    # 调用函数,第一个参数留空

    send_email_notification('abc')
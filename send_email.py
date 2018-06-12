# - * - coding: utf - 8 -*-
import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
msgFrom = 'jhh130910@163.com' #从该邮箱发送

#msgTo = 'jinhh@cloudhealth99.com' #发送到该邮箱
smtpSever='smtp.163.com' # 163邮箱的smtp Sever地址
smtpPort = '25' #开放的端口
sqm='dropbox****'  # 在登录smtp时需要login中的密码应当使用授权码而非账户密码

msgTo2 = '1045969014@qq.com'
msg['from'] = msgFrom
#msg['to'] = msgTo
msg['to'] = msgTo2
msg['subject'] = '集群资源拷贝申请' 
people1 = 'Axx'
people2 = 'Bxx'
content = '''

你好 people1 :
    这是一封Py3.x发送的邮件,please help do ...

    thanks very much !
'''
txt = email.mime.text.MIMEText(content)
msg.attach(txt)
smtp = smtplib
smtp = smtplib.SMTP()
'''
smtplib的connect（连接到邮件服务器）、login（登陆验证）、sendmail（发送邮件）
'''
smtp.connect(smtpSever, smtpPort)
smtp.login(msgFrom, sqm)
#smtp.sendmail(msgFrom, msgTo, str(msg))
smtp.sendmail(msgFrom, msgTo2, str(msg))
smtp.quit()

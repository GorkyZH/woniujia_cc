#coding=utf-8
import smtplib
from email.mime.text import MIMEText
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
"""
统计并发送邮件报告工具类
"""
class SendEmail:
    global send_user
    global email_host
    global password
    email_host = "smtp.163.com"
    send_user = "gorky1112@163.com"
    password = "gorky@1112"

    def send_email(self, user_list, sub, content):
        user = "Gorky"+"<"+send_user+">"
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user, password)
        server.sendmail(user, user_list, message.as_string())
        server.close()

    def send_main(self, pass_list, fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num+fail_num

        pass_percent = "%.2f%%" %(pass_num/count_num*100)
        fail_percent = "%.2f%%" %(fail_num/count_num*100)

        user_list = ['1018063128@qq.com']
        sub = "接口自动化测试邮件"
        content = "总共运行接口%s个,通过个数：%s个，失败个数：%s个，通过率：%s，失败率：%s。" %(count_num, pass_num, fail_num, pass_percent, fail_percent)
        self.send_email(user_list, sub, content)

if __name__ == '__main__':
    send = SendEmail()
    send.send_main([1,2,3,4],[5,6,7,8,9])
    print(sys.path)





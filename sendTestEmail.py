#!/usr/bin/env python
#coding=utf-8
# 发送测试邮件

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import argparse

class MyEmail:
    def __init__(self):
        self.user = None
        self.password = None
        self.to_list = []
        self.cc_list = []
        self.content = None
        self.tag = None
        self.doc = None


    def send(self):
        try:
        # 链接服务器
            server = smtplib.SMTP_SSL("smtp.exmail.qq.com", port=465)

            #登陆
            server.login(self.user, self.password)

            #发送邮件
            server.sendmail("<%s>" % self.user, self.to_list, self.get_attach())

            #关闭
            server.close()

            print('发送邮件成功')

        except Exception as e:
            print(e)
            print('发送邮件失败')


    def get_attach(self):

        #构造邮件内容
        attach = MIMEMultipart()

        if self.tag is not None:
            # 主题,最上面的一行
            attach["Subject"] = self.tag

        if self.user is not None:
            # 显示在发件人
            attach["From"] = "<%s>" % self.user

        if self.to_list:
            # 收件人列表
            attach["To"] = ";".join(self.to_list)

        if self.cc_list:
            # 抄送列表
            attach["Cc"] = ";".join(self.cc_list)

        if self.content:
            msg = MIMEText(self.content, 'plain', 'utf-8')
            attach.attach(msg)

        return attach.as_string()


# 生成邮件主题
def create_subject(name, version):
    content = "%s %s 提测" % (name,version)
    return content


# 拼接邮件内容
def create_content(name, version):
    # app下载地址
    load_url = 'https://testdownapp.liaodaotiyu.com/app/ios/liaodao/insideTest/index.html'

    # 设计稿地址
    design_url = 'http://lottery.gs.9188.com/liaodao/pm/dash/#g=1&p=native'

    content = "Dear all:\n%siOS端已经完成开发,现提交测试.\napp下载地址:%s\n原型稿和UI设计稿:%s" % (name, load_url, design_url)
    return content


# 发送邮件
def send_email(content, subject):
    sender = MyEmail()
    sender.user = "shigaoqiang@caiyikeji.com"
    sender.password = "Sgq199112180059"
    sender.tag = subject
    sender.content = content
    sender.to_list = ["shigaoqiang@caiyikeji.com", "guojingjing@caiyikeji.com", "zhouyunyun@caiyikeji.com","yanxingxing@caiyikeji.com"]
    sender.cc_list = ["liaodao@caiyikeji.com"]
    sender.send()


def main_command():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", help="版本号", metavar="version")
    parser.add_argument("-n", "--name", help="包名", metavar="name")
    parser.add_argument("-m", "--desc", help="自动发送提测邮件, 必选携带参数包括 -v 版本号 -n 包名", metavar="description")
    options = parser.parse_args()

    name = options.name
    version = options.version

    # 邮件内容
    content = create_content(name, version)

    # 邮件主题
    subject = create_subject(name, version)

    if not name is None and not version is None:
        print(subject + '\n' + content)

        send_email(content, subject)

    else:
        print("自动发送提测邮件, 必选携带参数包括 -v 版本号 -n 包名")


if __name__ == '__main__':
    main_command()
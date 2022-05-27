"""
============================
Author: 潘师傅
Time: 2021/8/2 10:22
Project: wex_api
Company: 厦门微尔笑网络科技有限公司
============================
"""


import yagmail


class SendMail(object):

    def __init__(self, user, password, host, port):
        """
        连接服务器
        :param user:    *邮箱账号
        :param password:    *授权码
        :param host:    *协议
        :param port:    *端口
        """
        self.user = user
        self.password = password
        self.mail = yagmail.SMTP(user=self.user, password=self.password, host=host, port=port)

    def send_mail(self, theme, to, content=None, attachments=None, cc=None):
        """
        发送邮件
        :param theme: *主题
        :param content: 内容
        :param attachments: 附件
        :param to:  *收件人
        :param cc:  * 抄送
        :return:
        """
        # 发送邮件
        self.mail.send(
            to=to,  # 如果多个收件人的话，写成list就行了，如果只是一个账号，就直接写字符串就行to='736297001@qq.com'
            # ['34414822@qq.com', 'chenxiaomumu@163.com', '736297001@qq.com', '23071059@qq.com'] -- 多个
            subject=theme,  # 主题
            contents=content,  # 内容
            attachments=attachments,  # 附件
            cc=cc  # 抄送a
        )


if __name__ == '__main__':
    FS = SendMail(user='153390680@qq.com', password='obsordardxilcabj', host='smtp.qq.com', port=465)
    FS.send_mail(theme='这个是邮箱主题', content='马鑫是靓仔', to='maxin@kqrj.cn')

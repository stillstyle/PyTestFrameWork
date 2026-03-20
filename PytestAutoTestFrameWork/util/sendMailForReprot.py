# pip install yagmail
import yagmail

class SendMailWithReport:
    """发送测试报告邮件"""

    @staticmethod
    def send_mail(smtp_server, from_user, from_password, to_user,
                  subject, contents, attachment_path):
        """
        发送邮件
        :param smtp_server: 邮件服务器，如 'smtp.qq.com'
        :param from_user: 发送者邮箱
        :param from_password: 发送者邮箱密码或授权码
        :param to_user: 接收者邮箱列表，如 ['xxx@qq.com']
        :param subject: 邮件主题
        :param contents: 邮件正文
        :param attachment_path: 附件路径（测试报告HTML文件）
        """
        try:
            # 连接邮箱服务器
            yag = yagmail.SMTP(user=from_user, password=from_password, host=smtp_server)
            # 发送邮件
            yag.send(to=to_user, subject=subject, contents=contents, attachments=attachment_path)
            print("邮件发送成功！")
        except Exception as e:
            print("邮件发送失败：", e)
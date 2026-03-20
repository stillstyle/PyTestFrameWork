import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

sys.path.append('.')
from config.conf import htmlName, args
from util.sendMailForReprot import SendMailWithReport

def main():
    os.system(args)
    SendMailWithReport.send_mail(
        smtpServer, fromUser, fromPassWord,
        toUser, subject, contents, htmlName
    )

if __name__ == '__main__':
    main()
import yagmail
import configparser
import os

mail_config_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/config' + '/mail_config.ini'
mail_config = configparser.ConfigParser()
mail_config.read(mail_config_path)

user = mail_config['163mail']['user']
password = mail_config['163mail']['password']
host = mail_config['163mail']['host']


def send_mail(to, subject, contents, user=user, password=password, host=host):
    '''https://github.com/kootenpv/yagmail'''
    yag = yagmail.SMTP(user=user, password=password, host=host)
    yag.send(to=to, subject=subject, contents=contents)

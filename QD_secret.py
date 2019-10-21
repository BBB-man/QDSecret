
#-*- coding:utf-8 -*-
'''
随机密码生成器
author:QD
string functions:
    ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
'''
from random import choice
import string
import time
 
#python3中为string.ascii_letters,而python2下则可以使用string.letters和string.ascii_letters
 
def GenPassword(length=8,chars=string.ascii_letters+string.digits+string.punctuation):
    return ''.join([choice(chars) for i in range(length)])


if __name__=="__main__":
    # print(GenPassword(12))  # 密码的长度为12,可随意修改
    QD_input = raw_input("请输入账号 >>> ")
    sec = str(QD_input) + "    " + GenPassword(12) + "    "+ str(time.strftime("%Y-%m-%d %H:%M:%S"))
    with open('QD.txt','a') as f:
    	print sec
        f.write("\n"+sec)

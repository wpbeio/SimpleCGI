#!C:\Users\beioo\Anaconda3\python.exe
#-*- coding:utf-8 -*-

# print('ssss')
print('Content-type:text/html\n\n')

from os.path import join, abspath
import cgi
import hashlib
import sys

BASE_DIR = abspath('data')
# print(BASE_DIR)
form = cgi.FieldStorage()
import urllib.parse
text = form.getvalue('text')
print('len(text)=', len(text))
text = urllib.parse.unquote(text)
# print(text)
filename = form.getvalue('filename')
# print(filename)
password = form.getvalue('password')
# print(password)
if not (filename and text and password):
    print('参数输入有问题')
    sys.exit()
# print(hashlib.md5.update(password).hexdigest())
m = hashlib.md5()
m.update(password.encode('utf-8'))
#print(password, m.hexdigest())
if m.hexdigest() != '3858f62230ac3c915f300c664312c63f':
    print('密码输入有问题')
    sys.exit()
#print(text.encode('utf-8', 'ignore').decode())
try:
    f = open(join(BASE_DIR, filename), 'w')
    f.write(text)
    f.close()
    print('文件保存完毕')
except Exception:
    f.close()
    print('文件保存失败')

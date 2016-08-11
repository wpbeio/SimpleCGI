#!C:\Users\beioo\Anaconda3\python.exe
# -*- coding:utf-8 -*-

print('Content-type:text/html\n')

from os.path import join, abspath

import cgi
import sys

BASE_DIR = abspath('data')
# print(BASE_DIR)

form = cgi.FieldStorage()
filename = form.getvalue('filename')
if not filename:
    print('请输入正确的文件名')
    sys.exit()
text = open(join(BASE_DIR, filename),encoding= 'utf-8').read()
print("""
<html>

    <head>

        <title>编辑中</title>
    </head>
    <body>
        <form action='save.cgi' method='POST' >
        <b>文件：</b>{0}<br />
        <input type='hidden' value={1} name='filename'/>
        <b>密码：</b><br/>
        <input name='password' type=password/><br/>
        <b>文本：</b><br />

        <textarea row='20' cols='40' name='text'>{2}</textarea><br/>
        <input type='submit' value='保存'/>
        </form>
    </body>
</html>
      """.format(filename, filename, text).encode('utf-8').decode())

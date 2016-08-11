#!C:\Users\beioo\Anaconda3\python.exe
#-*- coding:utf-8 -*-
import codecs
import cgi
form = cgi.FieldStorage()


text = form.getvalue('text', open(
    'data/simple_edit.dat').read().encode('utf-8').decode())


print("""Content-type:text/html

<html>
    <head>
     <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>A Simple Editor</title>
    </head>
    <body>
        <form action='simple_edit.cgi' method='POST' charset='utf-8'>
        <textarea row='10' cols='20' name='text'>{0}</textarea><br/>
        <input type='submit'/>
        </form>
    </body>
</html>
      """.format(text).encode('utf-8').decode())
with open('simple_edit.dat', 'w') as f:
    f.write(text)

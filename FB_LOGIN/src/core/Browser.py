'''
Created on 7 Mar, 2015

@author: wangyi
'''

import mechanize
import http.cookiejar

class Browser(object):
    
    def __init__(self, url=None):
        self._browser = mechanize.Browser()
        
        # Cookie Jar
        self._browser.set_cookiejar(http.cookiejar.LWPCookieJar())
        # set header
        self._browser.set_handle_robots(False)
        self._browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        
        # open some site
        self.response = self._browser.open("www.facebook.com/login") 
        
        # show available forms
        for f in self._browser.forms():
            print(f)
            
    
if __name__ == "__main__":
    browser = Browser()        
        
        

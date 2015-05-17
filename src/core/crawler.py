# -*- coding: utf-8 -*-
'''
Created on 23 Dec, 2014

@author: wangyi, Researcher Associate @ EIRAN, Nanyang Technological University

@email: L.WANG@ntu.edu.sg

@copyright:  2014 organization_name. All rights reserved.

@license:    license

@decription:

@param: 
'''
import urllib
import urllib2

from pyquery import PyQuery as pq

from framework.event.Event import *

__default__ = "http://s.taobao.com/search?initiative_id=staobaoz_20120515&q=%3F%3F&suggest=history_1&_input_charset=utf-8&source=suggest&tab=all&bcoffset=1&s=0"

import os
# files path config
pwd = os.path.dirname( os.path.realpath(__file__) )

class Browser(object):
    
    def __init__(self, client, url=__default__, target=None):
        import subprocess     
        self.args = ["/usr/local/bin/phantomjs", pwd +"/js/" + client, url, target]#, "--ignore-ssl-errors=true"
        self.call = subprocess
         

# filter event
class Filter(Event):
      
    def __init__(self, doc=None):
          
        Event.__init__(self, doc)
  
# parser event        
class HTMLParser(Event):
      
    def __init__(self, doc=None):
          
        Event.__init__(self, doc) 

class Crawler(object):
    
    entryHttpUrl = __default__
    user_agent = 'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25'
    headers = { 'User-Agent' : user_agent }
    
    maxOfBucket = 1000
    
    # attach events for triggers
    _parser = HTMLParser('html parser')
    _filter = Filter('html filter')
    
    def __init__(self, url=__default__):
        
        self.entryHttpUrl = url
    
    def craw(self, entity, url=__default__, *tags, **hints):
        if  hints != {}:   
            self.data = urllib.urlencode(hints)

# I want to change it later with encryped data
#       req = urllib2.Request(url, self.data, self.headers)
        req = urllib2.Request(url)
        
        try:
            response = urllib2.urlopen(req)
            xmlfile  = response.read()
            
# save files for testing
            self.save(xmlfile)
            
            # for memory processing
            htmlpage = xmlfile.decode('gbk')
 
# Jquery lib           
            dom = pq(htmlpage)

# Examples:            
#           MerchanEntry = dom("#J_SearchForm").attr("action")
#           MerchanEntries = dom(".crumbs-items").text()
# Just for str or unicode results: 
#           print(MerchanEntries.encode("gbk",'ignore'))
            
#           MerchantEntries = dom("div.item-box.st-itembox") 
                                        
            dict = self.parse(dom, entity, tags)
            
            return dict
            
        except urllib2.HTTPError as e:
            pass 
        
    # e.g: Tao Bao
    # <a class="J_Ajax J_Pager link icon-tag" href="#" title="下一页" trace="srp_select_pagedown" data-url="pager" data-key="s" data-value="132">
    #    <span class="icon-btn-next-2"></span>
    # </a>
    # to get optimal url initialization    
    def parse(self, *args, **keywords):
        return self._parser(*args, **keywords)
    
    def save(self, html):
        with open("web.html", "w") as webpage:
            # save file for investigation
            webpage.write(html)
    
    def _AJAX_Crawling_test(self, url=__default__):
        
        from framework.webkit import Driver, __default__#, __driver__
        
        driver = Driver(url, driver=__default__)
        
        for i in range(0, 5):
            
            # one should wait for a moment
            driver.get('下一页'.decode('utf8'), type='partial_link_text').click()
            
            print(driver.driver.current_url)

    def _AJAX_Crawling_Mini_Browser(self, url=__default__):
        self.browser = None
    
#     # filter event
#     class Filter(Event):
#           
#         def __init__(self, doc=None):
#               
#             Event.__init__(self, doc)
#       
#     # parser event        
#     class HTMLParser(Event):
#           
#         def __init__(self, doc=None):
#               
#             Event.__init__(self, doc)       
        
        

# initial url
URL_INIT = "http://s.taobao.com/search?initiative_id=staobaoz_20120515&q=%3F%3F&suggest=history_1&_input_charset=utf-8&source=suggest&tab=all&bcoffset=1&s=0"
        
# Crawler()._AJAX_Crawling_test(URL_INIT)        

# test record: 5       
"""
http://s.taobao.com/search?initiative_id=staobaoz_20120515&q=%3F%3F&suggest=history_1&_input_charset=utf-8&source=suggest&tab=all&bcoffset=1&s=0
http://s.taobao.com/search?initiative_id=staobaoz_20120515&q=%3F%3F&suggest=history_1&_input_charset=utf-8&source=suggest&tab=all&bcoffset=1&s=44
http://s.taobao.com/search?initiative_id=staobaoz_20120515&q=%3F%3F&suggest=history_1&_input_charset=utf-8&source=suggest&tab=all&bcoffset=1&s=88
http://s.taobao.com/search?initiative_id=staobaoz_20120515&q=%3F%3F&suggest=history_1&_input_charset=utf-8&source=suggest&tab=all&bcoffset=1&s=132
http://s.taobao.com/search?initiative_id=staobaoz_20120515&q=%3F%3F&suggest=history_1&_input_charset=utf-8&source=suggest&tab=all&bcoffset=1&s=176

"""  

# handler
def tbhtmlOnParser(obj, dom, client, tags, **hints):
    # tags analysis: string is value based
    param = {}
    str = ""
    for tag in tags:
        str = '_' + str + tag
     
    tablename = client.__class__.__name__ + str
    
    param['tablename'] = tablename        
    
    # get xml elements
    param['data'] = client(dom, str)
    
    return param 
        



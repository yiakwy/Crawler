# -*- coding: utf-8 -*-
'''
Created on 7 Jan, 2015

@author: wangyi
'''
from datetime import *
# for taobao
values = {
        "initiative_id":datetime.now().strftime('staobaoz_%Y%m%d') ,#initiative_id=staobaoz_20120515
        "q":u'手表'.encode('gbk') ,#q=%3F%3F
        "suggest":'history_1' ,#suggest=history_1
        "_input_charset":'utf-8', #_input_charset=utf-8
        "source":'suggest', #source=suggest
        "tab":'all', #tab=all
        "bcoffset":'1', #bcoffset=1
        "s":'0', #s=0
}

class TestCrawler(object):
    
    def __init__(self):
        
        pass
    
    def test_crawler(self):
        
        from core.crawler import Crawler, tbhtmlOnParser
        from DBManagement.models import Shop
        
        crawler = Crawler()
        
        crawler._parser.register(tbhtmlOnParser)
        
#       entryHttpUrl = "http://s.taobao.com/search?"
        entryHttpUrl = "http://s.taobao.com/search?initiative_id=staobaoz_20120515&q=手表&suggest=history_1&_input_charset=utf-8&source=suggest&tab=all&bcoffset=1&s="
        
        list = []
        
        tag = '手表'
        
        for page in range(0, 100):
            # modify data template
            values['s'] = str(page)
        
            tbData  = crawler.craw( Shop() , entryHttpUrl + str(page * 44), tag, **values) 
            
            # identify the page number
            tbData['page'] = page
            
            list.append( tbData )
            
            print(tbData['data'])
            
        return list
    
if __name__ == "__main__":
    TestCrawler().test_crawler()

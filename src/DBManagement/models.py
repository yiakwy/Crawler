# -*- coding: utf-8 -*-
'''
Created on 27 Aug, 2014

@author: wangyi
'''

from datetime import *
from copy import *

import re

class Shop(object):
    '''
    classdocs
    '''
    param = {
#   'id'                 : None,
    'title'              : None, 
#   'tmv'                : None,
#   'price'              : None,
#   'merchanturl'        : None,
    'httpurl_shop'       : None,
    'httpurl_commodity'  : None,
#   'rank'               : 'NULL',
    'noOfBuiers'         : 'NULL',
    'noOfComments'       : 'NULL'
    }
    
    htmlmapping = {
        'shop':"div.col.item.st-item",  
        'entry':"div.tb-content",   
    }
    
    items = 100
    
    sqlcreate = """
CREATE TABLE `TBMerchantCredit`.`%s` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `httpurl_shop` VARCHAR(45) NOT NULL,
  `httpurl_commodity` VARCHAR(45) NOT NULL,  
  `title` VARCHAR(45) NOT NULL,
  `tags` VARCHAR(45) NOT NULL,
  `rank_tags` INT NULL,
  `price` INT NULL,  
  `tmv` DATE NOT NULL,
  `noOfBuiers` INT NULL,
  `noOfComments` INT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `rank_tags_UNIQUE` (`rank_tags` ASC));    
"""
    sqlinsert = """
INSERT INTO %s (`id`, `httpurl_shop`, `httpurl_commodity`, `title`, `tags`, `price`, `rank_tags`, `noOfBuiers`, `noOfComments`, `tmv`) VALUES (NULL, %(httpurl_shop)s, %(httpurl_commodity)s, %(title)s, %(tags)s, %(price)s, %(rank_tags)s, %(noOfBuiers)s, %(noOfComments)s, now())    
"""
#data = [('www.yiak.co', 'shiyishi', 'shoubiao', 1,2,3), ('www.yiak.co2', 'shiyishi2', 'shoubiao', 4,5,6)]
    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def extractEntry(self, dom):
        try:
            ShopsEntries = dom.find("div#mainsrp-itemlist")
            
            # 9-2015，formatter
            #dom("div#mainsrp-spucombo")
            # 9-2014, formatter
            #dom("div.tb-content").children("div.col.item.st-item")
        except Exception as e:
            raise(e)
        
        return ShopsEntries
        
    def extractShopUrl(self, shopAnchor):
        try:
            self.param['httpurl_shop'] = shopAnchor("div.col.seller").children("a").attr("href")#div.col.seller.feature-dsi-tgr.popup-tgr
        except Exception as e:
            raise(e)
    
    def extractCommUrl(self, shopAnchor):
        try:               
            self.param['httpurl_commodity'] = shopAnchor("h3.summary").children("a").attr("href")           
        except AttributeError as e:
            raise(e)        
        
    def extractTitle(self, shopAnchor):
        try:        
            self.param['title'] = shopAnchor("h3.summary").children("a").attr("title")                     
        except AttributeError as e:
            raise(e)
    
    def extractNumofBuyers(self, shopAnchor):
        try:
            pattern = re.compile("\d+")
            noOfBuierstxt = shopAnchor("div.col.end.dealing").text()#.encode('unicode-escape')
            self.param['noOfBuiers'] = int(re.search(pattern, noOfBuierstxt).group())
        except AttributeError as e:
            raise(e)
    
    def extractPrice(self, shopAnchor):
        try:
            pattern = re.compile("\d+\.\d+")
            pricetxt = shopAnchor("div.col.price.g_price.g_price-highlight").text()#.encode('unicode-escape')
            self.param['price'] = float(re.search(pattern, pricetxt).group()) 
        except AttributeError as e:
            raise(e)  
      
        
    def fire(self, dom, tags_str):
        self.param['tags'] = tags_str
        
        index =  0
        list  = [ ]
        
        while index < self.items:
            
            try:
                self.param['rank_tags'] = index
                
                # get shop anchor
                shopAnchor = self.extractEntry(dom).eq(index)
                
                # get details
                self.extractShopUrl(shopAnchor)
                self.extractCommUrl(shopAnchor)
                
                self.extractTitle(shopAnchor)
                self.extractNumofBuyers(shopAnchor)
                self.extractPrice(shopAnchor)
                
                list.append( self.param.copy() )
                
                index += 1
            except AttributeError as e:
                break 
                       
        return list
        
    __call__ = fire
            

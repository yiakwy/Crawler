# -*- coding: utf-8 -*-
'''
Created on 22 Dec, 2014

@author: wangyi
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from framework.event.Event import *

import contextlib

import os
# files path config
pwd = os.path.dirname( os.path.realpath(__file__) )

CHROME_DIR = pwd + "/" + "chromedriver"

# test using google browser
#__driver__ = webdriver.Chrome(executable_path=CHROME_DIR)

# headless testing
__default__ = webdriver.PhantomJS(executable_path="/usr/local/bin/phantomjs")

class Get_Element(Event):
    
    def __init__(self, doc=None):
        
        Event.__init__(self, doc)
        

class Driver(object):
    # fetch event
    fetchr = Get_Element('get')#Get_Element('get')
    
    def __init__(self, url, driver=__default__):
        self.driver = driver #webdriver.PhantomJS(executable_path="/usr/local/bin/phantomjs").get(url)
        
        self.driver.get(url)
        
        self.fetchr.register(onGet)
        
    def get(self, *arg, **keywords):
        # firing fetch event
        return self.fetchr(*arg, **keywords)
    
    @contextlib.contextmanager
    def ctx(self):
        try:
            yield
        finally:
            self.driver.close()     

# handler for get event
def onGet(obj, *tag, **keywords):
    
    obj.driver.page_source.encode('utf8')
    
    try:
        position = keywords['position']
        
        if  position == None:
            position  = slice()
        
    except KeyError:
         
        position = 0
    
    # calling API
    if   keywords['type'] == 'id':
        return obj.driver.find_elements_by_id(*tag)[position]
    elif keywords['type'] == 'css':
        return obj.driver.find_elements_by_css_selector(*tag)[position]
    elif keywords['type'] == 'partial_link_text':
        return obj.driver.find_elements_by_partial_link_text(*tag)[position]

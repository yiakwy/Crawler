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

__driver__ = webdriver.Chrome(executable_path=CHROME_DIR)
__default_driver__ = webdriver.PhantomJS(executable_path="/usr/local/bin/phantomjs")

class Get_Element(Event):
    
    def __init__(self, doc=None):
        
        Event.__init__(self, doc)
        

class Driver(object):
    # fetch event
    fetchr = Get_Element('get')#Get_Element('get')
    
    def __init__(self, url, driver=__default_driver__):
        self.driver = driver #webdriver.PhantomJS(executable_path="/usr/local/bin/phantomjs").get(url)
        
        self.driver.get(url)
        
    def get(self, arg):
        # firing fetch event
        return self.fetchr(arg) 
    
    @contextlib.contextmanager
    def ctx(self):
        try:
            yield
        finally:
            self.driver.close()     

def onGet(obj, tag):
    obj.driver.find_element_by_name(tag)

driver = Driver("http://www.python.org", __driver__)

#register a handle
driver.fetchr.register(onGet)
 
xmltxt = driver.get('q')

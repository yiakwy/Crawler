'''
Created on 8 Jan, 2015

@author: wangyi
'''

class TestBrowser(object):
    
    def __init__(self):
        
        pass
    
    def test_browser(self):
        
        from core.crawler import Browser
        
        browser = Browser("test.js", "http://ariya.github.io/svg/tiger.svg", "tiger.png")#phantomjs rasterize.js http://ariya.github.io/svg/tiger.svg tiger.png
        
        try:
            result = browser.call.check_output(browser.args)
            
            print(result)
        except Exception as e:
            browser.call.kill()
            raise(e)
        
        
if __name__ == "__main__":
    TestBrowser().test_browser()

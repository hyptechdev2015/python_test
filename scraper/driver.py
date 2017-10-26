'''
Created on Oct 25, 2017

@author: kevin
'''

'''
Created on Oct 25, 2017

@author: kle
'''

'''
Created on Oct 25, 2017

@author: kle
'''
from selenium import webdriver

class Driver(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.webdriver = webdriver
       

    def init_phantomjs_driver(self, *args, **kwargs):
        '''
        init_phantomjs_driver
        '''
        headers = { 'Accept':'text/html,application/xhtml+xml,application/xml,application/json;q=0.9,*/*;q=0.8',
            'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
            'Connection': 'keep-alive'
        }
    
        for key, value in headers.items():
            self.webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.{}'.format(key)] = value
    
        self.webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.settings.userAgent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
        self.webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.settings.javascriptEnabled'] = 'True'
            
        driver =  self.webdriver.PhantomJS(*args, **kwargs)
        driver.set_window_size(1400,1000)
    
        return driver         
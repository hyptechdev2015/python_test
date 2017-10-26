'''
Created on Oct 25, 2017

@author: kle
'''
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException, ElementNotSelectableException,NoSuchElementException
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from scraper.driver import Driver


class Lowes(object):
    '''
    classdocs
    '''  
    def __init__(self, browser=None):
        '''
        Constructor
        '''
        if browser:
            self.browser = browser
        else:
            self.browser = Driver().init_phantomjs_driver()  
                     
    def scrap_it(self, url, args):
        
        if self.browser is None:
            raise Exception("webdriver not initialize")
        
        #browser = init_phantomjs_driver() #service_args=service_args)
         
        self.browser.implicitly_wait(10)
        #browser.set_window_size(800, 600)
        #browser.set_page_load_timeout(60)
        self.browser.get(url)
                    
        try:   
            wait = WebDriverWait(self.browser, 10)
                    
            #proceed = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "pd-price grid-100")))
            
            self.browser.save_screenshot('screenshot_'+args+'-1.png')
            #print(browser.page_source.encode('utf-8'))
            addCartEl = None
            try:
                addCartEl = wait.until(EC.visibility_of_element_located(((By.XPATH, "//*[@id='add-to-cart-form']/div/div[4]/button"))))
            except Exception as e:
                print("no AddCart: " + str(e))    
            except:
                print("skip this AddCart")
                pass
            
            print(addCartEl)               
            if addCartEl is None:        
                try:    
                        # click proceed
                    searchkey = "92841"
                    searchbox = self.browser.find_element_by_id("zipcode-input")
                    searchbox.clear()
                    searchbox.send_keys(searchkey)
                    print ("\nSearching for zip %s ..." % searchkey)
                    
                    proceedZip = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='store-locator-form']/div/div/span[2]/button")) ) #"/html/body/div[1]/div/div[3]/section[1]/div[3]/div[1]/form/div/div/span[2]/button")) )
                    proceedZip.click()     
                    
                    #zip popup
                    wait.until(EC.presence_of_element_located((By.ID, "store-locator-modal")))
                        
                        #zipList = wait.until( )js-SL-list find-a-store-list
                        #click on one store
                    WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='store-locator-modal']/div[2]/div/div[2]/div[1]/div/ul/li[1]/div/div[2]/button")) ).click()                    
                            
                    #proceed = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='add-to-cart-form']/div/div[4]/button")) )    
                    #proceed.click()
                     
                    # wait for the content to be present ADD to Cart
                    #wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-form']/div/div[4]/button")))
                    WebDriverWait(self.browser,10).until(EC.visibility_of_element_located(((By.ID, "add-to-cart-modal"))))
                      
                    self.browser.save_screenshot('screenshot_'+args+'-2.png') 
                except ElementNotSelectableException as e:    
                    print("ele: " + str(e) )          
            
                except Exception as e:
                    print("exp for rap:" + str(e))    
                except:
                    print("skip this proce")
                    pass
                                
            #tree = html.fromstring(browser.page_source)
            #print(tree)    
            
            #htmlOut = self.browser.page_source.encode('utf-8')    
            #print(htmlOut)
            
            
            soup = BeautifulSoup(self.browser.page_source,"lxml")
            
            title = soup.find('title')
            links = soup.find('link', rel='canonical')
            
            pClass = soup.find_all("span",{"itemprop":"price"})[0]
            #print(pClass)
            #print(type(pClass))
            price = pClass['content']
            print(title.string)
            print(links["href"])
            print(price)
            
            
            #try:
            #    soup = BeautifulSoup(htmlContent, 'lxml')
            #    with open("output3.html", "w") as file:
            #        file.write(str(soup))        
            #except AttributeError as e:
            #    print(e)
                
            print("done saved output!")
           
        except TimeoutException as e:
            #Handle your exception here
            self.browser.save_screenshot('screenshot_'+args+'-timeout.png')
            print("timout:" + str(e))
        except Exception as e:
            print("exp: " + str(e))
        
        
        finally:
            print("done: " + args)
            #self.browser.quit()        
    def dispose(self):
        self.browser.quit()          
            
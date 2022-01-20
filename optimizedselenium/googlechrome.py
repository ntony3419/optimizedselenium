import traceback

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from time import sleep
from shutil import which
from selenium.webdriver.common.action_chains import ActionChains

class Chrome_Browser():
    
    def __init__(self,driver_path, **kwargs):
        #profile_path=None, profile_number=None, window_size=None, maximize=False,headless=False):
        options = Options()  
        # default options
       
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    
        options.add_argument("--disable-notifications")  # disable the allow or disallow notification
        ''' codeBlock: disable automatic control to bypass cloudflare by remove navigator.webdriver flag 
                   google chrome only'''
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        # chrome_options.add_experimental_option("detach", True)
        if "profile_path" in kwargs and "profile_number" in kwargs:
            options.add_argument(r"user-data-dir={}".format(kwargs["profile_path"]))
            options.add_argument(r"profile-directory={}".format( kwargs["profile_number"]))        
        #instance driver browser        
        try:
            window_size = None        
            if "headless" in kwargs:
                options.add_argument("--headless")
            else: 
                if "window_size" in kwargs:
                    window_size = kwargs["window_size"].split(",")

            self.driver_browser = webdriver.Chrome(executable_path=driver_path, options=options)
            
            if  "maximize" in kwargs :
                    self.driver_browser.maximize_window()
            else:
                    if window_size is not None:
                        self.driver_browser.set_window_size(window_size[1],window_size[0])

        except :
            print("Issue opening google chrome {}".format(traceback.format_exc()))
            exit()

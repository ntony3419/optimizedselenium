import undetected_chromedriver.v2 as uc
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
import traceback

class Undetect_Chrome():
    def __init__(self, driver_path,**kwargs):        

        options = uc.ChromeOptions()       
             
      

        if "profile_path" in kwargs and "profile_number" in kwargs:
            options.add_argument(r"user-data-dir={}".format(kwargs["profile_path"]))
            options.add_argument(r"profile-directory={}".format( kwargs["profile_number"]))        

        try:
            window_size = None
            headless= False
            if "headless" in kwargs:
                options.add_argument("--headless")            
                headless = True
            else: 
                if "window_size" in kwargs:
                    window_size = kwargs["window_size"].split(",")
            
            self.driver_browser =uc.Chrome( executable_path=driver_path,options=options)
            
            if headless is False :
                if "maximize" in  kwargs:
                    self.driver_browser .maximize_window()
                else:
                    if window_size is not None:
                        self.driver_browser .set_window_size(window_size[1],window_size[0])
        except :
            print(f"Issue opening google chrome {traceback.format_exec()}")
            exit()
        
   
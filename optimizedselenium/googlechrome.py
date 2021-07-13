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
    def __init__(self,driver_path, profile_path, profile_number, window_size, maximize,headless):
        self.options = Options()

        # default options
        if headless is True:
            self.options.add_argument("--headless")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        # if window_size is not None:
        #     win_size = f"--window-size={window_size}"
        #     self.options.add_argument(win_size)
        # else:
        #     self.options.add_argument("--window-size=1920,1080")
        # if maximize is True:
        #     self.options.add_argument("--start-maximized")
        self.window_size = None
        if window_size is not None:
            self.window_size = window_size.split(",")

        self.maximize = False
        if maximize is True:
            self.maximize = True
        self.options.add_argument("--disable-notifications")  # disable the allow or disallow notification
        ''' codeBlock: disable automatic control to bypass cloudflare by remove navigator.webdriver flag 
                   google chrome only'''
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option("useAutomationExtension", False)
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        # chrome_options.add_experimental_option("detach", True)
        if profile_path is not None:
            profile_path = r"user-data-dir={}".format(profile_path)
            profile = r"profile-directory={}".format(profile_number)
            self.options.add_argument(profile_path)
            self.options.add_argument(profile)
        self.driver_path = driver_path
    def browser_driver(self):
        driver = None
        # driver_path = '''f"{os.path.dirname(os.path.abspath(__file__))}\{'chromedriver_91.exe'}"'''
        try:
            driver = webdriver.Chrome(executable_path=self.driver_path, options=self.options)
            if self.maximize is True:
                driver.maximize_window()
            if self.window_size is not None and self.maximize is False:
                driver.set_window_size(self.window_size[1],self.window_size[0])

        except (WebDriverException, FileNotFoundError):
            print(f"Can't find the executable <.exe> of google chrome at <{self.driver_path}> !!\nMake sure the executable file and path to its executable in setting.conf match each other\nAttemp to use full path to the executable!!")
            exit()

            #print(traceback.format_exc())
            # raise Exception(f"Unable to open browser with according profile."
            #                  f"Possible issue and solution: "
            #                  f"\n- Profile is in used: Close all the google chrome tabs to release the profile"
            #                  f"\n- Chrome Driver doesn't exist: download chrom driver associate with chrome version from https://chromedriver.chromium.org/downloads"
            #                  f"\n- Chrome Driver version different: download new chrome driver assosicate with chrome version from https://chromedriver.chromium.org/downloads")
        return driver


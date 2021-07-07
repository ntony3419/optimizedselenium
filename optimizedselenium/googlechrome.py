from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class Chrome_Browser():
    def __init__(self,driver_path, profile_path, profile_number, window_size, maximize,headless):
        self.options = Options()

        # default options
        if headless is True:
            self.options.add_argument("--headless")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        if window_size is not None:
            win_size = f"--window-size={window_size}"
            self.options.add_argument(win_size)
        else:
            self.options.add_argument("--window-size=1920,1080")
        if maximize is True:
            self.options.add_argument("--start-maximized")
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
    def browser(self):
        driver = None
        # driver_path = '''f"{os.path.dirname(os.path.abspath(__file__))}\{'chromedriver.exe'}"'''
        try:
            driver = webdriver.Chrome(executable_path=self.driver_path, options=self.options)
        except:
            raise Exception(f"Unable to open browser with according profile."
                             f"Possible issue and solution: "
                             f"\n- Profile is in used: Close all the google chrome tabs to release the profile"
                             f"\n- Chrome Driver doesn't exist: download chrom driver associate with chrome version from https://chromedriver.chromium.org/downloads"
                             f"\n- Chrome Driver version different: download new chrome driver assosicate with chrome version from https://chromedriver.chromium.org/downloads")
        return driver

    def scroll_down(driver, amount):
        i = 1
        screen_height = driver.execute_script("return window.screen.height;")
        keep_scroll = True
        while keep_scroll:

            driver.execute_script(
                "window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
            i += 1
            sleep(10)  # wait for the page to load
            scroll_height = driver.execute_script("return document.body.scrollHeight;")
            if amount == 0 and (screen_height * i) > scroll_height:  # unlimited scrolling untill reach end of page
                keep_scroll = False
            elif amount != 0 and i >= amount:  # only scrol untill i reach amount of scroll
                keep_scroll = False

        # TODO: developing type_text simulation

    def type_text(driver, wait_time, frequence, list_error_to_ignored, xpath, text):
        default_exception_to_ignore = [ElementNotSelectableException, ElementNotInteractableException,
                                       ElementNotVisibleException, NoSuchElementException]
        element = WebDriverWait(driver, wait_time, poll_frequency=frequence,
                                ignored_exceptions=list_error_to_ignored) \
            .until(EC.presence_of_element_located((By.XPATH, xpath)))

    def get_element_by_xpath(driver, wait_time, frequence, list_error_to_ignored, xpath):
        getable_ele = None
        default_exception_to_ignore = [ElementNotSelectableException, ElementNotInteractableException,
                                       ElementNotVisibleException, NoSuchElementException]
        if list_error_to_ignored is None:
            list_error_to_ignored = default_exception_to_ignore
        try:
            getable_ele = WebDriverWait(driver, wait_time, poll_frequency=frequence,
                                        ignored_exceptions=list_error_to_ignored) \
                .until(EC.presence_of_element_located((By.XPATH, xpath)))
        except:
            pass
        # send post data to the input field
        return getable_ele

    def get_elements_by_xpath(driver, wait_time, frequence, list_error_to_ignored, xpath):
        getable_ele = []
        default_exception_to_ignore = [ElementNotSelectableException, ElementNotInteractableException,
                                       ElementNotVisibleException, NoSuchElementException]
        if list_error_to_ignored is None:
            list_error_to_ignored = default_exception_to_ignore
        try:
            getable_ele = WebDriverWait(driver, wait_time, poll_frequency=frequence,
                                        ignored_exceptions=list_error_to_ignored) \
                .until(EC.presence_of_element_located((By.XPATH, xpath)))
        except:
            pass
        # send post data to the input field
        return getable_ele

    def clickable_btn(driver, wait_time, frequence, list_error_to_ignored, xpath):
        clickable_btn = None
        default_exception_to_ignore = [ElementNotSelectableException, ElementNotInteractableException,
                                       ElementNotVisibleException, NoSuchElementException]
        if list_error_to_ignored is None:
            list_error_to_ignored = default_exception_to_ignore
        try:
            clickable_btn = WebDriverWait(driver, wait_time, poll_frequency=frequence,
                                          ignored_exceptions=list_error_to_ignored) \
                .until(EC.element_to_be_clickable((By.XPATH, xpath)))
        except:
            pass
        # send post data to the input field
        return clickable_btn

    def send_text(driver, wait_time, frequence, list_error_to_ignored, xpath, text):
        default_exception_to_ignore = [ElementNotSelectableException, ElementNotInteractableException,
                                       ElementNotVisibleException, NoSuchElementException]
        if list_error_to_ignored is None:
            list_error_to_ignored = default_exception_to_ignore
        try:
            WebDriverWait(driver, wait_time, poll_frequency=frequence, ignored_exceptions=list_error_to_ignored) \
                .until(EC.presence_of_element_located((By.XPATH, xpath))) \
                .send_keys(text)
        except:
            raise Exception(
                "ISSUE: can't send text.\nSOLUTION: update xpath for text field.\nBetter to update xpath before press OK")

#bro = Chrome_Browser("chromedriver_90.exe",r"C:\Users\quang nguyen\AppData\Local\Google\Chrome\User Data", "Profile 6", "800x600",False,False)
bro = Chrome_Browser("chromedriver_90.exe",None,None, "860,400",False,False)
browser=bro.browser()
browser.get(r"https:\\google.com")
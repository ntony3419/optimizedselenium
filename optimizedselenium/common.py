from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep



def mouse_click(driver, locator_xpath, coordx, coordy):
        element = None
        try:
            element = driver.find_element_by_xpath(locator_xpath)
        except:
            pass

        ActionChains(driver).move_to_element(element).move_by_offset(coordx, coordy).click_and_hold().perform()
        ActionChains(driver).move_to_element(element).move_by_offset(coordx,coordy).release().perform()



def move_to_element(driver, wait_time, frequence, list_error_to_ignored,xpath):
    default_exception_to_ignore = [ElementNotSelectableException, ElementNotInteractableException,
                                   ElementNotVisibleException, NoSuchElementException]
    if list_error_to_ignored is None:
        list_error_to_ignored = default_exception_to_ignore
    try:
        element=WebDriverWait(driver, wait_time, poll_frequency=frequence,
                                      ignored_exceptions=list_error_to_ignored) \
            .until(EC.presence_of_element_located((By.XPATH, xpath)))
        action = ActionChains(driver)
        action.move_to_element(element).perform()
    except:
        pass
'''scroll down the page certain amount input. 
    if amount = 0 then perform unlimited scroll untill reach end of page
'''
def scroll_down(browser_driver, amount):
    i = 1
    screen_height = browser_driver.execute_script("return window.screen.height;")
    keep_scroll = True
    while keep_scroll:

        browser_driver.execute_script(
            "window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
        i += 1
        sleep(10)  # wait for the page to load
        scroll_height = browser_driver.execute_script("return document.body.scrollHeight;")
        if amount == 0 and (screen_height * i) > scroll_height:  # unlimited scrolling untill reach end of page
            keep_scroll = False
        elif amount != 0 and i >= amount:  # only scrol untill i reach amount of scroll
            keep_scroll = False


def find_element_by_xpath(browser_driver, xpath, **kwargs):
    getable_ele = None
    default_exception_to_ignore = [ElementNotSelectableException, ElementNotInteractableException,
                                   ElementNotVisibleException, NoSuchElementException]
   
    try:
        if  "list_error_to_ignored" in  kwargs:
            default_exception_to_ignore = kwargs["list_error_to_ignored"]
        if ("wait_time" in kwargs and "freequence" in kwargs):
            getable_ele = WebDriverWait(browser_driver,  kwargs["wait_time"], poll_frequency=kwargs["frequence"],
                            ignored_exceptions=default_exception_to_ignore ) \
                .until(EC.presence_of_element_located(By.XPATH, xpath ) )
        else:            
            getable_ele = WebDriverWait(browser_driver,  5, 1,ignored_exceptions=default_exception_to_ignore) \
                    .until(EC.presence_of_element_located((By.XPATH, xpath)))
    except:
        print('unable to find element\n')
    # send post data to the input field
    return getable_ele

def find_elements_by_xpath(browser_driver, xpath, **kwargs ):
    #wait_time, frequence, list_error_to_ignored, 
    getable_ele = []
    default_exception_to_ignore = [ElementNotSelectableException, ElementNotInteractableException,
                                   ElementNotVisibleException, NoSuchElementException]
    if  "list_error_to_ignored" in  kwargs:
        list_error_to_ignored = default_exception_to_ignore
    if "wait_time" in kwargs and "freequence" in kwargs:
        found = False
        while (found is False and frequence <=kwargs["wait_time"] ):
            try:
                getable_ele = browser_driver.find_elements_by_xpath(xpath)
                found = True
            except:
                pass
            frequence = frequence+1    
    return getable_ele

def sel_click_btn(browser_driver,xpath, **kwargs):
    clickable_btn = None
    default_exception_to_ignore = [ElementNotSelectableException, ElementNotInteractableException,
                                   ElementNotVisibleException, NoSuchElementException]
    if  "list_error_to_ignored" in  kwargs:
        default_exception_to_ignore = kwargs["list_error_to_ignored"]
    if "wait_time" in kwargs and "freequence" in kwargs:
        try:
            clickable_btn = WebDriverWait(browser_driver, kwargs["wait_time"] , poll_frequency=kwargs["list_error_to_ignored"],
                                        ignored_exceptions=default_exception_to_ignore) \
                .until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        except:
            print(f"unable to click button {xpath}\n")
    
    

def send_text(browser_driver,  xpath, text, **kwargs):
    default_exception_to_ignore = [ElementNotSelectableException, ElementNotInteractableException,
                                   ElementNotVisibleException, NoSuchElementException]
    try:
        if  "list_error_to_ignored" in  kwargs:
            default_exception_to_ignore = kwargs["list_error_to_ignored"]
        if "wait_time" in kwargs and "freequence" in kwargs:
            WebDriverWait(browser_driver, kwargs["wait_time"], poll_frequency=kwargs["frequence"],
                                ignored_exceptions=default_exception_to_ignore) \
                                .until(EC.presence_of_element_located((By.XPATH, xpath))) \
                                    .send_keys(text)
        else:
            WebDriverWait(browser_driver, 5, poll_frequency=1,
                                ignored_exceptions=default_exception_to_ignore) \
                                .until(EC.presence_of_element_located((By.XPATH, xpath)))\
                                .send_keys(text)
    except:
        raise Exception(
            "ISSUE: can't send text.\nSUGGESTION: check xpath.\n")
#perform click action using javascript
def java_script_click(browser_driver, xpath):
    button = find_element_by_xpath(browser_driver,)
    browser_driver.execute_script("arguments[0].click();", button)
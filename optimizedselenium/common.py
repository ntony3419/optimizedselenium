from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    # TODO: developing type_text simulation

def type_text(browser_driver, wait_time, frequence, list_error_to_ignored, xpath, text):
    default_exception_to_ignore = [ElementNotSelectableException, ElementNotInteractableException,
                                   ElementNotVisibleException, NoSuchElementException]
    element = WebDriverWait(browser_driver, wait_time, poll_frequency=frequence,
                            ignored_exceptions=list_error_to_ignored) \
        .until(EC.presence_of_element_located((By.XPATH, xpath)))

def get_element_by_xpath(browser_driver, wait_time, frequence, list_error_to_ignored, xpath):
    getable_ele = None
    default_exception_to_ignore = [ElementNotSelectableException, ElementNotInteractableException,
                                   ElementNotVisibleException, NoSuchElementException]
    if list_error_to_ignored is None:
        list_error_to_ignored = default_exception_to_ignore
    try:
        getable_ele = WebDriverWait(browser_driver, wait_time, poll_frequency=frequence,
                                    ignored_exceptions=list_error_to_ignored) \
            .until(EC.presence_of_element_located((By.XPATH, xpath)))
    except:
        pass
    # send post data to the input field
    return getable_ele

def get_elements_by_xpath(browser_driver, wait_time, frequence, list_error_to_ignored, xpath):
    getable_ele = []
    default_exception_to_ignore = [ElementNotSelectableException, ElementNotInteractableException,
                                   ElementNotVisibleException, NoSuchElementException]
    if list_error_to_ignored is None:
        list_error_to_ignored = default_exception_to_ignore

    found = False
    while (found is False and frequence <=wait_time):
        try:
            getable_ele = browser_driver.find_elements_by_xpath(xpath)
            found = True
        except:
            pass
        frequence = frequence+1

    # send post data to the input field
    return getable_ele

def clickable_btn(browser_driver, wait_time, frequence, list_error_to_ignored, xpath):
    clickable_btn = None
    default_exception_to_ignore = [ElementNotSelectableException, ElementNotInteractableException,
                                   ElementNotVisibleException, NoSuchElementException]
    if list_error_to_ignored is None:
        list_error_to_ignored = default_exception_to_ignore
    try:
        clickable_btn = WebDriverWait(browser_driver, wait_time, poll_frequency=frequence,
                                      ignored_exceptions=list_error_to_ignored) \
            .until(EC.element_to_be_clickable((By.XPATH, xpath)))
    except:
        pass
    # send post data to the input field
    return clickable_btn

def send_text(browser_driver, wait_time, frequence, list_error_to_ignored, xpath, text):
    default_exception_to_ignore = [ElementNotSelectableException, ElementNotInteractableException,
                                   ElementNotVisibleException, NoSuchElementException]
    if list_error_to_ignored is None:
        list_error_to_ignored = default_exception_to_ignore
    try:
        WebDriverWait(browser_driver, wait_time, poll_frequency=frequence, ignored_exceptions=list_error_to_ignored) \
            .until(EC.presence_of_element_located((By.XPATH, xpath))) \
            .send_keys(text)
    except:
        raise Exception(
            "ISSUE: can't send text.\nSOLUTION: update xpath for text field.\nBetter to update xpath before press OK")


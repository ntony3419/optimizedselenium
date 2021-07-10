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

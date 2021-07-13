import random

import undetected_chromedriver.v2 as uc_ori
from time import sleep
from optimizedselenium.undetectchrome import Undetect_Chrome
from optimizedselenium import common as br_common_act
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# driver = uc_ori.Chrome()
# with driver:
#     driver.get('https://freecoursesite.com')
#
#uc = Undetect_Chrome(r"C:\Users\quang nguyen\PycharmProjects\python\optimizedselenium\optimizedselenium\chromedriver.exe",None,None,None,False,False)
uc = Undetect_Chrome(r"C:\Users\quang nguyen\PycharmProjects\python\optimizedselenium\optimizedselenium\chromedriver.exe",r"C:\Users\quang nguyen\AppData\Local\Google\Chrome\User Data","Profile 3",None,False,False)
driver = uc.browser_driver()
try:
    driver.get('https://freecoursesite.com')
except:
    pass
finally:
    driver.quit()
# with driver:
#     driver.get('https://freecoursesite.com')
#     sleep(random.randint(10,15))
    # title=br_common_act.get_element_by_xpath(driver,100,5,None,'''(//h2[contains(@class,"title")])[1]''').text
    # print(title)
    # element = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '''(//h2[contains(@class,"title")])[1]'''))
    # )
    # title=element.text
    # print(title)

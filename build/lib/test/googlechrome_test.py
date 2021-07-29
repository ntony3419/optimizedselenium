

from optimizedselenium.googlechrome import Chrome_Browser
from optimizedselenium import common as br_com_act
from time import sleep
bro = Chrome_Browser(driver_path=r"optimizedselenium\chromedriver_91.exe",profile_path=None,profile_number=None, window_size="800,600",maximize=True,headless=False)
#bro = Chrome_Browser(driver_path=r"optimizedselenium\chromedriver_90.exe",profile_path=r"C:\Users\quang nguyen\AppData\Local\Google\Chrome\User Data",profile_number="Profile 3", window_size=None,maximize=False,headless=False)
browser=bro.browser_driver()
browser.get(r"https://projectjav.com/")

test=br_com_act.get_element_by_xpath(browser, 10, 1, None,
                                             '''/html/body/main/div[1]/div[3]/div[1]/div/div/h1''').text
sleep(10)
browser.quit()
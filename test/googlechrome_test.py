

from optimizedselenium.googlechrome import Chrome_Browser
from optimizedselenium import common as br_com_act
from time import sleep
bro = Chrome_Browser(driver_path=r"C:\Users\Administrator\PycharmProjects\python\optimizedselenium\chromedriver_96.exe",profile_path=None,profile_number=None, window_size="800,600",maximize=True,headless=False)

browser=bro.browser_driver()
browser.get(r"https://vieclamdanang.vn/viec-lam?order_by=updated")

test=br_com_act.find_element_by_xpath(browser,    '''//*[@id="list-item"]/div[1]/div/div[2]/div/h3/a''').text
sleep(10)
browser.quit()
import random
import time
from optimizedselenium.undetectchrome import Undetect_Chrome
from optimizedselenium import common as br_common_act
uc = Undetect_Chrome(r"C:\Users\quang nguyen\PycharmProjects\python\optimizedselenium\chromedriver.exe", None, None, None, False, False)
driver = uc.browser_driver()
with driver: #open the url once to pass the cloudflare test
    driver.get('https://freecoursesite.com')
time.sleep(random.randint(10,20))
title=br_common_act.get_element_by_xpath(driver,10,2,None,'''(//h2[contains(@class,"title")])[1]''').text
print(title)
driver.quit()

#
#uc = Undetect_Chrome(r"C:\Users\quang nguyen\PycharmProjects\python\optimizedselenium\optimizedselenium\chromedriver_91.exe",None,None,None,False,False)
# uc = Undetect_Chrome(r"C:\Users\quang nguyen\PycharmProjects\python\optimizedselenium\optimizedselenium\chromedriver_91.exe",r"C:\Users\quang nguyen\AppData\Local\Google\Chrome\User Data","Profile 5",None,False,False)
# driver = uc.browser_driver()
# # try:
# # try:
# #     driver.get('https://freecoursesite.com')
# # except:
# #     pass
# # print("test")
# # driver.quit()
# #     # sleep(random.randint(10,15))
# # except:
# #     pass
# # finally:
# #     driver.quit()
# # with driver:
# #     driver.get('https://freecoursesite.com')
# #     #title=br_common_act.get_element_by_xpath(driver,100,5,None,'''(//h2[contains(@class,"title")])[1]''').text
# #     count =0
# #     while count < 1000000:
# #         count+=1
# #         print(count)
# #     # title=br_common_act.get_element_by_xpath(driver,100,5,None,'''(//h2[contains(@class,"title")])[1]''').text
# #     print("title")
#     # element = WebDriverWait(driver, 10).until(
#     #     EC.presence_of_element_located((By.XPATH, '''(//h2[contains(@class,"title")])[1]'''))
#     # )
#     # title=element.text
#     # print(title)

import random
import time
from optimizedselenium.undetectchrome import Undetect_Chrome
import undetected_chromedriver.v2 as uc_2
if __name__=="__main__":
    #browser = uc_2.Chrome()
    browser = Undetect_Chrome(r"C:\Users\Administrator\PycharmProjects\python\optimizedselenium\chromedriver.exe", maximize=True).driver_browser
    with browser: #open the url once to pass the cloudflare test
        browser.get('https://freecoursesite.com')

#from optimizedselenium import common as br_common_act

# uc = Undetect_Chrome(r"C:\Users\quang nguyen\PycharmProjects\python\optimizedselenium\chromedriver.exe", None, None, None, False, False)
# driver = uc.browser_driver()
# with driver: #open the url once to pass the cloudflare test
#     driver.get('https://freecoursesite.com')


#title=br_common_act.get_element_by_xpath(driver,10,2,None,'''(//h2[contains(@class,"title")])[1]''').text
#print(title)
#driver.quit()
# import undetected_chromedriver.v2 as uc_2
# from optimizedselenium import common as br_common_act
# driver_2 = uc_2.Chrome()
# with driver_2:
#     driver_2.get('https://freecoursesite.com')
# not_pass = True
# while not_pass:
#     time.sleep(random.uniform(5.0, 10.0))  # must have this line to wait for the validation of cloudflare
#     try:
#         home_btn = driver_2.find_element_by_id("main-navigation")
#         not_pass = False #passed the cloudflare
#     except:
#         pass

# title=br_common_act.get_element_by_xpath(driver_2,10,2,None,'''(//h2[contains(@class,"title")])[1]''').text
# print(title)
# driver_2.quit()

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

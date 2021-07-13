

from optimizedselenium.googlechrome import Chrome_Browser
from time import sleep
#bro = Chrome_Browser(driver_path=r"optimizedselenium\chromedriver_90.exe",profile_path=None,profile_number=None, window_size="800,600",maximize=True,headless=False)
bro = Chrome_Browser(driver_path=r"optimizedselenium\chromedriver_90.exe",profile_path=r"C:\Users\quang nguyen\AppData\Local\Google\Chrome\User Data",profile_number="Profile 3", window_size=None,maximize=False,headless=False)
browser=bro.browser_driver()
browser.get(r"https:\\google.com")
sleep(10)
browser.quit()
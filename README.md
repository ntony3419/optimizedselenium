How to Build and install the package
1. download the package
   <pre>git clone https://github.com/ntony3419/optimizedselenium.git --depth 1 --branch=master
</pre>

2. change directory to the package where the setup.py located
   <pre>cd path/to/optimizedselenium</pre>
3. Build the package : 
   <pre>python setup.py bdist_wheel</pre>
   
Copy the path of wheelfile.whl in folder "dist"
4. install the package : 
   <pre>pip install /path/to/wheelfile.whl</pre>

How to use the package:
import optimizedselenium
from optimizedselenium.googlechrome import Chrome_Browser

How to open an url:

<pre>
import optimizedselenium
from optimizedselenium.googlechrome import Chrome_Browser
chrome_object = Chrome_Browser(driver_path=path_to_googlechrome.exe, profile_path="C://google/Profile/, profile_number=profile 1, window_size=None,maximize=True, headless=False)
chrome_object.browser_driver.get("https://google.com")
</pre>

How to use undetect browser example
<pre>
import random
import time
from optimizedselenium.undetectchrome import Undetect_Chrome
from optimizedselenium import common as br_common_act
uc = Undetect_Chrome(r"C:\Users\quang nguyen\PycharmProjects\python\optimizedselenium\optimizedselenium\chromedriver_91.exe", None, None, None, False, False)
driver = uc.browser_driver()

with driver: #open the url once to pass the cloudflare test
    driver.get('https://freecoursesite.com')
    #do not put any code inside the with or the cloudflare will detect

time.sleep(random.randint(10,20))  
title=br_common_act.get_element_by_xpath(driver,10,2,None,'''(//h2[contains(@class,"title")])[1]''').text
print(title)
driver.quit()
</pre>
It is important to notify line 7 to 9 in the example, the browser must open a cloudflare protected url before the browser can be used for scraping
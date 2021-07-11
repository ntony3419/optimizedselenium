How to Build and install the package
1. download the package
2. extract the package
3. change directory to the package where the setup.py located
4. Build the package : python setup.py bdist_wheel
   
Copy the path of wheelfile.whl in folder "dist"
5. install the package : pip install /path/to/wheelfile.whl

How to use the package:
import optimizedselenium
from optimizedselenium.googlechrome import Chrome_Browser

How to open an url
import optimizedselenium
from optimizedselenium.googlechrome import Chrome_Browser
chrome_object = Chrome_Browser(driver_path=path_to_googlechrome.exe, profile_path="C://google/Profile/, profile_number=profile 1, window_size=None,maximize=True, headless=False)
chrome_object.browser_driver.get("https://google.com")
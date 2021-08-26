import undetected_chromedriver.v2 as uc
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *

class Undetect_Chrome(uc.Chrome):
    def __init__(self):
        super.__init__()


        # self.options = uc.ChromeOptions()
        #
        # # default options
        # self.window_size = None
        # self.maximize = False
        # self.headless = False
        # if headless is True:
        #     self.options.add_argument("--headless")
        #     self.headless = True
        # else:  # maximize and windowsize depend on headless status
        #     if maximize is True:
        #         self.maximize = True
        #     if window_size is not None:
        #         self.window_size = window_size.split(",")
        # #self.options.add_argument("--no-sandbox")
        # #self.options.add_argument("--disable-dev-shm-usage")
        #
        # if profile_path is not None and profile_number is not None:
        #     combine_path = r"{}\{}".format(profile_path, profile_number)
        #     # self.options.add_argument(combine_path)
        #     profile_path = r"--user-data-dir={}".format(profile_path)
        #     profile = r"--profile-directory={}".format(profile_number)
        #     self.options.add_argument(profile_path)
        #     self.options.add_argument(profile)
        #     #self.options.user_data_dir=combine_path
        # self.options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
        # self.driver_path = driver_path
    def browser_driver(self):
        driver = None
        try:
            driver=uc.Chrome( executable_path=self.driver_path,options=self.options)
            # if self.maximize is True:
            #     driver.maximize_window()
            # if self.window_size is not None and self.maximize is False:
            #     driver.set_window_size(self.window_size[1], self.window_size[0])

        except (WebDriverException, FileNotFoundError):
            print(
                f"Can't find the executable <.exe> of google chrome at <{self.driver_path}> !!\nMake sure the executable file and path to its executable in setting.conf match each other!!\nAttemp to use full path to the executable!!")
            exit()

            # print(traceback.format_exc())
            # raise Exception(f"Unable to open browser with according profile."
            #                  f"Possible issue and solution: "
            #                  f"\n- Profile is in used: Close all the google chrome tabs to release the profile"
            #                  f"\n- Chrome Driver doesn't exist: download chrom driver associate with chrome version from https://chromedriver.chromium.org/downloads"
            #                  f"\n- Chrome Driver version different: download new chrome driver assosicate with chrome version from https://chromedriver.chromium.org/downloads")
        return driver


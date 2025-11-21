from utils.driver import getChromeDriver
from utils.utils import open_flipkart_website

from Page.mobile import Mobile

driver = None
def setup_function():
    global driver
    driver = getChromeDriver()


def teardown_function():
    global driver
    # if driver:
    #     driver.quit()

def test_mobile_page():
    open_flipkart_website(driver)
    mobile_obj = Mobile(driver)
    mobile_obj.open_mobile_page()



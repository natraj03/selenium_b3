from utils.driver import getChromeDriver
from utils.utils import open_flipkart_website
from Constants.constants import terms_page

from Page.terms import Terms

driver = None
def setup_function():
    global driver
    driver = getChromeDriver()


def teardown_function():
    global driver
    if driver:
        driver.quit()

def test_terrms_page():
    open_flipkart_website(driver, terms_page)
    term_obj = Terms(driver)
    assert term_obj.open_corporate_page() == "Flipkart Terms of Use check"
    # mobile_obj.click_on_apple()



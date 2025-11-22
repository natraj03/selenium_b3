from selenium.webdriver.common.by import By


class Terms:

    def __init__(self, driver):
        self.driver = driver

    def open_corporate_page(self):
        self.driver.implicitly_wait(5)
        terms_element = self.driver.find_element(By.XPATH, "//p[text()='Flipkart Terms of Use']")
        return terms_element.text

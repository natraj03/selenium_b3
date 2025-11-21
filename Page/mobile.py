from selenium.webdriver.common.by import By


class Mobile:

    def __init__(self, driver):
        self.driver = driver

    def open_mobile_page(self):
        self.driver.find_element(By.XPATH, "//a[contains(@href, '/mobile-phones-store')]").click()


from selenium.webdriver.common.by import By


class Mobile:

    def __init__(self, driver):
        self.driver = driver

    def open_mobile_page(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//a[contains(@href, '/mobile-phones-store')]").click()

    def click_on_apple(self):
        self.driver.implicitly_wait(9)
        self.driver.find_element(By.XPATH, "//div[@title='Apple']//input").click()

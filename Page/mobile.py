from selenium.webdriver.common.by import By


class Mobile:

    def __init__(self, driver):
        self.driver = driver

    def open_mobile_page(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//a[contains(@href, '/mobile-phones-store') and @aria-label='Mobiles & Tablets']").click()

    def click_on_apple(self):
        self.driver.implicitly_wait(9)
        self.driver.find_element(By.XPATH, "//div[@title='Apple']//input").click()

    def click_on_8gb(self):
        self.driver.implicitly_wait(5)
        gb_element =  self.driver.find_element(By.XPATH,"//section[.//div[text()='RAM']]//label[.//div[text()='8 GB and Above']]")
        self.driver.execute_script("arguments[0].scrollIntoView;",gb_element)
        self.driver.implicitly_wait(1)
        gb_element.click()

    def click_on_mobile(self):
        self.driver.implicitly_wait(5)
        phone_element = self.driver.find_element(By.XPATH,"//a[.//div[text()='MOTOROLA Edge 60 Fusion 5G (PANTONE Amazonite, 256 GB)']]")
        self.driver.execute_script("arguments[0].scrollIntoView;", phone_element)
        self.driver.implicitly_wait(1)
        phone_element.click()

    def click_on_view_details(self):
        self.driver.implicitly_wait(5)
        phone_element = self.driver.find_element(By.XPATH,"//a[text()='12 GB']")
        self.driver.execute_script("arguments[0].scrollIntoView;", phone_element)
        phone_element.click()

